from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np

def load_file(file_name):
    X = []
    y = []
    with open(file_name) as fp:
        for line in fp:
            label, feature = line.split('\t')
            X.append(list(map(float,feature.split())))
            y.append(label)
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(y)
    return X, y

def accuracy(y, pred):
    y = np.array(y)
    pred = np.array(pred)
    correct = sum(y == pred)

    return correct / len(y)



train_X, train_y = load_file('train.feature.txt')
test_X, test_y = load_file('test.feature.txt')
val_X, val_y = load_file('valid.feature.txt')

lr = LogisticRegression(solver='lbfgs')
lr.fit(train_X, train_y)

test_pred = lr.predict(test_X)
val_pred = lr.predict(val_X)
# print(test_pred[:10])
# print(val_pred[:10])
print(accuracy(test_y, test_pred)) # 0.3592814371257485
print(accuracy(val_y, val_pred)) # 0.3712574850299401





        
