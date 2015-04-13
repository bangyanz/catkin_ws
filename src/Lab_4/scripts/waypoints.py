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

def Waypoints (pointList):

	print "waypoints!"

	waypointpub = rospy.Publisher('waypoints', GridCells)
	WaypointCells = [Point()]

	i = 0
	current_state = 2

	WaypointCells.append(pointList[0])

	for item in pointList:
		current_point = item
		if (i < len(pointList)-1):
			next_point = pointList[i+1]
			i += 1

			#if the x coordinate is changing and the y coordinate is staying the same
			if ((not(next_point.x - current_point.x == 0)) and (next_point.y - current_point.y == 0)):
				if (current_state == 1):
					WaypointCells.append(current_point)
					publishableWaypoints = MakeGridCellsFromList(WaypointCells)
					waypointpub.publish(publishableWaypoints)
					time.sleep(.2)

				current_state = 0	
				
			#if the x coordinate is staying the same and the y coordinate is changing
			elif ((next_point.x - current_point.x == 0) and (not(next_point.y - current_point.y == 0))):
				if (current_state == 0):
					WaypointCells.append(current_point)
					publishableWaypoints = MakeGridCellsFromList(WaypointCells)
					waypointpub.publish(publishableWaypoints)
					time.sleep(.2)
				current_state = 1


				
			else:
				print "something is broken"
				print current_point
				print next_point

	WaypointCells.append(pointList[len(pointList)-1])

	print WaypointCells

	return WaypointCells


# if __name__ == '__main__':
# 	rospy.init_node('megagnon_Lab_3_Waypoint_node')

# 	rospy.Subscriber('path', GridCells, Waypoints)

# 	test = [(0,0), (0,1), (0,2), (1,2), (1,3)]

# 	print "starting Waypoints"
# 	Waypoints(test)
# 	print "end Waypoints"

