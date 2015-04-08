#!/usr/bin/env python

import rospy, tf

from tf.transformations import euler_from_quaternion

from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

import time
import math


#This function sequentially calls methods to perform a trajectory.
#The trajectory is defined to be a capital 'R'
def DoTheThing():
	DriveStraight(.25, .6)
	time.sleep(2)
	Rotate(math.pi / -2)
	time.sleep(2)
	DriveArc(.15, math.pi / 8, math.pi / -1)
	time.sleep(2)
	Rotate(3 * math.pi / 4)
	time.sleep(2)
	DriveStraight(.25, .42)


def PublishTwist(linearVelocity, angularVelocity):

	twist = Twist()
	twist.linear.x = linearVelocity
	twist.linear.y = 0
	twist.linear.z = 0
	twist.angular.x = 0
	twist.angular.y = 0
	twist.angular.z = angularVelocity

	publisher.publish(twist)


def DriveStraight(speed, distance):

	global x
	global y
	tol = .1
	acc = 0
	
	time.sleep(.5)

	xGoal = x + distance * math.cos(theta)
	yGoal = y + distance * math.sin(theta)

	while ((x < xGoal - tol or x > xGoal + tol) or (y < yGoal - tol or y > yGoal + tol)):
		acc += .1
		if (acc > 1):
			acc = 1
		PublishTwist(speed * acc, 0)
		time.sleep(.1)

	while (acc != 0):
		acc -= .1
		if (acc < 0):
			acc = 0
		PublishTwist(speed * acc, 0)
		time.sleep(.1)

	PublishTwist(0, 0)

	#BlindMethod
	#SpinWheels(speed, speed, distance / speed)


def Rotate(angleOfRotation):

	global theta

	tol = math.pi / 36

	print "tol"
	print tol
	
	time.sleep(.5)

	angleGoal = (theta + angleOfRotation) 
	if (angleGoal > math.pi):
		angleGoal -= (math.pi * 2)
	elif (angleGoal < (-1 * math.pi)):
		angleGoal += (math.pi * 2)

	print "theta"
	print theta

	print "angleOfRotation"
	print angleOfRotation

	print "AngleGoal"
	print angleGoal

	while (theta < angleGoal - tol or theta > angleGoal + tol):
		if (angleOfRotation < 0):
			PublishTwist(0, math.pi / -6)
		else:
			PublishTwist(0, math.pi / 6)
		print theta
		time.sleep(.1)

	print "DONE with rotate"
	PublishTwist(0, 0)

	#BlindMethod
	#if (angleOfRotation < 0):
	#	SpinWheels(-1, 1, (angleOfRotation * -1) / (2 / robotRadius))
	#else:
	#	SpinWheels(1, -1, angleOfRotation / (2 / robotRadius))


def DriveArc(radiusOfTurn, angularSpeed, angleOfRotation):

	global theta
	tol = math.pi / 36
	
	wheelSpeed1 = angularSpeed * (radiusOfTurn + (robotRadius/2))
	wheelSpeed2 = angularSpeed * (radiusOfTurn - (robotRadius/2))
	linearSpeed = (wheelSpeed1 + wheelSpeed2) / 2

	angleGoal = (theta + angleOfRotation) 
	if (angleGoal > math.pi):
		angleGoal -= (math.pi * 2)
	elif (angleGoal < (-1 * math.pi)):
		angleGoal += (math.pi * 2)

	print angleGoal
	print "goal"

	while (theta < angleGoal - tol or theta > angleGoal + tol):
		if (angleOfRotation < 0):
			PublishTwist(linearSpeed, -1 * angularSpeed)
		else:
			PublishTwist(linearSpeed, angularSpeed)
		print theta
		time.sleep(.1)

	PublishTwist(0, 0)

	#BlindMethod
	#wheelSpeed1 = angularSpeed * (radiusOfTurn + (robotRadius/2))
	#wheelSpeed2 = angularSpeed * (radiusOfTurn - (robotRadius/2))
	#if (angleOfRotation < 0):
	#	SpinWheels(wheelSpeed2, wheelSpeed1, (-1 * angleOfRotation) / angularSpeed)
	#else:
	#	SpinWheels(wheelSpeed1, wheelSpeed2, angleOfRotation / angularSpeed)


#Odometry Callback function
def OdometryCallback(msg):
	global x
	global y
	global theta
	xPos = msg.pose.pose.position.x
	yPos = msg.pose.pose.position.y
	orientation = msg.pose.pose.orientation
	quaternion = [orientation.x, orientation.y, orientation.z, orientation.w]
	roll, pitch, yaw = euler_from_quaternion(quaternion)

	x = xPos
	y = yPos
	theta = yaw


#Bumper Callback function
def BumperCallback(msg):
	global bumper
	print "I got booped"
	if (msg.state == BumperEvent.RELEASED):
		bumper = 1


def SpinWheels(leftWheelVelocity, rightWheelVelocity, runTime):

	linearVelocity = (wheelRadius) * (leftWheelVelocity + rightWheelVelocity) / 2
	angularVelocity = (wheelRadius / robotRadius) * (rightWheelVelocity - leftWheelVelocity) / 2

	startTime = time.time()

	while ((time.time() - startTime) < runTime):
		PublishTwist(linearVelocity, angularVelocity)

	PublishTwist(0, 0)


if __name__ == '__main__':

	global publisher, bumper, odom_list, wheelRadius, robotRadius

	rospy.init_node('jbmorse_Lab_2_node')

	wheelRadius = .0381
	robotRadius = .2286
	bumper = 0

	publisher = rospy.Publisher('cmd_vel_mux/input/teleop', Twist) 

	rospy.Subscriber('odom', Odometry, OdometryCallback) 
	rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, BumperCallback) 

	odom_list = tf.TransformListener()

	rospy.sleep(rospy.Duration(1, 0))

	print "Starting Lab 2"

	print bumper
	while (bumper == 0):
		print bumper
		time.sleep(.5)
		
	print "Its go time"
	DoTheThing()

	print "Lab 2 complete!"
