#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D
class dp():

	def __init__(self):
		rospy.init_node('dp', anonymous=True)
		rospy.loginfo('The infocenter is initilized...')
		self.pub1 = rospy.Publisher('/info/trajectory', Pose2D, queue_size = 100)
		rospy.wait_for_message('read',String)
		rospy.Subscriber('read',String, self.callback, queue_size=1)

	def callback(self,data):
		#rospy.loginfo(rospy.get_caller_id() + "/n I heard %s", data.data)
     		self.postdata = data.data.split(',')
                #rospy.loginfo(self.postdata)
     		if self.postdata[0] == 'AA':
			rospy.loginfo("data received")
			rospy.loginfo("the status is: " + str(postdata[1]))
			pose = Pose2D()
     			pose.x = float(self.postdata[2])
     			pose.y = float(self.postdata[3])
			pose.theta = float(self.postdata[4])
			rospy.loginfo(str(pose.x)+" " +str(pose.y)+" "+str(pose.theta))
     			self.pub1.publish(pose)
		else:
			rospy.loginfo("not a valid data")

if __name__ == '__main__':
    try:
    	dp()
    	rospy.spin()
    except:
    	pass
