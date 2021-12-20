import streamlit as st
import pandas as pd


st.title('Clustering Sci-Fi movies by scripts using Topic Modeling with LDA (Latent Dirichlet Allocation)')

st.write('The main goal of this project is to clusterize Sci-Fi movies by its scripts, defining a dominant topic for each movie (script) in order to form groups alike. A next step would be to be able to infer the topics and thus classify new movies (scripts).')
st.write('The scripts ara available on https://imsdb.com/genre/Sci-Fi')
st.write('It was divided in 3 topics shown below:')
st.image('.//assets//topic_distrib.png')
st.write('It was generated a Wordcloud for each topic:')
st.image('.//assets//wordcloud_topics.png')

dataset = pd.read_csv('Data/df_concat.csv',sep=';')
dataset.drop(['0','1','2','script'], axis=1, inplace=True)

st.write('Select a topic to get a list of movies alike')
option = st.selectbox(
     'Topics:',
     (0, 1, 2))
st.write('Movies:', dataset[dataset['Topic']== option])




st.write('Learn more on https://www.analyticsvidhya.com/blog/2021/06/part-2-topic-modeling-and-latent-dirichlet-allocation-lda-using-gensim-and-sklearn/')

