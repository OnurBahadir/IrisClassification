from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

x = np.loadtxt("data/iris.txt", delimiter=',', usecols=(0, 1, 2, 3))
y = np.loadtxt("data/iris.txt", delimiter=',', usecols=(4,))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = LinearSVC(random_state=0, tol=1e-5, max_iter=10000)
clf.fit(x_train, y_train)

Y = clf.predict(x_test)

score = clf.score(x_test, y_test)

joblib.dump(clf, "irisLinearSVC.sav")
