from imports import *
from distribute import distribute

from training import train


pickle_in = open("../../Q1_data/data.pkl", "rb")
rawDict = pickle.load(pickle_in)

np.random.shuffle(rawDict)

xDict , yDict = np.hsplit(rawDict, 2)

xTrain, xTest, yTrain, yTest = train_test_split(xDict, yDict, test_size=0.1, random_state=57)

dx , dy , xTest, yTest = distribute(xTrain, yTrain, xTest, yTest)

bias, variance = train(dx, dy, xTest, yTest)


# now that we have the bias and the variance ,we can plot this data or whatever  


