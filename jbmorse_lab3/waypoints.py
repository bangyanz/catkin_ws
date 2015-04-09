import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import GridCells
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point

import AStar

def Waypoints (path):

	waypointpub = rospy.Publisher('Waypoint_Cells', GridCells)
	WaypointCells = GridCells()
	WaypointCells.cell_width = 1
	WaypointCells.cell_height = 1
	WaypointCells.cells = [Point()]
	WaypointCells.header.frame_id = 'map'

	i = 0
	poseList = path.PoseStamped
	print poseList
	#poseList = poses.pose
	#pose = poseList.pop(i)

	#for item in PoseList:
	#	current_x = item.pose.position.x
	#	current_y = item.pose.position.y
	#	next_pose = poseLise.pop(i+1)
	#	next_x = next_pose.pose.position.x
	#	next_y = next_pose.pose.position.y

	#	if (next_x - current_x != 0):
	#		WaypointCells.cells[0].x = current_x
	#		WaypointCells.cells[0].y = current_y
	#		WaypointCells.cells[0].z = 0
	#		gridPub.publish(WaypointCells)
	#		i += 1
	#	elif (next_y - current_y != 0):
	#		WaypointCells.cells[0].x = current_x
	#		WaypointCells.cells[0].y = current_y
	#		WaypointCells.cells[0].z = 0
	#		gridPub.publish(WaypointCells)
	#		i += 1


if __name__ == '__main__':
	rospy.init_node('megagnon_Lab_3_Waypoint_node')

	rospy.Subscriber('path', GridCells, Waypoints)
	print "starting Waypoints"
	Waypoints(AStar)
	print "end Waypoints"

