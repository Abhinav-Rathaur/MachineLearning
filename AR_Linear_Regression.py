import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coefficient(x, y): 
	# number of observations
	n = np.size(x) 

	# mean of x and y vector 
	mean_x, mean_y = np.mean(x), np.mean(y) 

	# calculating deviation
	SS_xy = np.sum(y*x) - n*mean_y*mean_x 
	SS_xx = np.sum(x*x) - n*mean_x*mean_x 

	# calculating coefficients 
	b1 = SS_xy / SS_xx 
	b0 = mean_y - b1*mean_x 

	return(b0, b1) 

def plot_regression_line(x, y, b): 
	# plotting the actual points
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 

	# predicted line
	y_pred = b[0] + b[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	plt.xlabel('x') 
	plt.ylabel('y') 
	plt.show() 

def main(): 
	# observations
	np.random.seed(0)
	x = np.random.rand(70,1)
	y = 5+9*x+np.random.rand(70,1)

	b = estimate_coefficient(x, y) 


	# plotting regression line 
	plot_regression_line(x, y, b) 

if __name__ == "__main__": 
	main() 
