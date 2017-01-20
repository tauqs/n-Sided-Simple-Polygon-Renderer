#################################################
##  Computational Geometry Assignment: Implement the algorithm for generating and drawing 
##  (using GUI) of a simple polygon after taking number (n) of points from user and generating n 
##  random (but distinct) points in 2D space.
## 
##  Authors: 
##  (1) Tauqueer Ahmad  (13114066)
##  (2) Prakhar Pandey  (13114037)
## 
#################################################

import matplotlib.pyplot as plt
import numpy as np 

def draw_polygon(points):
	## Unzip list of points into list of X-coordinates and Y-coordinates repectively
	X,Y = zip(*points)

	## plot all the points
	plt.scatter(X,Y)

	## label X and Y axes
	plt.xlabel('x')
	plt.ylabel('y')

	## Calculate centroid of all the points
	mean_x = np.sum(X)/len(X)
	mean_y = np.sum(Y)/len(Y)

	#plt.plot(mean_x,mean_y,'o',color='r')

	points_ = []

	##  loop to calculate tan_theta values and quadrent of all the points w.r.t centroid as origin
	for i,(x,y) in enumerate(points):
		x_ = x - mean_x
		y_ = y - mean_y
		tan_theta = (y_/float(x_))

		quad  = 1

		if x_<0 and y_<0:
			quad = 3
		elif x_<0:
			quad = 2
		elif y_<0:
			quad = 4
		points_.append((quad,tan_theta,i))

	## sort points w.r.t to angle
	points_ = sorted(points_, key = lambda x: (x[0], x[1]))
	points_ = np.array(points_)

	## draw lines between consecutive pair of points
	for j,(_,_,i) in enumerate(points_):
		x_1,y_1 = points[int(i)]
		x_2,y_2 = x_1,y_1
		if j == len(points)-1:
			x_2,y_2 = points[int(points_[0][2])]	
		else:
			x_2,y_2 = points[int(points_[j+1][2])]
		plt.plot([x_1,x_2], [y_1, y_2], 'k-', lw=1)

	## Show the resulting polygon
	plt.show()


## Take number of points in polygon as an input from user
n = int(input("Enter number of points in polygon: "))

## Generate n distinct random points 
X = np.random.choice(range(n*2), n, replace=False)
Y = np.random.choice(range(n*2), n, replace=False)

## zip list of X-coordinates and list of Y-coordinates
points = zip(X,Y)

## Draw the polygon
draw_polygon(points)

