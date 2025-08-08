import streamlit as st
import pickle
import pandas as pd
import requests
import webbrowser



def recommend(movie):
    movie_index = movies[movies['title'] == movie]
    distances = similarity[movie_index.index[0]]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [] 
   
    # Ensure movie_index is not empty
    for i in movie_list:
       
        recommended_movies = [movies.iloc[i[0]]['title'] for i in movie_list]
          
    return recommended_movies 

    
movies_dict = pickle.load(open('movie_dict.pkl', 'rb')) 
movies = pd.DataFrame(movies_dict) 

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('🎬 Movie Recommendation System')

# Create a text input for the user to enter a movie name
selected_movie = st.text_input('Enter the movie Name:')
if selected_movie in movies['title'].values:
    selected_movie_name = movies[movies['title'] == selected_movie].index[0]
else:    
    selected_movie_name = st.selectbox('Select a movie to get recommendations:', movies['title'].values)
  

# Display the selected movie name
if st.button('Recommend'):
    name = recommend(selected_movie_name)
    col1, col2, col3, col4 = st.columns(4)
    with col1:      
        st.text(name[0])
    with col2:
        st.text(name[1])
    with col3:
        st.text(name[2])
    with col4:
        st.text(name[3])

        if col1 == name[0]:
            webbrowser.open_new_tab(f"https://www.themoviedb.org/search?query={name[0]}")
        elif col2 == name[1]:
            webbrowser.open_new_tab(f"https://www.themoviedb.org/search?query={name[1]}")
        elif col3 == name[2]:
            webbrowser.open_new_tab(f"https://www.themoviedb.org/search?query={name[2]}")
        elif col4 == name[3]:
            webbrowser.open_new_tab(f"https://www.themoviedb.org/search?query={name[3]}")
        else:
            st.write("No recommendations found.")