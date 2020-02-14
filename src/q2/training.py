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
		# print(degree)
		variance_wala_array = [] 
		bias_wala_array = np.zeros((np.shape(xTest)[0], 20))
		for i in range(0, 20):
			# print(dx[i])
			# print(type(dy[i]))
			train_x = dx[i][:, np.newaxis]
			train_y = dy[i]

			test_x = xTest[:, np.newaxis]

			# print(train_x)
			poly = PolynomialFeatures(degree = degree) 
			X_poly = poly.fit_transform(train_x) 
			  
			lin2 = LinearRegression()
			# print(X_poly)
			# print(len(train_y.flatten())) 
			lin2.fit(X_poly, train_y)


			pred_y = lin2.predict(poly.fit_transform(test_x))
			# print(pred_y.shape)
			bias_wala_array[:, i] = pred_y.flatten()
			# temp.append(pred_y)
			# print(type(pred_y))
			# plt.scatter(xTest, pred_y, s=1)
			# plt.scatter(xTest, yTest, s=1)
			# sort_axis = operator.itemgetter(0)
			# sorted_zip = sorted(zip(xTest,pred_y), key=sort_axis)
			# x, y_poly_pred = zip(*sorted_zip)
			# print(x)
			# temp.append(y_poly_pred)

			# plt.plot( color='m')
			# plt.show()
			variance_wala_array.append(pred_y)
			# for i in range(0, len(pred_y)):
				# print(str(xTest[i][1]) + " : " + str(yTest[i]) + " : " + str(pred_y[i]))
		bias = np.sqrt(np.mean(np.square(np.mean(bias_wala_array, axis=1)-yTest)))
		variance = np.mean(np.var(bias_wala_array, axis=1))
		bi.append(bias*10)
		vare.append(float(variance/100))
	return bi, vare




