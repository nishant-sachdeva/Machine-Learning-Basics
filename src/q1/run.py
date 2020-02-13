from imports import *
from distribute import distribute


pickle_in = open("../../Q1_data/data.pkl", "rb")
rawDict = pickle.load(pickle_in)

random.shuffle(rawDict)

xDict , yDict = np.hsplit(rawDict, 2)

xTrain, xTest, yTrain, yTest = train_test_split(xDict, yDict, test_size=0.1, random_state=20)

dx , dy = distribute(xTrain, yTrain)
train_x = dx[5]
train_y = dy[5]

poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(train_x)
pol_reg = LinearRegression()
pol_reg.fit(x_poly, train_y)

pred_y = pol_reg.predict(poly_reg.fit_transform(xTest))
plt.plot(xTest, pred_y)
plt.scatter(xDict, yDict, label='rand', s=1)
plt.show()


