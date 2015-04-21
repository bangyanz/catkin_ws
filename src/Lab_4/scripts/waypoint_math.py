#!/usr/bin/env python

# the thing josh said I needed
import rospy
import math
import time
from geometry_msgs.msg import Point

def ChooseTurnDirection (goalx, goaly, startx, starty, theta):

	#goal_waypoint = waypointList[1]
	localx = goalx - startx
	localy = goaly - starty

	goal_theta = 0

	if (localx == 0.0):
		if (localy > 0.0):
			goal_theta = math.pi/2
		else:
			goal_theta = -math.pi/2
	else:
		goal_theta = math.atan2(localy, localx) - theta
		print "turn towards", math.atan2(localy, localx)

	return goal_theta

def ChooseDriveDistance (goalx, goaly, x, y, theta):
	return ((((x - goalx) ** 2) + ((y - goaly) ** 2)) ** (0.5))

def TranslateWaypoint(gridMap, point):

	#print "translating waypoint"
	#print "origin x", gridMap.info.origin.position.x
	#print "origin y", gridMap.info.origin.position.y
	#print "oldx", point.x
	#print "oldy", point.y

	newx = ((float(point.x)/ 10) + gridMap.info.origin.position.x)
	newy = ((float(point.y) / 10) + gridMap.info.origin.position.y)

	#print "newx", newx
	#print "newy", newy

	return newx, newy

if __name__ == '__main__':

	while (1):
	 	startx = float(input("Enter startx: "))
	 	starty = float(input("Enter starty: "))
	 	goalx = float(input("Enter goalx: "))
	 	goaly = float(input("Enter goaly: "))
	 	starttheta = float(input("Enter starttheta: "))
	 	goaltheta = ChooseTurnDirection(startx, starty, goalx, goaly, starttheta)
	 	print "goaltheta", goaltheta
