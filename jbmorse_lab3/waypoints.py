import rospy

from geometry_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point

def Waypoints (path):

	Poses = path.PoseStamped
	poseList = path.Poses
	i = 0
	for pose in PoseList:
		


