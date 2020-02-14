from imports import *
import time

from calculations import calculate_bias_and_variance

def train(dx, dy , xTest, yTest):
	# now we are having the data for the entire training :\
	# now we will look to calculate the bias and variance for this thing( smhw I really hope )
	# print(str(type(xTest))+"is" )

	temp = []
	bi = []
	vare = []
	for degree in range(1,100):
		variance_wala_array = [] 
		bias_wala_array = np.zeros((np.shape(xTest)[0], 10))
		for i in range(0, 10):
			train_x = dx[i][:, np.newaxis]
			train_y = dy[i][:, np.newaxis]
			poly = PolynomialFeatures(degree = degree) 
			X_poly = poly.fit_transform(train_x) 
			lin2 = LinearRegression()
			lin2.fit(X_poly, train_y)
			pred_y = lin2.predict(poly.fit_transform(xTest))
			bias_wala_array[:, i] = pred_y.flatten()
			variance_wala_array.append(pred_y)
		bias, variance = calculate_bias_and_variance(bias_wala_array, yTest)
		bi.append(bias)
		vare.append(variance)
	return bi, vare




