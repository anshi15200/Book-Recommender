import pandas as pd

def preprocess(books, ratings, min_ratings=250):
    # Merge
    merged_df = ratings.merge(books, on='ISBN')

    # Filter active users and popular books
    num_ratings_df = merged_df.groupby('Book-Title').count()['Book-Rating'].reset_index()
    num_ratings_df.rename(columns={'Book-Rating': 'num_of_ratings'}, inplace=True)
    popular_books = num_ratings_df[num_ratings_df['num_of_ratings'] >= min_ratings]['Book-Title']
    filtered_df = merged_df[merged_df['Book-Title'].isin(popular_books)]

    # Create pivot table
    pt = filtered_df.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
    pt.fillna(0, inplace=True)

    return filtered_df, pt
