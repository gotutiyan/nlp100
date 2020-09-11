'''
051.pyの時点で，単語をtfidfの値に置き換えたきり，単語情報は失ってしまっているため，top10の単語が何なのかが分かりません．
よって急遽051.pyでfeature_nameをファイルに保存し，本057.pyで呼び出すことで，featureとそのnameを対応させています．
'''
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import classification_report

def load_file(file_name, le):
    X = []
    y = []
    with open(file_name) as fp:
        for line in fp:
            label, feature = line.split('\t')
            X.append(list(map(float,feature.split())))
            y.append(label)
    y = le.transform(y)
    return X, y

def accuracy(y, pred):
    y = np.array(y)
    pred = np.array(pred)
    correct = sum(y == pred)

    return correct / len(y)

labels_real = ['science and technology', 'entertainment', 'business', 'health']
labels = ['t', 'e', 'b', 'm']
le = preprocessing.LabelEncoder()
le.fit(labels)

train_X, train_y = load_file('train.feature.txt', le)

lr = LogisticRegression(solver='lbfgs')
lr.fit(train_X, train_y)

coef = lr.coef_
# print(coef.shape, coef[:10])
features_asc_idx = []
for idx, category in enumerate(le.classes_):
    features_asc_idx.append(coef[idx].argsort())

feature_name = open("feature_name.txt", "r").read().split()
print('重みの高い特徴量')
for idx, label in enumerate(labels_real):
    print('--',label,'--')
    for i in features_asc_idx[idx][:10]:
        print(feature_name[i], end=" ")
    print()
print('\n重みの低い特徴量')
for idx, label in enumerate(labels_real):
    print('--',label,'--')
    for i in features_asc_idx[idx][-10:]:
        print(feature_name[i], end=" ")
    print()

'''
出力：
重みの高い特徴量
-- science and technology --
her star she chris apple ebola video facebook the game
-- entertainment --
china google says bank sales billion stocks ecb euro ceo
-- business --
fed stocks bank google ceo euro facebook ecb china profit
-- health --
stocks fed ecb her ukraine thrones euro movie dollar shares

重みの低い特徴量
-- science and technology --
oil profit dollar ukraine china euro ecb stocks bank fed
-- entertainment --
cyrus miley film wedding she kanye the paul movie chris
-- business --
health heart cases cdc study drug mers fda cancer ebola
-- health --
nasa mobile space gm fcc climate microsoft apple facebook google
'''
    





        
