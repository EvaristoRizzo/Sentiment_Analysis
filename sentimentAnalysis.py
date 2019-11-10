# import tensorflow as tf
import numpy as np
import pandas as pd
import re
from termcolor import colored
import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# print(tf.__version__)
# print(np.__version__)
# print(nltk.__version__)

df_software = pd.read_json('data/Software_5.json', lines = True, encoding='utf-8')
df_science = pd.read_json('data/Industrial_and_Scientific_5.json', lines = True,encoding='utf-8')

df = pd.concat([df_software, df_science])

# print(df_software.head())

df_text = df['reviewText'].values
df_score = df['overall'].values

print(len(df_text))
print(len(df_score))

# text_uncleaned = df_software['reviewText'].values
# score_uncleaned = df_software['overall'].values

# text_uncleaned = df_science['reviewText'].values
# score_uncleaned = df_science['overall'].values

# print(len(text_uncleaned))
# print(len(score_uncleaned))

# text = [x for x in text if str(x) != "nan"]

text = []
score = []
c = 0 

for i in range(len(df_text)):
    if str(df_text[i]) != "nan":
        text.append(df_text[i])
        score.append(df_score[i])
    else:
        c += 1
        print(i)

print(len(text))
print(len(score))
print(c)

# print(colored('---------- TEXT ----------', 'green', attrs=['bold']))
# print(text[10403])

def cleanText(string, ):
    # print(colored('---------- NEW ----------', 'green', attrs=['bold']))
    # print(string)
    string = re.sub(r"[-()\"#/@;:<>{}+=./|.!?,~]", "", string)
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
    # string = re.sub(r"use", "", string)
    # string = re.sub(r"used", "", string)
    # string = re.sub(r"one", "", string)
    string = re.sub(r"\s{2,}", " ", string)
    # print(colored('---------- CLEAN ----------', 'green', attrs=['bold']))
    # print(string.strip().lower())
    return string.strip().lower()

cleanT = []
for t in text:
    cleanT.append(cleanText(t))

# removing common words by using the Stopwords

stop_words =  ['if', 'do', '\'ve' , 'program' , 'window',  'windows', 'even' ,  'computer' ,'product' ,'software' ,'\'ll' , 'use', 'used', 'one' ,'n\'t' , '\'re' , '\'s' ,'few', "it's", "shouldn't", 'myself', 'its', 'has', 'with', 'been', 'can', 'won', "you'll", 'below', "weren't", 'into', 'him', 'this', 'above', 'our', "needn't", 'here', 'i', 'me', 'all', 're', "won't", 'don', 'should', 'such', 'or', 'for', "couldn't", 'what', "should've", 'does', 'hers', 'other', "that'll", "doesn't", "wasn't", 'once', 'while', 'between', 'mightn', "hasn't", 'too', 'up', 'before', 'their', 'himself', 'it', "you'd", 'some', 'themselves', 'ain', 'an', 'ours', 'at', 'haven', 'about', 'just', 'shouldn', 'o', 'both', 'out', "isn't", 'll', 'ma', 'you', "haven't", 'only', 'hadn', 'those', 'they', 'against', 'down', 'over', 't', 'she', 'again', 'why', 'did', 'wouldn', 'a', 'when', 'your', 'ourselves', 'who', 'having', 'on', 'y', 'theirs', 'being', 'herself', 'nor', 'that', 'by', "don't", "mustn't", "shan't", 'because', 'not', 'under', 'are', 'he', 'own', "you've", 'there', 'yours', 'and', 'most', "mightn't", 'have', 'doing', 'during', 'couldn', "didn't", 'will', 'weren', 'd', 'were', "she's", "wouldn't", 'isn', 'then', 'doesn', 'wasn', 'itself', 'now', 'didn', 'these', 'them', 'needn', 'yourself', 'shan', 'is', 'more', 'be', "you're", 'than', 'after', 'aren', 'how', 'where', 'which', 'in', "hadn't", 'further', 'no', 'yourselves', 'as', 'whom', 'to', 'hasn', 'mustn', 'through', 'the', 'm', 's', 'very', 'we', 'each', 'until', 'same', "aren't", 'was', 'my', 'so', 'from', 've', 'am', 'had', 'his', 'but', 'off', 'any', 'of', 'her']
punctuation = list(string.punctuation)

stop = stop_words + punctuation

clean_text = []

for s in cleanT:
    sentence = s
    sent_words = sentence.split()
    words = [i for i in sent_words if i not in stop]
    output = ' '.join(words)
    clean_text.append(output)

# print(colored('---------- CLEAN TEXT ----------', 'green', attrs=['bold']))
# for s in clean_text[0:10]:
#     print(colored('---------- NEXT ----------', 'red', attrs=['bold']))
#     print(s)
# print(score[0:10])

# Classifing reviews by their overall rating
# print(len(score))
# print(len(clean_text))

positive_reviews = []
positive_score = []
negative_reviews = []
negative_score = []

for i in range(len(score)):
    if score[i] == 5:
        positive_reviews.append(clean_text[i])
        positive_score.append(score[i])
    elif score[i] == 1:
        negative_reviews.append(clean_text[i])
        negative_score.append(score[i])

print(len(positive_reviews))
print(len(positive_score))
print(len(negative_reviews))
print(len(negative_score))

# >= 3
# 83239
# 83239
# 6637
# 6637

def wordcloud_draw(data, color = 'black'):
    words = ' '.join(str(data))
    cleaned_word = " ".join([word for word in words.split()])
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color=color, width=2500, height=2000).generate(data)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

negative_words = ""

for i in range(len(negative_reviews)):
    negative_words += str(negative_reviews[i])

positive_words = ""

for i in range(len(positive_reviews[0:100])):
    positive_words += str(positive_reviews[i])


wordcloud_draw(negative_words)
wordcloud_draw(positive_words, 'white')