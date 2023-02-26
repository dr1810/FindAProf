import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def name(nm):
    pth = paths[paths["Name "]==nm]
    return list(pth["Path"])[0]
def predict(file,las):
    def logi(file,las):
        dataset= pd.read_csv(file)
        dataset=dataset.dropna()
        x = dataset["learning adaptability"]
        pred_assign = dataset["assignment"]
        log = LogisticRegression()
        log.fit(x,pred_assign)
        pred_assign = log.predict(las)
        x = np.array(dataset["learning adaptability"]).reshape(-1,1)
        pred_mid = np.array(dataset["mid term assessment"]).reshape(-1,1)
        log = LogisticRegression()
        log.fit(x,pred_mid)
        pred_mida = log.predict(las)
        x = np.array(dataset["learning adaptability"]).reshape(-1,1)
        pred_final = np.array(dataset["final assessment"]).reshape(-1,1)
        log = LogisticRegression()
        log.fit(x,pred_final)
        pred_fina = log.predict(las)
        return [pred_assign,pred_mid,pre_fina]
    def deci(file,las):
        dataset= pd.read_csv(file)
        dataset=dataset.dropna()
        x = dataset["learning adaptability"]
        pred_assign = dataset["assignment"]
        log = DecisionTreeClassifier()
        log.fit(x,pred_assign)
        pred_assign = log.predict(las)
        x = np.array(dataset["learning adaptability"]).reshape(-1,1)
        pred_mid = np.array(dataset["mid term assessment"]).reshape(-1,1)
        log = DecisionTreeClassifier()
        log.fit(x,pred_mid)
        pred_mida = log.predict(las)
        x = np.array(dataset["learning adaptability"]).reshape(-1,1)
        pred_final = np.array(dataset["final assessment"]).reshape(-1,1)
        log = DecisionTreeClassifier()
        log.fit(x,pred_final)
        pred_fina = log.predict(las)
        return [pred_assign,pred_mid,pre_fina]
    dataset= pd.read_csv(file)
    dataset=dataset.dropna()
    x = dataset.iloc[:, [3, 4]].values
    # output
    y = dataset.iloc[:, 6].values
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
    sc_x = StandardScaler()
    xtrain = sc_x.fit_transform(X_train)
    xtest = sc_x.transform(X_test)
    classifier = LogisticRegression(random_state = 0)
    decision = DecisionTreeClassifier(random_state = 0)
    classifier.fit(xtrain, y_train)
    decision.fit(xtrain, y_train)
    y_pred_logistic = classifier.predict(xtest)
    y_pred_decision = decision.predict(xtest)
    accuracy_dec = accuracy_score(y_test, y_pred_decision)
    accuracy_logis = accuracy_score(y_test, y_pred_decision)
    accuracy = {"dec":accuracy_dec,"log":accuracy_logis}
    if max(accuracy.keys()) == 'logi':
        return logi(file,las)
    if max(accuracy.keys()) == 'dec':
        return deci(file,las)