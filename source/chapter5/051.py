"""
bag of words的なことをしたいが，そのままやると文数1万と語彙サイズ1万とかでデータ量が心配なので，適当に出現頻度で絞って語彙サイズを減らし，データ量削減してます
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from collections import Counter
from nltk import word_tokenize
from tqdm import tqdm

def merge_data():
    file_names = ['train.txt', 'test.txt', 'valid.txt']
    labels = []
    titles = []
    for file_name in file_names:
        with open(file_name) as fp:
            for line in fp:
                label, title = line.split('\t')
                labels.append(label)
                titles.append(word_tokenize(title))
    return labels, titles

def write(file_name, X, y):
    out = open(file_name, "w")
    for idx in range(len(X)):
        if idx == 0:
            print(X[idx][:5])
        out.write(labels[idx] + '\t' + ' '.join(map(str, X[idx])) + '\n')


def extract_feature(labels, titles):
    all_words = []
    for title in titles:
        for token in title:
            all_words.append(token)

    # print(all_words)
    counter = Counter(all_words)
    for idx, title in enumerate(titles):
        titles[idx] = ' '.join([token for token in title if 10<counter[token]<300])
    # print(titles)

    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(titles)
    X_arr = X.toarray()
    
    data_size = len(X_arr)
    train_X = X_arr[:int(data_size*0.8)]
    val_X = X_arr[int(data_size*0.8):int(data_size*0.9)]
    test_X = X_arr[int(data_size*0.9):]
    

    train_y = labels[:int(data_size*0.8)]
    val_y = labels[int(data_size*0.8):int(data_size*0.9)]
    test_y = labels[int(data_size*0.9):]

    write('train.feature.txt', train_X.tolist(), train_y)
    write('test.feature.txt', test_X.tolist(), test_y)
    write('valid.feature.txt', val_X.tolist(), val_y)

    feature_name = tfidf.get_feature_names()
    out = open("feature_name.txt", "w")
    out.write(' '.join(feature_name))
    

labels, titles = merge_data()
extract_feature(labels, titles)
