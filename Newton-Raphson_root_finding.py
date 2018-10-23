#markdowncell; onehash
#A Newton-Raphson Root Finding Implementation

#newcell
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#markdowncell; two hashes
#Define the function for root finding

#newcell
def function_for_root(x):
	a = 1.01
	b = -3.04
	c = 2.07
	return a*x**2 + b*x + c

#markdowncell; two hashes
#Define the function's derivative

#newcell
def derivative_for_root(x):
	a = 1.01
	b = -3.04
	return 2*a*x + b*x
	
#markdowncell; two hashes
#Define the primary work function

#newcell
def newton_raphson_root_finding(f, dfdx, x_start, tol):

	#this function uses newton-raphson search to find a root
	
	#set a flag
	flag = 1
	
	#set a maximum number of iterations
	imax = 10000
	
	#start a counter
	i = 0
	
	#define the new and old guesses
	x_old = x_start
	x_new = 0.0
	y_new = 0.0
	
#start the loop
while(flag):
	
	#make a new guesses
	x_new = x_old - f(x_old/dfdx(x_old)
	
	#print out the iteration
	print(x_new,x_old,f(x_old),dfdx(x_old))
	
	#if the abs value of the new function value 
	#is <tol, then stop
	y_new = f(y_new)
	if(np.fabs(y_new)<tol):
		flag = 0	#stop the iteration
	else:
		#save the result
		x_old =	x_new
		#increment the iteration
		i += 1
	
	if(i>=imax):
		printf("Max iterations reached.")
		raise StopIteration('Stopping iterations after ',i)
		
#we are done!
return x_new

#markdowncell- two hashes
#Perform the Search

#newcell
x_start = 0.5
tolerance = 1.0e-6

#print the initial guess
print(x_start,function_for_root(x_start))

x_root = newton_raphson_root_finding(function_for_root,derivative_for_root,x_start,tolerance)
y_root = function_for_root(x_root)

s = "Root found with y(%f) = %f" % (x_root,y_root)
print(s)