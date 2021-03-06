#!/usr/bin/env python

import rospy, tf

from nav_msgs.msg import OccupancyGrid

import math
import time

def ExpandMap(occupancyGrid):

	lowerResGrid = OccupancyGrid(occupancyGrid.header, occupancyGrid.info, [])

	oldWidth = occupancyGrid.info.width

	lowerResGrid.info.resolution = .1
	lowerResGrid.info.width = int(math.floor(float(occupancyGrid.info.width)/2))
	lowerResGrid.info.height = int(math.floor(float(occupancyGrid.info.height)/2))

	width = lowerResGrid.info.width
	height = lowerResGrid.info.height

	lowerResGrid.data = [-1]*width*height

	for i in range (0, height):
		for j in range (0, width):
			if occupancyGrid.data[(j*2) + (oldWidth * i*2)] >= 1 or \
				occupancyGrid.data[(j*2) + (oldWidth * ((i*2)+1))] >= 1 or \
				occupancyGrid.data[(j*2)+1 + (oldWidth * i*2)] >= 1 or \
				occupancyGrid.data[(j*2)+1 + (oldWidth * ((i*2)+1))] >= 1:
				lowerResGrid.data[j + (width * i)] = 100
			elif occupancyGrid.data[(j*2) + (oldWidth * i*2)] == 0 and \
				occupancyGrid.data[(j*2) + (oldWidth * ((i*2)+1))] == 0 and \
				occupancyGrid.data[(j*2)+1 + (oldWidth * i*2)] == 0 and \
				occupancyGrid.data[(j*2)+1 + (oldWidth * ((i*2)+1))] == 0:
				lowerResGrid.data[j + (width * i)] = 0
			else:
				lowerResGrid.data[j + (width * i)] = -1

	expandedGrid = OccupancyGrid(lowerResGrid.header, lowerResGrid.info, lowerResGrid.data)

	expandedData = list(lowerResGrid.data)

	print "expanding"
	for i in range (0, height):
		for j in range (0, width):
			if (lowerResGrid.data[j + (width * i)] >= 1):
				for k in range (j - 2, j + 3):
					for l in range (i - 2, i + 3):
						if (k > 0 and k < width and l > 0 and l < height):
							expandedData[k + (width * l)] = 100

	expandedGrid.data = tuple(expandedData)
	print "expanded"
	return expandedGrid, lowerResGrid


def MapCallback(occupancy):
	print "ready"
	global mapReady, occupancyGrid
	
	mapReady = 1
	occupancyGrid = occupancy

if __name__ == '__main__':

	global mapReady, occupancyGrid

	rospy.init_node('doop')

	mapReady = 0
	occupancyGrid = None

	rospy.Subscriber('map', OccupancyGrid, MapCallback)
	occPub = rospy.Publisher('expandedMap', OccupancyGrid)
	resPub = rospy.Publisher('resMap', OccupancyGrid)

	time.sleep(1)

	odom_list = tf.TransformListener()

	rospy.sleep(rospy.Duration(1, 0))

	print "gonna wait"
	while not mapReady:
		time.sleep(.3)
		print mapReady

	print "doing the thing"
	expandedGrid, lowerResGrid = ExpandMap(occupancyGrid)
	print "expanded"
	occPub.publish(expandedGrid)
	resPub.publish(lowerResGrid)
	time.sleep(2)

