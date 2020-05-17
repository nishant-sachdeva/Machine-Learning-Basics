from imports import *
import time

def train(dx, dy , xTest, yTest):
	# now we are having the data for the entire training :\
	# now we will look to calculate the bias and variance for this thing( smhw I really hope )
	# print(str(type(xTest))+"is" )

	temp = []
	bi = []
	vare = []
	for degree in range(1,10):
		variance_wala_array = [] 
		bias_wala_array = np.zeros((np.shape(xTest)[0], 20))
		for i in range(0, 20):
			train_x = dx[i][:, np.newaxis]
			train_y = dy[i]
			test_x = xTest[:, np.newaxis]
			poly = PolynomialFeatures(degree = degree) 
			X_poly = poly.fit_transform(train_x) 
			lin2 = LinearRegression()
			lin2.fit(X_poly, train_y)
			pred_y = lin2.predict(poly.fit_transform(test_x))
			bias_wala_array[:, i] = pred_y.flatten()
			variance_wala_array.append(pred_y)
		bias = np.sqrt(np.mean(np.square(np.mean(bias_wala_array, axis=1)-yTest)))
		variance = np.mean(np.var(bias_wala_array, axis=1))
		bi.append(bias*10)
		vare.append(float(variance/100))
	return bi, vare




