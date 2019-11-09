# import tensorflow as tf
import numpy as np
import nltk
import pandas as pd
import re

# print(tf.__version__)
# print(np.__version__)
# print(nltk.__version__)

df_software = pd.read_json('data/Software_5.json', lines = True)
# dt_science = pd.read_json('data/Industrial_and_Scientific_5.json', lines = True)

print(df_software.head())

text = df_software['reviewText'].values
print(text[0:2])

def cleanText(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text) 
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=./|.!?,~]", "", text)
    return text


clean_text = []

for t in text[0:1]:
    clean_text.append(cleanText(t))

print(clean_text[0])