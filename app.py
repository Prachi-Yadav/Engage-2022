import streamlit as st
import pickle
import pandas as pd


def recommend(anime):
    anime_index = animes[animes['title'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_animes = []
    for i in anime_list:
        recommended_animes.append(animes.iloc[i[0]].title)

    return recommended_animes


anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
animes = pd.DataFrame(anime_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('WoebegoneWeeb')

selected_anime_name = st.selectbox(
    'Select your Anime',
    animes['title'].values)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_anime_name)
    for i in recommendations:
        st.write(i)
