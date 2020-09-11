from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from tqdm import tqdm
import xgboost as xgb

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

labels = ['t', 'e', 'b', 'm']
le = preprocessing.LabelEncoder()
le.fit(labels)

train_X, train_y = load_file('train.feature.txt', le)
test_X, test_y = load_file('test.feature.txt', le)

lr = LogisticRegression(solver='lbfgs')
lr.fit(train_X, train_y)

xgb = xgb.XGBClassifier()
xgb.fit(np.array(train_X), np.array(train_y))

print('--LogisticRegression--')
print(lr.score(test_X, test_y))
print('--XGBClassifier--')
print(xgb.score(np.array(test_X), np.array(test_y)))

'''
--LogisticRegression--
0.3592814371257485
--XGBClassifier--
0.3615269461077844
'''