#!/usr/bin/env python

import rospy, tf

from nav_msgs.msg import OccupancyGrid

import time

def ExpandMap(occupancyGrid):

	width = occupancyGrid.info.width
	height = occupancyGrid.info.height

	expandedGrid = OccupancyGrid(occupancyGrid.header, occupancyGrid.info, occupancyGrid.data)

	expandedData = list(expandedGrid.data)

	for i in range (0, width):
		for j in range (0, height):
			if (occupancyGrid.data[i + (height * j)] >= 1):
				for k in range (i - 2, i + 3):
					for l in range (j - 2, j + 3):
						if (k > 0 and k < width and l > 0 and l < height):
							expandedData[k + (height * l)] = 100

	expandedGrid.data = tuple(expandedData)
	return expandedGrid


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

