import numpy as np
from utils import *
import icp

cam_height = 0.5

base_x = 0.8
base_y = 0.5

cam = np.array([[1, 0, 0, 0],
				[0,-1, 0, 0],
				[0, 0,-1, cam_height],
				[0, 0, 0, 1]])

base = np.array([[1, 0, 0, base_x],
				 [0, 1, 0, base_y],
				 [0, 0, 1, 0],
				 [0, 0, 0, 1]])

obj = np.load('snapshots/preprocessed.npy')

model = randomize_cuboid(0.045, 0.045, 0.045, density=obj.shape[0])

print(model.shape)
print(obj.shape)
print(obj.min())
print(obj.max())

transf, distances, _ = icp.icp(model, obj)
print(transf)

ones = np.ones((model.shape[0], 1))
model = np.c_[model, ones]

fitted_model = np.dot(model, transf.T)

plot_both_scatters(obj, fitted_model)
