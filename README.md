# Clustering Sci-Fi movies by scripts using Topic Modeling with LDA (Latent Dirichlet Allocation)


The main goal of this project is to clusterize Sci-Fi movies by its scripts, defining a dominant topic for each movie (script) in order to form groups alike.
A next step would be to be able to infer the topics and thus classify new movies (scripts).
### The scripts ara available on https://imsdb.com/genre/Sci-Fi
Divided in:

1. Scraping_movie_scripts.ipynb - Webscraping the scripts of each movie;
2. NLTK+NLP.ipynb - Script for the LDA Model and analysis;


## **Streamlit**
The visualization is also compiled into a streamlit script. To do this, just install the dependencies in requirements-streamlit.txt and run the following command:

```bash
streamlit run app.py
```

## References:
https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24
https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
https://www.analyticsvidhya.com/blog/2021/06/part-2-topic-modeling-and-latent-dirichlet-allocation-lda-using-gensim-and-sklearn/
