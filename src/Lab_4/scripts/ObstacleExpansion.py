#!/usr/bin/env python

import rospy, tf

from nav_msgs.msg import OccupancyGrid

import time

def ExpandMap(occupancyGrid):

	width = occupancyGrid.info.width
	height = occupancyGrid.info.height

	lowerResGrid = OccupancyGrid(occupancyGrid.header, occupancyGrid.info, [])

	lowerResGrid.info.resolution = .1
	lowerResGrid.info.width = int(math.ceil(width/2))
	lowerResGrid.info.height = int(math.ceil(height/2))

	lowerResGrid.data = []

	for i in range (0, int(math.ceil(height/2))):
		for j in range (0, int(math.ceil(width/2))):
			if occupancyGrid.data[(j*2) + (width * i*2)] >= 1 or \
				occupancyGrid.data[(j*2) + (width * ((i*2)+1)] >= 1 or \
				occupancyGrid.data[(j*2)+1 + (width * i*2)] >= 1 or \
				occupancyGrid.data[(j*2)+1 + (width * ((i*2)+1)] >= 1:
				lowerResGrid.data[j + (width * i)] = 100

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

	odom_list = tf.TransformListener()

	rospy.sleep(rospy.Duration(1, 0))

	print "gonna wait"
	while not mapReady:
		time.sleep(.3)
		print mapReady

	print "did the thing"
	print type(occupancyGrid.data)
	expandedGrid = ExpandMap(occupancyGrid)
	occPub.publish(expandedGrid)
	time.sleep(2)

