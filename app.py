## import libraries

import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd


st.set_page_config(layout="wide")

st.header("Book Recommendation System")

st.markdown('''
           ##### This site using collaborative filtering suggests books from our catalog.
           ##### we recommend top 50 books for every one as well.
           ''')


##import our models:
popular = pkl.load(open('popular.pkl','rb'))
books = pkl.load(open('books.pkl','rb'))
pt = pkl.load(open('pt.pkl','rb'))
similiarity_scores = pkl.load(open('similiarity_scores.pkl','rb'))

## Top 50 books
st.sidebar.title("Top 50 books")

if st.sidebar.button("SHOW"):
    cols_per_row = 5 
    num_rows = 10 
    for row in range(num_rows): 
        cols = st.columns(cols_per_row)
        for col in range(cols_per_row): 
            book_idx = row * cols_per_row + col
            if book_idx < len(popular):
                with cols[col]:
                    st.image(popular.iloc[book_idx]['Image-URL-M']) # Displays the image
                    st.text(popular.iloc[book_idx]['Book-Title']) # Displays the Book Title
                    st.text(popular.iloc[book_idx]['Book-Author']) # Display the Author name



def recommend(book_name):
    index = np.where(pt.index==book_name)[0][0]
    similiar_items = sorted(list(enumerate(similiarity_scores[index])),key=lambda x : x[1] , reverse=True)[1:6]
     ## lets create an emply list and in that list i want to popoluate with the book info
    
    data = []
    for i in similiar_items:
        item = [] 
        temp_df = books[books['Book-Title']==pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return data   

## this is giving the name list of books
book_list = pt.index.values

st.sidebar.title("Similiar Book Suggestions")
selected_books = st.sidebar.selectbox("Select a book from dropdown",book_list)


if st.sidebar.button("Recommend Me"):
    book_recommend = recommend(selected_books)
    cols = st.columns(5)
    for col_idx in range(5):
        with cols[col_idx]:
            if col_idx < len(book_recommend):
                st.image(book_recommend[col_idx][2]) # Displays the image
                st.text(book_recommend[col_idx][0]) # Displays the Book Title
                st.text(book_recommend[col_idx][1]) # Display the Author name


## import data
books = pd.read_csv(
    'archive/Books.csv',
    dtype={'Year-Of-Publication': str},
    low_memory=False
)
users = pd.read_csv('archive/Users.csv')
ratings = pd.read_csv('archive/Ratings.csv')

st.sidebar.title("Data Used")

if st.sidebar.button("Show Data"):
    st.subheader("This is the book data that we used in our model")
    st.dataframe(books)
    st.subheader("This is the users data that we used in our model")
    st.dataframe(users)
    st.subheader("This is the user ratings data that we used in our model")
    st.dataframe(ratings)
