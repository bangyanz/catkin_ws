#!/usr/bin/env python

import rospy, tf

import AStar, ObstacleExpansion, waypoint_math

from tf.transformations import euler_from_quaternion

from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from nav_msgs.msg import GridCells
from nav_msgs.msg import OccupancyGrid

import time
import math

def MapCallback(occupancy):
	global mapReady, occupancyGrid, stop
	print "I need a map"

	#matt wuz here
	# need to get the map's origin and resolution
	mapOrigin = occupancy.info.origin.position
	gridResolution = occupancy.info.resolution
	gridOrigin = Point(mapOrigin.x + gridResolution/2 , mapOrigin.y + gridResolution/2 , 0)
	
	mapReady = 1
	#stop = 1
	occupancyGrid = occupancy

def GoalCallback(goalPoint):
	global goalReady, goal

	goalReady = 1
	goal.x = goalPoint.pose.position.x
	goal.y = goalPoint.pose.position.y
	goal.z = 0
	print "printing goal"
	print goal

#Odometry Callback function

def TimerCallback(event):
	global x, y, theta
	

	try:
		(trans,orientation) = odom_list.lookupTransform('map', 'base_footprint', rospy.Time(0))
		quaternion = [orientation[0], orientation[1], orientation[2], orientation[3]]
		roll, pitch, yaw = euler_from_quaternion(quaternion)
		x = trans[0]
		y = trans[1]
		theta = yaw
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		pass

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

def PublishTwist(linearVelocity, angularVelocity):

	twist = Twist()
	twist.linear.x = linearVelocity
	twist.linear.y = 0
	twist.linear.z = 0
	twist.angular.x = 0
	twist.angular.y = 0
	twist.angular.z = angularVelocity

	twistPublisher.publish(twist)

#Drive straight function
def DriveStraight(speed, distance):

	global x, y, stop
	tol = .1

	xGoal = x + distance * math.cos(theta)
	yGoal = y + distance * math.sin(theta)

	startx = x
	starty = y
	localx = 0
	localy = 0
	xdistance = distance * math.cos(theta)
	ydistance = distance * math.sin(theta)

	while ((x < xGoal - tol or x > xGoal + tol) or (y < yGoal - tol or y > yGoal + tol) or (stop == 1)):
		PublishTwist(speed, 0)
		time.sleep(.1)
		localx = x - startx
		localy = y - starty
		#if (abs(localx) >= xdistance*3 or abs(localy) >= ydistance*3):
			#break

	print "Drove straight"
	PublishTwist(0, 0)

	#BlindMethod
	#SpinWheels(speed, speed, distance / speed)


def Rotate(angleOfRotation):

	global theta

	tol = math.pi / 36

	closertol = math.pi / 256
	
	angleGoal = (theta + angleOfRotation) 

	if (angleGoal > math.pi):
		angleGoal -= (math.pi * 2)
	elif (angleGoal < (-1 * math.pi)):
		angleGoal += (math.pi * 2)

	while (theta < angleGoal - tol or theta > angleGoal + tol):
		if (angleOfRotation < 0):
			PublishTwist(0, math.pi / -4)
		else:
			PublishTwist(0, math.pi / 4)

		time.sleep(.1)

		#print "I am at", theta
		#print "goalRotate", angleGoal

	while (theta < angleGoal - closertol or theta > angleGoal + closertol):
		if (angleOfRotation < 0):
			PublishTwist(0, math.pi / -12)
			if (theta < angleGoal + closertol):
				break
		else:
			PublishTwist(0, math.pi / 12)
			if (theta > angleGoal - closertol):
				break

		time.sleep(.05)
		#print "I am at", theta
		#print "goalRotate precision", angleGoal 

	print "Rotated"
	PublishTwist(0, 0)

def RotateExplore():
	#rotate 45 degrees
	#wait
	#repeat like 16 times
	i = 0
	while i < 16:
		Rotate(math.pi/4)
		time.sleep(.5)
		i += 1

def ExplorationThing(expandedMap, x, y):
	#receive map and current position
	#decide where closest AStarable location is
	#if not AStarable, put in time out
	#pass to do the things
	explorationStart = Point(x, y, 0)


def DoTheThings(exploreGoal):
	#receive a goal (from exploration thing/AStar confirmed)
	#publish the goal
	explorePublisher = rospy.Publisher("/move_base_simple/goal", Point)

	explorePublisher(exploreGoal)





if __name__ == '__main__':

	global mapReady, occupancyGrid, goalReady, goal, x, y, theta, twistPublisher, wheelRadius, robotRadius, odom_list, bumper, stop

	# mat wuz here
	global mapOrigin, gridResolution, gridOrigin
	#	

	print "starting"

	rospy.init_node('Lab_4_node')

	mapReady = 0
	goalReady = 0
	stop = 0
	goal = Point()
	occupancyGrid = None

	wheelRadius = .0381
	robotRadius = .2286
	bumper = 0

	rospy.Subscriber('map', OccupancyGrid, MapCallback)
	#rospy.Subscriber('odom', Odometry, OdometryCallback) 
	#rospy.Subscriber('map_metadata', MapMetaData, MapMetaCallback)
	rospy.Subscriber('move_base_simple/goal2', PoseStamped, GoalCallback)
	#rospy.Subscriber('initialpose', PoseWithCovarianceStamped, InitialPoseCallback)
	twistPublisher = rospy.Publisher('cmd_vel_mux/input/teleop', Twist) 
	expPub = rospy.Publisher('expandedMap', OccupancyGrid)
	resPub = rospy.Publisher('lowerResMap', OccupancyGrid)

	odom_list = tf.TransformListener()

	rospy.Timer(rospy.Duration(.01), TimerCallback)

	rospy.sleep(1)

	print "Starting Lab 4"

	start = Point()
	start.z = 0
	newPointList = []

	while not mapReady:
		time.sleep(.3)
		print "please publish map"

	while 1:
		while not goalReady:
			time.sleep(.3)
			print "waiting"

		goalReady = 0
		expandedMap, lowerResMap = ObstacleExpansion.ExpandMap(occupancyGrid)
		resPub.publish(lowerResMap)
		expPub.publish(expandedMap)
		start.x = x
		start.y = y
		print "start", x, y
		print "goal", goal.x, goal.y
		stop = 0
		try:
			path = AStar.GetPath(expandedMap, start, goal)
			waypoints = AStar.Waypoints(path)
			for i in range (1, len(waypoints)):
				newx, newy = waypoint_math.TranslateWaypoint(expandedMap, waypoints[i])
				newPointList = [Point(newx, newy, 0)]
				newCellPublisher = rospy.Publisher("newCells", GridCells)
				print "new x and y", newx, newy
				newCellPublisher.publish(AStar.MakeGridCellsFromList(expandedMap, newPointList))
				turnAngle = waypoint_math.ChooseTurnDirection(newx, newy, x, y, theta)
				print turnAngle
				Rotate(turnAngle)
				driveDistance = waypoint_math.ChooseDriveDistance (newx, newy, x, y, theta)
				print driveDistance
				DriveStraight(.4, driveDistance)
				if (stop == 1):
					break
				#check for obstacles/change in map
		except (AStar.NoPathError):
			print "No path error!"
			continue

	print "Lab 4 complete!"
