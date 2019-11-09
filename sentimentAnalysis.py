# import tensorflow as tf
import numpy as np
import nltk
import pandas as pd
import re
from termcolor import colored

# print(tf.__version__)
# print(np.__version__)
# print(nltk.__version__)

df_software = pd.read_json('data/Software_5.json', lines = True, encoding='utf-8')
df_science = pd.read_json('data/Industrial_and_Scientific_5.json', lines = True)

# print(df_software.head())

text = df_software['reviewText'].values
# text = df_science['reviewText'].values
text = [x for x in text if str(x) != "nan"]

print(colored('---------- TEXT ----------', 'green', attrs=['bold']))
print(text[10403])

def cleanText(string, ):
    
    print(colored('---------- NEW ----------', 'green', attrs=['bold']))
    print(string)
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    print(colored('---------- CLEAN ----------', 'green', attrs=['bold']))
    print(string.strip().lower())
    return string.strip().lower()

clean_text = [cleanText(sent) for sent in text]

# print(colored('---------- CLEAN TEXT ----------', 'red', attrs=['bold']))
# print(clean_text[0:2])