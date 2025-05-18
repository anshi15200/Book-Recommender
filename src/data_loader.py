
import pandas as pd
def load_data(book_path,user_path,rating_path):
    Books=pd.read_csv("C:/Users/anshika/Documents/DATASETS/book recommendation dataset/Books.csv",low_memory=False)
    Ratings=pd.read_csv("C:/Users/anshika/Documents/DATASETS/book recommendation dataset/Ratings.csv")
    Users=pd.read_csv("C:/Users/anshika/Documents/DATASETS/book recommendation dataset/Users.csv")
    return  Books,Users,Ratings

