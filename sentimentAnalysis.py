# import tensorflow as tf
import numpy as np
import pandas as pd
import re
from termcolor import colored
import string

# print(tf.__version__)
# print(np.__version__)
# print(nltk.__version__)

df_software = pd.read_json('data/Software_5.json', lines = True, encoding='utf-8')
df_science = pd.read_json('data/Industrial_and_Scientific_5.json', lines = True)

# print(df_software.head())

text_uncleaned = df_software['reviewText'].values
score_uncleaned = df_software['overall'].values

# text = df_science['reviewText'].values
# score = df_science['overall'].values

print(len(text_uncleaned))
print(len(score_uncleaned))

# text = [x for x in text if str(x) != "nan"]

text = []
score = []
c = 0 

for i in range(len(text_uncleaned)):
    if str(text_uncleaned[i]) != "nan":
        text.append(text_uncleaned[i])
        score.append(score_uncleaned[i])
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
    string = re.sub(r"\s{2,}", " ", string)
    # print(colored('---------- CLEAN ----------', 'green', attrs=['bold']))
    # print(string.strip().lower())
    return string.strip().lower()

cleanT = []
for t in text:
    cleanT.append(cleanText(t))

print(cleanT[0])

# text = [cleanText(sent) for sent in text[0]]

# removing common words by using the Stopwords

# stop_words =  ['if', 'do', '\'ve' , '\'s' ,'few', "it's", "shouldn't", 'myself', 'its', 'has', 'with', 'been', 'can', 'won', "you'll", 'below', "weren't", 'into', 'him', 'this', 'above', 'our', "needn't", 'here', 'i', 'me', 'all', 're', "won't", 'don', 'should', 'such', 'or', 'for', "couldn't", 'what', "should've", 'does', 'hers', 'other', "that'll", "doesn't", "wasn't", 'once', 'while', 'between', 'mightn', "hasn't", 'too', 'up', 'before', 'their', 'himself', 'it', "you'd", 'some', 'themselves', 'ain', 'an', 'ours', 'at', 'haven', 'about', 'just', 'shouldn', 'o', 'both', 'out', "isn't", 'll', 'ma', 'you', "haven't", 'only', 'hadn', 'those', 'they', 'against', 'down', 'over', 't', 'she', 'again', 'why', 'did', 'wouldn', 'a', 'when', 'your', 'ourselves', 'who', 'having', 'on', 'y', 'theirs', 'being', 'herself', 'nor', 'that', 'by', "don't", "mustn't", "shan't", 'because', 'not', 'under', 'are', 'he', 'own', "you've", 'there', 'yours', 'and', 'most', "mightn't", 'have', 'doing', 'during', 'couldn', "didn't", 'will', 'weren', 'd', 'were', "she's", "wouldn't", 'isn', 'then', 'doesn', 'wasn', 'itself', 'now', 'didn', 'these', 'them', 'needn', 'yourself', 'shan', 'is', 'more', 'be', "you're", 'than', 'after', 'aren', 'how', 'where', 'which', 'in', "hadn't", 'further', 'no', 'yourselves', 'as', 'whom', 'to', 'hasn', 'mustn', 'through', 'the', 'm', 's', 'very', 'we', 'each', 'until', 'same', "aren't", 'was', 'my', 'so', 'from', 've', 'am', 'had', 'his', 'but', 'off', 'any', 'of', 'her']
# punctuation = list(string.punctuation)

# stop = stop_words + punctuation


# clean_text = []

# sentence = cleanT[0]
# print(sentence)
# sent_words = sentence.split()
# print(sent_words)
# words = [i for i in sent_words if i not in stop]

# output = ' '.join(words)
# print(output)

# for s in cleanT[0]:
#     sent_words = str(s).split()
#     words = [i for i in sent_words if i not in stop and i[0] != "'"]
#     clean_text.append(' '.join(words))

# print(clean_text)

# for s in sentence:
#     clean_text.append(" ".join(i for i in word_tokenize(s.lower) if i not in stop))

# # clean_text.append(" ".join(i for i in sentence[0] if i not in stop))

# print(clean_text)