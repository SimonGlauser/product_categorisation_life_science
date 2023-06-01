import streamlit as st
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import regexp
word_tokenizer = regexp.WhitespaceTokenizer()
nltk.download('stopwords')
stop = stopwords.words('english')
new_stopwords = ["nan"]
stop.extend(new_stopwords)
porter = PorterStemmer()

#import LinearSVC.pkl

#streamlit run live_demonstration/app.py

def preprocess_text(text):
    ''' The function to remove punctuation,
    stopwords and apply stemming'''
    tokenized_text = [word.lower() for word in word_tokenizer.tokenize(text) if word.lower() not in stop]
    tokenized_text = [porter.stem(word) for word in tokenized_text]
    return " ".join(tokenized_text)

def remove_punctuation(old_string):
    """
    This function transforms a string into a string without punctuation
    Removed punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    :param old_string: string to transform
    :return: string without punctuation
    """
    if old_string is not None:
        new_string = old_string.translate(str.maketrans('', '', string.punctuation))
        return new_string


#@st.cache
def app():
    st.title("Live Demonstration")

    product_description = st.text_input("Product Description")

    if st.button("preprocess data"):
        st.write("Your current Product Description is:")
        st.subheader(product_description)
        st.write("let me preprocess that!")
        product_description_in_progress = remove_punctuation(product_description)
        product_description_cleaned = preprocess_text(product_description_in_progress)
        st.write("Your cleaned Product Description is:")
        st.subheader(product_description_cleaned)

    if st.button("find correct categorisation"):
        st.write("continue")




