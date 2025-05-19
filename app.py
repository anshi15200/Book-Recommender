import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
from src.recommend import recommend

# Define path to artifact files (updated)
artifact_path = 'artifacts/'

# Load precomputed files
popular_df = pickle.load(open(artifact_path + 'popular.pkl', 'rb'))
pt = pickle.load(open(artifact_path + 'pt.pkl', 'rb'))
books = pickle.load(open(artifact_path + 'books.pkl', 'rb'))
similarity_scores = pickle.load(open(artifact_path + 'similarity_scores.pkl', 'rb'))

# Streamlit App
st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("📚 Book Recommendation System")

# -------------------------------
# 📌 Recommendation Section
# -------------------------------
st.header("📚 Recommend Books")

book_list = pt.index.values
selected_book = st.selectbox("Type or select a book from the dropdown", book_list)

if st.button("Show Recommendation"):
    recommended_books = recommend(selected_book, pt, books, similarity_scores)

    for title, author, image in recommended_books:
        st.markdown(f"**{title}**")
        st.caption(author)

        # Debug print to console - helps you check the type of image
        print(f"Image type: {type(image)}, Image value: {image}")

        # Try to display image safely
        try:
            if isinstance(image, str):
                # Check if it looks like a URL
                if image.startswith('http'):
                    st.image(image, width=150)
                else:
                    # Assume it's a local file path, try to open it
                    img = Image.open(image)
                    st.image(img, width=150)
            elif isinstance(image, Image.Image):
                # Already a PIL image
                st.image(image, width=150)
            else:
                st.write("Image format not supported or missing.")
        except Exception as e:
            st.write(f"Error loading image: {e}")

        st.markdown("---")

# -------------------------------
# 🔥 Popular Books Section
# -------------------------------
st.header("🔥 Popular Books")

for i in range(len(popular_df)):
    cols = st.columns([1, 1, 4])
    with cols[0]:
        st.image(popular_df['Image-URL-M'].iloc[i], width=100)
    with cols[1]:
        st.markdown(f"{popular_df['Book-Title'].iloc[i]}")
        st.caption(f"{popular_df['Book-Author'].iloc[i]}")
