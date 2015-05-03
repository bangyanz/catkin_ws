import rospy

from nav2d_navigator import *

if __name__ == '__main__':

	rospy.init_node('ProjectServices')
	print "start services.py"

	rospy.wait_for_service('GetMap')
	print "1"
	startMapping = rospy.ServiceProxy('GetMap', StartMapping)
	try:
		print "trying StartMapping"
		resp1 = startMapping(3)
	except rospy.ServiceException as exc:
		print "mapping exception"
		print("Service did not process request: " + str(exc))

	rospy.wait_for_service('GetMap')
	print "got map"

	rospy.wait_for_service('StartExploration')
	print 2
	startExploration = rospy.ServiceProxy('Explore', StartExploration)
	try:
		print "trying exploration"
		resp1 = startExploration(2)
	except rospy.ServiceException as exc:
		print("Service did not process request: " + str(exc))

	rospy.wait_for_service('Explore')
	print "done exploring"

	print "All done!"