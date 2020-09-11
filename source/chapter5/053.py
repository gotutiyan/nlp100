from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression

def load_file(file_name):
    X = []
    y = []
    with open('train.feature.txt') as fp:
        for line in fp:
            label, feature = line.split('\t')
            X.append(list(map(float,feature.split())))
            y.append(label)
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(y)
    return X, y

train_X, train_y = load_file('train.feature.txt')
test_X, test_y = load_file('test.feature.txt')
val_X, val_y = load_file('val.feature.txt')

lr = LogisticRegression(solver='lbfgs')
lr.fit(train_X, train_y)

test_pred = lr.predict_proba(test_X)
print(test_pred[:3])

'''
[[0.15095255 0.35795748 0.35941637 0.1316736 ]
 [0.09030144 0.43587996 0.0217784  0.4520402 ]
 [0.08716688 0.86318547 0.03594396 0.01370369]]
'''



        
