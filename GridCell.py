#!/usr/bin/env python

import rospy, tf, time
from geometry_msgs.msg import Point

from nav_msgs.msg import GridCells

def PublishSingleCell():
	global gridCell
	cellPoint= [Point(-15.4, -13.8, 0)] 
	
	cellPublisher = rospy.Publisher('cell', GridCells)

	gridCell = GridCells()
	gridCell.cell_width = 1
	gridCell.cell_height = 1
	gridCell.cells = cellPoint
	gridCell.header.frame_id = 'map'

	cellPublisher.publish(gridCell)	

	return gridCell

if __name__ == '__main__':

	rospy.init_node('Lab_4_node')
	global gridCell

	while 1:
		PublishSingleCell()
		time.sleep(.5)
