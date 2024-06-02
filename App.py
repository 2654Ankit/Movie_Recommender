import streamlit as st
import pickle
import pandas as pd
import requests

def fetchPoster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1e79649cc43e5c092090cb473c5e95a8&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        # fetch poster
        recommended_movies_poster.append(fetchPoster(movie_id))
        recommended.append(movies.iloc[i[0]].title)

    return recommended, recommended_movies_poster

st.title('Movie Recomender System')
movies_dict = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)
movie = st.selectbox('Enter movie name',  movies['title'].values)


if st.button('Recommend'):
    names, poster = recommend(movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

