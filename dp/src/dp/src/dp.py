#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray

def callback(data):
	 rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     location = data.data.split(',')
     
def talker():
     pub = rospy.Publisher('location', Float32MultiArray, queue_size=100)
     rospy.init_node('dp', anonymous=True)
     rospy.Subscriber('read',String, callback)
     rate = rospy.Rate(10) # 10hz
     while not rospy.is_shutdown():
         
         location_str = "hello world %s" % rospy.get_time()
         rospy.loginfo(hello_str)
         pub.publish(hello_str)
         rate.sleep()
if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass
