from imports import *
from distribute import distribute

from training import train


pickle_in1 = open("../../Q2_data/Fx_test.pkl", "rb")
pickle_in2 = open("../../Q2_data/X_test.pkl", "rb")
pickle_in3 = open("../../Q2_data/X_train.pkl", "rb")
pickle_in4 = open("../../Q2_data/Y_train.pkl", "rb")

yTest = pickle.load(pickle_in1)
xTest = pickle.load(pickle_in2)

xTrain = pickle.load(pickle_in3)
yTrain = pickle.load(pickle_in4)


bias, variance = train(xTrain, yTrain, xTest, yTest)

plt.plot(bias, color = 'red' , label = 'bias')
plt.plot(variance, color = 'blue', label='variance')
plt.legend()
plt.show()

# # now that we have the bias and the variance ,we can plot this data or whatever  


