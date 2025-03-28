import pandas as pd
import streamlit as st
import pickle
import requests

# method 1 
# this is also correct 
# movies_List = pickle.load(open('movies.pkl','rb'))
# movie = movies_List['title'].values
# st.title('Movie Recommender System')

# text box
# option = st.selectbox(
#     "How would you like to be contacted?",
#    movie, key=1,
# )

# method 2
moviesList = pickle.load(open('movies_list_dict','rb'))
movies = pd.DataFrame(moviesList)
similarity = pickle.load(open('similarity','rb'))
def fetch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=781d6ae2ad389a8fc25c51a3bbe00e21&language=en-us'.format(movie_id))
    data =responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance =  similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse = True, key=lambda x: x[1])[1:6]
    recom_movies = []
    recom_movies_poster = []
    for i in movie_list:
        movieId = movies.iloc[i[0]].movie_id
        # fatch poster from API

        recom_movies.append(movies.iloc[i[0]].title)
        recom_movies_poster.append(fetch_poster(movieId))
    return recom_movies, recom_movies_poster


st.title('Movie Recommender System')

# text box
selected_movie = st.selectbox(
    "Choose any Movie",
    movies['title'].values, key=2,
)
if st.button('Recommend'):
    name, poster = recommend(selected_movie)

    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])





