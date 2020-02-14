from imports import *
from distribute import distribute

from training import train


pickle_in = open("../../Q1_data/data.pkl", "rb")
rawDict = pickle.load(pickle_in)


xDict , yDict = np.hsplit(rawDict, 2)

xTrain, xTest, yTrain, yTest = train_test_split(xDict, yDict, test_size=0.1, random_state=57)
temp=np.concatenate((xTrain, yTrain), axis =1)
np.random.shuffle(temp)
xTrain, yTrain = np.hsplit(temp, 2)

print(type(xTest), type(yTest))

dx , dy= distribute(xTrain, yTrain)

bias, variance = train(dx, dy, xTest, yTest)
plt.plot(bias, color = 'red')
plt.plot(variance, color = 'blue')
plt.show()

# now that we have the bias and the variance ,we can plot this data or whatever  


