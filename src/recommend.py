def recommend(book_name, pt, books, similarity_scores, top_n=5):
    if book_name not in pt.index:
        return []

    index = pt.index.get_loc(book_name)
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n + 1]

    recommendations = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        
        if not temp_df.empty:
            title = temp_df['Book-Title'].values[0]
            author = temp_df['Book-Author'].values[0]
            image = temp_df['Image-URL-M'].values[0]

            # ✅ Fallback in case of missing/invalid image
            if isinstance(image, str) and image.startswith("http"):
                valid_image = image
            else:
                valid_image = "https://via.placeholder.com/150?text=No+Image"

            recommendations.append((title, author, valid_image))

    return recommendations
