import numpy as np

def mean_squared_error(y_true, y_predicted):
	cost = np.sum((y_true-y_predicted)**2) / len(y_true)
	return cost

def gradient_descent(x, y, iterations = 1000, learning_rate = 0.0001,
					stopping_threshold = 1e-6):
	current_weight = 0.1
	current_bias = 0.01
	iterations = iterations
	learning_rate = learning_rate
	n = float(len(x))
	
	costs = []
	weights = []
	previous_cost = None
	for i in range(iterations):
		y_predicted = (current_weight * x) + current_bias
		current_cost = mean_squared_error(y, y_predicted)
		if previous_cost and abs(previous_cost-current_cost)<=stopping_threshold:
			break
		
		previous_cost = current_cost

		costs.append(current_cost)
		weights.append(current_weight)
		weight_derivative = -(2/n) * sum(x * (y-y_predicted))
		bias_derivative = -(2/n) * sum(y-y_predicted)
		current_weight = current_weight - (learning_rate * weight_derivative)
		current_bias = current_bias - (learning_rate * bias_derivative)
		print(f"Iteration {i+1}: Cost {current_cost}, Weight \
		{current_weight}, Bias {current_bias}")
	return current_weight, current_bias


def main():
	X = np.array([32.5, 53.4, 61.5, 47.4, 59.8,
		55.1, 52.2, 39.2, 48.1, 52.5,
		45.4, 54.3, 44.1, 58.1, 56.7,
		])
	Y = np.array([31.70700585, 68.77759598, 62.5623823 , 71.54663223, 87.23092513,
		78.21151827, 79.64197305, 59.17148932, 75.3312423 , 71.30087989,
		55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,
		])
	estimated_weight, estimated_bias = gradient_descent(X, Y, iterations=100)
	print(f"Estimated Weight: {estimated_weight}\nEstimated Bias: {estimated_bias}")
	Y_pred = estimated_weight*X + estimated_bias



	
if __name__=="__main__":
	main()
