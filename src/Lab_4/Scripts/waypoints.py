import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import GridCells
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point

import AStar

import time

def MakeGridCellsFromList (cellList):
	gridCells = GridCells()
	gridCells.cell_width = 1
	gridCells.cell_height = 1
	gridCells.cells = cellList
	gridCells.header.frame_id = 'map'
	return gridCells

def Waypoints (pointlist):

	print "waypoints!"

	waypointpub = rospy.Publisher('waypoints', GridCells)
	WaypointCells = [Point()]

	i = 0
	PointList = pointlist
	print PointList
	current_state = 0

	for item in PointList:
		current_x = item[0]
		current_y = item[1]
		print "current x", current_x
		print "current y", current_y
		if (i < len(PointList)-1):
			next_point = PointList[i+1]
			next_x = next_point[0]
			next_y = next_point[1]
			print "next x", next_x
			print "next Y", next_y
			i += 1


		
		#if the x coordinate is changing and the y coordinate is staying the same
		if ((not(next_x - current_x == 0)) and (next_y - current_y == 0)):
			print "I hope I'm going left/right"
			if (current_state == 1):
				WaypointCells.append(Point(current_x, current_y, 0))
				print "publish"
				publishableWaypoints = MakeGridCellsFromList(WaypointCells)
				waypointpub.publish(publishableWaypoints)
				time.sleep(.2)

				current_state = 0	
			
		#if the x coordinate is staying the same and the y coordinate is changing
		elif ((next_x - current_x == 0) and (not(next_y - current_y == 0))):
			print "I hope I'm going up/down"
			if (current_state == 0):
				WaypointCells.append(Point(current_x, current_y, 0))
				print "publish2"
				publishableWaypoints = MakeGridCellsFromList(WaypointCells)
				waypointpub.publish(publishableWaypoints)
				time.sleep(.2)
				current_state = 1


			
		elif ((not(next_x - current_x == 0)) and (not(next_y - current_y))):
			print "something is broken"


if __name__ == '__main__':
	rospy.init_node('megagnon_Lab_3_Waypoint_node')

	rospy.Subscriber('path', GridCells, Waypoints)

	test = [(0,0), (0,1), (0,2), (1,2), (1,3)]

	print "starting Waypoints"
	Waypoints(test)
	print "end Waypoints"

