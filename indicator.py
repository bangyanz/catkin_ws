import rospy, subprocess, time

def CmdCallback(velocityMsg):
	global drive, turn

	drive = velocityMsg.linear
	turn = velocityMsg.angular


if __name__ == '__main__':
	global drive, turn

	rospy.Subscriber('cmd_vel_mux/input/teleop', Twist, CmdCallback)

	#sleep for one minute so /StartMapping can run
	rospy.sleep(600000)

	#i updates every ten seconds. This loop should run for 9 minutes
	while (i < 54):
		#if Twist message is (0,0)
		if (drive = 0 and turn = 0):
			subprocess.call('spd-say "Done Mapping"')
			print "Done Mapping"
		#sleep for 10 seconds
		rospy.sleep(10000)
		i += 1

	#if Twist message (0,0) is not published in 9 minutes
 	subprocess.call('spd-say "timeout"')
	print "timeout"


