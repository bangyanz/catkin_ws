#!/usr/bin/env python

import rospy, tf

import AStar, ObstacleExpansionn, waypoints, waypoint_math

from tf.transformations import euler_from_quaternion

from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from nav_msgs.msg import OccupancyGrid

import time
import math

def MapCallback(occupancy):
	global mapReady, occupancyGrid
	
	mapReady = 1
	occupancyGrid = occupancy

def GoalCallback(goalPoint):
	global goalReady, goal

	goalReady = 1
	goal.x = int(round(goalPoint.pose.position.x))
	goal.y = int(round(goalPoint.pose.position.y))
	goal.z = 0
	print "printing goal"
	print goal

#Odometry Callback function
def OdometryCallback(msg):
	#Current x, y, and theta
	global x, y, theta
	xPos = msg.pose.pose.position.x
	yPos = msg.pose.pose.position.y
	orientation = msg.pose.pose.orientation
	quaternion = [orientation.x, orientation.y, orientation.z, orientation.w]
	roll, pitch, yaw = euler_from_quaternion(quaternion)

	x = xPos
	y = yPos
	theta = yaw

if __name__ == '__main__':

	global mapReady, occupancyGrid, goalReady, goal, x, y, theta

	mapReady = 0
	goalReady = 0

	goal = Point()
	occupancyGrid = None

	rospy.init_node('Lab_4_node')

	rospy.Subscriber('map', OccupancyGrid, MapCallback)
	rospy.Subscriber('odom', Odometry, OdometryCallback) 
	#rospy.Subscriber('map_metadata', MapMetaData, MapMetaCallback)
	rospy.Subscriber('move_base_simple/goal', PoseStamped, GoalCallback)
	#rospy.Subscriber('initialpose', PoseWithCovarianceStamped, InitialPoseCallback)

	odom_list = tf.TransformListener()

	rospy.sleep(rospy.Duration(1, 0))

	print "Starting Lab 4"

	start = Point()
	start.x = 1
	start.y = 1
	start.z = 0

	while not mapReady:
		time.sleep(.3)
		print "please publish map"

	while 1:
		while not goalReady:
			time.sleep(.3)
			print "waiting"

		expandedMap = ObstacleExpansion.ExpandMap(occupancyGrid)
		path = AStar.GetPath(expandedMap, start, goal)
		waypoints = AStar.Waypoints(path)
		turnAngle = waypoint_math.ChooseTurnDirection(waypoints, x, y, theta)
		print turnAngle
		goalReady = 0
		start.x = goal.x
		start.y = goal.y

	print "Lab 4 complete!"
