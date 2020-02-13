from imports import *
import time

def train(dx, dy , xTest, yTest):
	# now we are having the data for the entire training :\
	# now we will look to calculate the bias and variance for this thing( smhw I really hope )



	bias = []
	variance = []
	for degree in range(1,10):
		print(degree)
		variance_wala_array = [] 
		bias_wala_array = []
		for i in range(0,10):
			train_x = dx[i]
			train_y = dy[i]

			poly = PolynomialFeatures(degree = degree) 
			X_poly = poly.fit_transform(train_x) 
			  
			lin2 = LinearRegression() 
			lin2.fit(X_poly, train_y)


			pred_y = lin2.predict(poly.fit_transform(xTest) )

			variance_wala_array.append(pred_y)
			# for i in range(0, len(pred_y)):
				# print(str(xTest[i][1]) + " : " + str(yTest[i]) + " : " + str(pred_y[i]))

	return bias, variance