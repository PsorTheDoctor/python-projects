#!/usr/bin/python

import rospy
import numpy as np
# import sensor_msgs.point_cloud2 as pc2
# import ctypes
import struct
from sensor_msgs.msg import PointCloud2, PointField
# from std_msgs.msg import Header
# import ros_numpy
import icp
from utils import *
	

def pcl_callback(msg):
	i = 0
	x_values = []
	y_values = []
	z_values = []
  
	while i < len(msg.data):
		point = msg.data[i * msg.point_step:(i+1) * msg.point_step]
		
		if len(point) >= 20:
			x = struct.unpack('f', point[0:4])[0]
			y = struct.unpack('f', point[4:8])[0]
			z = struct.unpack('f', point[8:12])[0]
			
			# r = struct.unpack('b', point[16])[0]
			# g = struct.unpack('b', point[17])[0]
			# b = struct.unpack('b', point[18])[0]
			
			x_values.append(x)
			y_values.append(y)
			z_values.append(z)
			
			# print('cp1')
			
		i += msg.point_step
		
	A = np.zeros((len(x_values), 3))
	A[:, 0] = x_values[:]
	A[:, 1] = y_values[:]
	A[:, 2] = z_values[:]
	
	B = generate_B_matrix(A)
	
	plot_both_scatters(A, B)
	
	final_transf, distances, iters = icp.icp(B, A, tolerance=0.000001)
	# print(final_transf)

		
rospy.init_node('rs_pcl')
rospy.Subscriber('/camera/depth/color/points', PointCloud2, pcl_callback)

while not rospy.is_shutdown():
	pass
