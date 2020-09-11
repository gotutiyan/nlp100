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

labels = ['t', 'e', 'b', 'm']
le = preprocessing.LabelEncoder()
le.fit(labels)

train_X, train_y = load_file('train.feature.txt', le)
test_X, test_y = load_file('test.feature.txt', le)
val_X, val_y = load_file('valid.feature.txt', le)

lr = LogisticRegression(solver='lbfgs')
lr.fit(train_X, train_y)

test_pred = lr.predict(test_X)
val_pred = lr.predict(val_X)
# print(accuracy(test_y, test_pred)) # 0.3592814371257485
# print(accuracy(val_y, val_pred)) # 0.3712574850299401

print(classification_report(test_y, test_pred, target_names=le.classes_, labels=[0,1,2,3]))
'''
              precision    recall  f1-score   support

           b       0.42      0.41      0.41       583
           e       0.37      0.46      0.41       512
           m       0.08      0.04      0.05        97
           t       0.05      0.03      0.04       144

    accuracy                           0.36      1336
   macro avg       0.23      0.23      0.23      1336
weighted avg       0.34      0.36      0.35      1336
'''




        
