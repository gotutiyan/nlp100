from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
labels = []
features = []
with open('train.feature.txt') as fp:
    for line in fp:
        label, feature = line.split('\t')
        labels.append(label)
        features.append(list(map(float,feature.split())))
le = preprocessing.LabelEncoder()
y = le.fit_transform(labels)
X = features
# Future Warningが出るため，solverを明示的に指定してる
lr = LogisticRegression(solver='lbfgs')
lr.fit(X, y)



        
