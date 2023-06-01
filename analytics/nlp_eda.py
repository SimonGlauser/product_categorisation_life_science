import pandas as pd
from collections import Counter
## for plotting
import matplotlib.pyplot as plt
import seaborn as sns
import wordcloud
## for text processing
import re
import nltk
## for language detection
import langdetect
## for sentiment
from textblob import TextBlob
## for ner
import spacy
## for vectorizer
from sklearn import feature_extraction, manifold
## for topic modeling
import gensim

def eda_wordcloud(file):
    df = pd.read_csv(file, engine="pyarrow")
    print("file imported")
    print(df.info())
    #df['language'] = df["title"].apply(lambda x: langdetect.detect(x) if x.strip() != "" else "")
    #print(df.info())
    #data = dict(Counter(df.language))
    #df_language = pd.DataFrame.from_dict(data, orient='index', columns=["language_count"])
    #print(df_language)



def main():
    eda_wordcloud("../data_cleaning/data_clean/csv_combined.csv")

if __name__ == '__main__':
    main()