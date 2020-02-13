from imports import *
from distribute import distribute


pickle_in = open("../../Q1_data/data.pkl", "rb")
rawDict = pickle.load(pickle_in)

random.shuffle(rawDict)

xDict , yDict = np.hsplit(rawDict, 2)

xTrain, xTest, yTrain, yTest = train_test_split(xDict, yDict, test_size=0.1, random_state=20)

dx , dy = distribute(xTrain, yTrain)

for i in range(0, 10):
    plt.scatter(xDict, yDict, label='rand', s=1)
    dx[i] = dx[i][:, np.newaxis]
    dy[i] = dy[i][:, np.newaxis]
    poly = PolynomialFeatures(degree=17)
    x_poly = poly.fit_transform(dx[i])
    model = LinearRegression()
    model.fit(x_poly, dy[i])
    y_poly_pred = model.predict(x_poly)
    sort_axis = operator.itemgetter(0)
    sorted_zip = sorted(zip(dx[i],y_poly_pred), key=sort_axis)
    dx[i], y_poly_pred = zip(*sorted_zip)
    plt.plot(dx[i], y_poly_pred, color='m')
    plt.show()
    # plt.plot(dx[i], y_poly_pred)
    # plt.show()
# bias, variance = train(dx , dy, xTest, yTest)

plt.scatter(xDict, yDict, label='rand', s=1)
plt.show()


