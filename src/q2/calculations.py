# we need to calculate bias in this file

from imports import *

def calculate_bias(mean_array, yTest):
	
	return np.mean ( np.absolute (np.subtract(mean_array ,yTest) ) )



def calculate_variance(mean_array, yTest):
	return np.mean ( np.square ( np.absolute (np.subtract(mean_array ,yTest) ) ) )

	# here we will calculate variance for the model that we got



def calculate_bias_and_variance(predictions , yTest):
	# so we now have this whole predictions wala array
	bias = 0
	variance = 0

	mean_array = np.zeros(len(yTest)) 

	for predicted_set in predictions:
		mean_array = np.add(mean_array , predicted_set)
	
	mean_array = np.divide(mean_array , len(predictions))

	bias = calculate_bias(mean_array, yTest)
	variance = calculate_variance(mean_array, yTest)

	return bias, variance