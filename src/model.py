
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def create_popularity_model(filtered_df):
    avg_rating = filtered_df.groupby('Book-Title')['Book-Rating'].mean()
    num_ratings = filtered_df.groupby('Book-Title')['Book-Rating'].count()

    pop_df = pd.DataFrame({
        'avg_rating': avg_rating,
        'num_of_ratings': num_ratings
    }).reset_index()

    # Join images and author
    book_info = filtered_df.drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Image-URL-M']]
    popular_df = pop_df.merge(book_info, on='Book-Title')
    popular_df = popular_df.sort_values(by='avg_rating', ascending=False).head(50)
    return popular_df

def compute_similarity_matrix(pt):
    similarity = cosine_similarity(pt)
    return similarity
