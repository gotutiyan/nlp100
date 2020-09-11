from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from tqdm import tqdm

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
Cs = np.arange(0.1, 3.0, 0.1)
train_score = []
test_score = []
val_score = []
for c in tqdm(Cs): 
    lr = LogisticRegression(solver='lbfgs', C=c)
    lr = lr.fit(train_X, train_y)
    train_score.append(lr.score(train_X, train_y))
    test_score.append(lr.score(test_X, test_y))
    val_score.append(lr.score(val_X, val_y))

plt.plot(Cs, train_score, label='train')
plt.plot(Cs, test_score, label='test')
plt.plot(Cs, val_score, label='val')
plt.legend()
plt.show()
plt.close()




        
