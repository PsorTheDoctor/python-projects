import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

dim = 3
transl_noise = 0.00001
rot_noise = 0.00001
noise_sigma = 0.01


def plot_scatter(voxels):
	fig = plt.figure()
	ax = Axes3D(fig)
	
	x_values = voxels[:, 0]
	y_values = voxels[:, 1]
	z_values = voxels[:, 2]
	
	ax.scatter(x_values, y_values, z_values)
	plt.show()
	

def plot_both_scatters(A, B):
	fig = plt.figure()
	ax = Axes3D(fig)

	x_A = A[:, 0]
	y_A = A[:, 1]
	z_A = A[:, 2]
	x_B = B[:, 0]
	y_B = B[:, 1]
	z_B = B[:, 2]
	
	ax.scatter(x_A, y_A, z_A, c='b')
	ax.scatter(x_B, y_B, z_B, c='r')
	plt.show()
	
	
def randomize_cuboid(a, b, h):
	num_of_points = 1000
	points = []
	
	for n in range(num_of_points):
		wall = random.randint(1, 6)
		
		if wall == 1:
			x = random.random() * a
			y = random.random() * h
			points.append([x, y, 0])
			
		elif wall == 2:
			x = random.random() * a
			y = random.random() * h
			points.append([x, y, b])
			
		elif wall == 3:
			x = random.random() * a
			z = random.random() * b
			points.append([x, 0, z])
			
		elif wall == 4:
			x = random.random() * a
			z = random.random() * b
			points.append([x, h, z])
			
		elif wall == 5:
			y = random.random() * h
			z = random.random() * b
			points.append([0, y, z])
			
		else:
			y = random.random() * h
			z = random.random() * b
			points.append([a, y, z])
	
	cuboid = np.asarray(points)
	return cuboid
	

def rotation_matrix(axis, theta):
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.)
    b, c, d = -axis * np.sin(theta / 2.)

    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])


def generate_B_matrix(A):
	B = np.copy(A)
	B += np.random.rand(A.shape[0], A.shape[1]) * transl_noise
	R = rotation_matrix(np.random.rand(dim), np.random.rand() * rot_noise)
	B = np.dot(R, B.T).T
	
	B += np.random.randn(B.shape[0], B.shape[1]) * noise_sigma
	return B

cuboid = randomize_cuboid(100, 100, 100)
plot_scatter(cuboid)
