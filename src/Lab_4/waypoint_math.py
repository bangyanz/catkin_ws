# the thing josh said I needed
import rospy
import math

def ChooseTurnDirection (waypointList, x, y, theta):

	goal_waypoint = waypointList[1]
	goal_x = goal_waypoint.x - x
	goal_y = goal_waypoint.y - y

	goal_theta = 0

	if (goal_x == 0):
		if (goal_y > 0):
			goal_theta = math.pi/2
		else:
			goal_theta = -math.pi/2
	else:
		goal_theta = theta - math.atan(goal_y/goal_x) 
	return goal_theta

# #Odometry Callback function
# def OdometryCallback(msg):
# 	#Current x, y, and theta
# 	global x, y, theta
# 	xPos = msg.pose.pose.position.x
# 	yPos = msg.pose.pose.position.y
# 	orientation = msg.pose.pose.orientation
# 	quaternion = [orientation.x, orientation.y, orientation.z, orientation.w]
# 	roll, pitch, yaw = euler_from_quaternion(quaternion)

# 	x = xPos
# 	y = yPos
# 	theta = yaw

# if __name__ == '__main__':

# 	global x, y, theta

# 	x, y, theta = 0

# 	rospy.Subscriber('odom', Odometry, OdometryCallback) 