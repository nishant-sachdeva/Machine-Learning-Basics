from imports import *
from distribute import distribute


pickle_in = open("../../Q1_data/data.pkl", "rb")
rawDict = pickle.load(pickle_in)

random.shuffle(rawDict)

xDict , yDict = np.hsplit(rawDict, 2)

xTrain, xTest, yTrain, yTest = train_test_split(xDict, yDict, test_size=0.1, random_state=20)
        
dx , dy = distribute(xTrain, yTrain)

plt.scatter(xDict, yDict, label='rand', s=1)

plt.show()


