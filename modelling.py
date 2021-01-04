"""
Created on Tue Oct  1 09:16:03 2019

"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

def spliting_data_and_training_model(path,df):
    df = pd.read_csv(path, index_col=None)
    x=df[['so2','no2']]
    y=df[['Asthma']]
    X_train, X_test, y_train, y_test=train_test_split(x, y, test_size = 0.2, random_state = 0)
    clf = LinearRegression(normalize=True)
    clf.fit(X_train,y_train)
    y_pred_asthama = clf.predict(X_test)
    plt.scatter(y_pred_asthama,y_test)
    #,marker = '^',markerfacecolor = 'yellow',markersize = 7
    plt.show()
    print("Model Accuracy= ",r2_score(y_test,y_pred_asthama)*100,"%")
    return X_test,y_pred_asthama,clf


def visualization(X_test,y_pred_asthama):
    plt.plot(X_test,y_pred_asthama)
    plt.xlabel("Air- pollution")
    plt.ylabel("Asthama")
    plt.title("Asthama-Predection")
    plt.legend()
    plt.show()


