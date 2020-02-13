
import operator
import random
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

pickle_in = open("Q1_data/data.pkl", "rb")
rawDict = pickle.load(pickle_in)
xDict=[]
yDict=[]
for i in range(0, len(rawDict)):
    xDict.append(rawDict[i][0])
    yDict.append(rawDict[i][1])
# print(rawDict)
# raw = np.load("Q1_data/data.pkl").shape(5000, 2)

xTrain, xTest, yTrain, yTest = train_test_split(xDict, yDict, test_size=0.1, random_state=57)
dx={}
dy={}
numCount={}
for i in range(0, 10):
    dx["xTrain{0}".format(i)] = []
    dy["yTrain{0}".format(i)] = []
    numCount["count{0}".format(i)]=0
j=0
while j<4500:
    arrayVal=random.randint(0, 9)
    if numCount["count{0}".format(arrayVal)]>=450:
        continue
    else:
        dx["xTrain{0}".format(arrayVal)].append(xTrain[j])
        dy["yTrain{0}".format(arrayVal)].append(yTrain[j])
        numCount["count{0}".format(arrayVal)]+=1
        j+=1

for i in range(0, 10):
    print(numCount["count{0}".format(arrayVal)])

        


plt.scatter(xTest, yTest, label='rand', s=1)
plt.show()