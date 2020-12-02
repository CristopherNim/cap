import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
data = pd.read_csv("mushroom1-0.csv")

data = data.sample(frac=1)


X = data.drop(['class'], axis=1)

y = data["class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)
clf.score(X_test, y_test)
print(clf.predict([[1, 0, 0, 1, 0]]))



pickle.dump(clf, open("mush.pkl", "wb"))
model = pickle.load(open('mush.pkl', 'rb'))
