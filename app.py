import streamlit as st
from recommendations import get_recommendations, movies

st.set_page_config(layout = 'wide')
st.header('JinGyuflix')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like', movie_list)

if st.button('Recommend'):
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)
        
        idx = 0 
        for i in range(0, 2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1