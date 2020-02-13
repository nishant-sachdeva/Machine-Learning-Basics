from imports import *


# 	  plt.scatter(xDict, yDict, label='rand', s=1)

#     dx[i] = dx[i][:, np.newaxis]
#     dy[i] = dy[i][:, np.newaxis]

#     poly = PolynomialFeatures(degree=17)
#     x_poly = poly.fit_transform(dx[i])

#     model = LinearRegression()
#     model.fit(x_poly, dy[i])

#     y_poly_pred = model.predict(x_poly)

#     sort_axis = operator.itemgetter(0)
#     sorted_zip = sorted(zip(dx[i],y_poly_pred), key=sort_axis)

#     dx[i], y_poly_pred = zip(*sorted_zip)

#     plt.plot(dx[i], y_poly_pred, color='m')
#     plt.show()





def train(dx, dy , xTest, yTest):
	# now we are gonna train 9 models here on each of those 10 sets that we have
	# so basically we will have a loop and train 10 models for each degree
	# for each model that we get, we will go to the test data and find the predicted values for each x
	# then with the predicted values we will get the avg bias
	for degree in range(1,9):
		# get 10 models for every degree using the 10 test sets
		for i in range(0,9)
			train_x = dx[i]
			train_y = dy[i]

			poly_reg = PolynomialFeatures(degree = degree)
			x_poly = poly_reg.fit_transform(train_x)
			pol_reg = LinearRegression()
			pol_reg.fit(x_poly, y)

			pred_y = pol_reg.predict(poly_reg.fit_transform(X)