# Importing the packages
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=38e7cb248b98d580170fc97794693e01'.format(movie_id))
    data = response.json()
    # st.text(data)
    return "http://image.tmdb.org/t/p/w500" + data['poster_path']

# Logic and import for recommedations using ML
def recommend(movie_input):
    movie_index = movies[movies['title'] == movie_input].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True , key = lambda x:x[1])[1:6]  
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# dictionary created in the project loading here
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

# Converting the dictionary to dataframe from now can access dataframe using df methods like movies['title']
movies = pd.DataFrame(movies_dict)

# loading similarity pickle 
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

# Selectbox with movies name
selected_movie_name = st.selectbox(
    'Select Movie on which you want Recommendations?',
    movies['title'].values)

# button for recommend
if st.button('Recommend Movies'):
    names , posters = recommend(selected_movie_name)
    # poster is empty list

    col1 , col2 , col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(names[1])
    with col2:
        st.text(names[2])
        st.image(names[3])
    with col3:
        st.text(names[4])
        st.image(names[5])
    with col4:
        st.text(names[6])
        st.image(names[7])
    with col5:
        st.text(names[8])
        st.image(names[9])


# now bringing movies posters using movies id fetching from tmbd
# used API also

