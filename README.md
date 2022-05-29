# Engage-2022
I developed this website using Streamlit. It's a Content Based Anime Recommender System. It will Recommend you 10 animes related to your chosen anime.

# Main Recommendation Engine.ipynb
import numpy
import pandas
import sklearn
import nltk 
It's a notebook where I built my recommendation engine. Firstly I did some processing on my dataset then made tags then did vectorization on tags after that wrote main function. then generated pickle and dict file of anime dataframe and similarity matrix to upload it on my web app.

# app.py
import streamlit
import pickle
import pandas
upload dict and and pickle file here 
Run it on server by using command "streamlit run app.py"

#Trial Engine!!
It's the engine that I made in starting by directly applying cosine similarity. YOu can check this out too. Here, I added a graph too.
Do not use it for website. Use "Main Recommendation Engine"
