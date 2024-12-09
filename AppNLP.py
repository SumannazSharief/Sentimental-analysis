import pandas as pd
import numpy as np
import streamlit as st
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob


# Function to clean the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text


# Function to tokenize the text and remove stop words
def tokenize(text):
    text_tokens = word_tokenize(text)
    tokenize_text = [i for i in text_tokens if i not in stopwords.words('english')]
    return tokenize_text


# Function to lemmatize the text
def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    lemmatize_text = [lemmatizer.lemmatize(i) for i in text]
    return ' '.join(lemmatize_text)


def main():
    st.title('Sentiment Analysis WebApp')

    # User input for text
    text = st.text_area('Enter the text')

    # Analyze the sentiment
    if st.button('Analyze the sentiment'):
        if len(text) > 0:
            cleaned_text = clean_text(text)

            tokenized_text = tokenize(cleaned_text)

            lemmatized_text = lemmatize(tokenized_text)

            text_blob = TextBlob(lemmatized_text)

            tb_polarity = text_blob.sentiment[0]

            if tb_polarity > 0:
                st.success('The entered text has positive sentiments.')
                st.success('Polarity = {:.2f}'.format(tb_polarity))
            elif tb_polarity < 0:
                st.error('The entered text has negative sentiments.')
                st.error('Polarity = {:.2f}'.format(tb_polarity))
            elif tb_polarity == 0:
                st.warning('The entered text has neutral sentiments.')
                st.warning('Polarity = {:.2f}'.format(tb_polarity))
        else:
            st.write('Please enter the text.')


if __name__ == '__main__':
    main()
