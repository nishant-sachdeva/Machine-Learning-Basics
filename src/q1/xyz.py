import pickle
import time
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from tabulate import tabulate
from matplotlib import pyplot as plt
with open('../../Q1_data/data.pkl', 'rb') as f:
    data = pickle.load(f)
data = data.T

X_train, X_test, Y_train, Y_test = train_test_split(
    data[0], data[1], test_size=0.1)

X_DataTrain = []
Y_DataTrain = []
for i in range(9):
    X_train, X_try, Y_train, Y_try = train_test_split(
        X_train, Y_train, test_size=450)
    X_DataTrain.append(X_try)
    Y_DataTrain.append(Y_try)
X_DataTrain.append(X_train)
Y_DataTrain.append(Y_train)

Result = []
Varian = []
for i in range(1, 10):
    Temp = []
    temper = []
    BiasArray = np.zeros((np.shape(X_test)[0],10))
    
    for j in range(10):

        X_DataTrain[j] = X_DataTrain[j].reshape(1, -1)
        Y_DataTrain[j] = Y_DataTrain[j].reshape(1, -1)
        poly = PolynomialFeatures(i)
        trial = poly.fit_transform(X_DataTrain[j].reshape(-1, 1))
        reg = LinearRegression().fit(trial, Y_DataTrain[j].flatten())
        aver = 0
        tri = poly.fit_transform(X_test.reshape(-1,1))
        average = reg.predict(tri)
        plt.plot(X_test, average)
        plt.show()
        BiasArray[:,j] = average
    Bias = np.mean(np.abs(np.mean(BiasArray,axis = 1) - Y_test))
    Variance = np.mean(np.var(BiasArray, axis=1))
    Varian.append(Variance)
    Result.append(Bias)
array = np.vstack((Varian,Result)).T
table = tabulate(array,headers=["Variance","Bias"],tablefmt="fancy_grid")

print(table)