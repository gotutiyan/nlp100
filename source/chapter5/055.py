from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import confusion_matrix

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
# print(accuracy(test_y, test_pred)) # 0.3592814371257485
# print(accuracy(val_y, val_pred)) # 0.3712574850299401

print('test -->')
print(confusion_matrix(test_y, test_pred))
print('\nvalid -->')
print(confusion_matrix(val_y, val_pred))


'''
test -->
[[238 283  20  42]
 [222 233  18  39]
 [ 46  42   4   5]
 [ 64  66   9   5]]

valid -->
[[261 263  19  40]
 [232 222  26  32]
 [ 39  44   5   9]
 [ 67  64   5   8]]
 
 '''


        
