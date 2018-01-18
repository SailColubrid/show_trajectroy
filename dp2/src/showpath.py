#!/usr/bin/env python
# license removed for brevity
import rospy
from nav_msgs.msg import Path
from std_msgs.msg import String
from geometry_msgs.msg import *
from visualization_msgs.msg import *
import tf

class showpath():

	def __init__(self):
		rospy.init_node('showpath', anonymous = False)
		rospy.loginfo('showpath is initialized...')
		self.pub = rospy.Publisher('trajectory', Path, queue_size = 10)
		self.marker_pub = rospy.Publisher('line', Marker, queue_size = 10)
		self.sub = rospy.Subscriber('/info/trajectory', Pose2D, self.callback, queue_size = 10)
		self.path = Path()
		self.path.header.stamp = rospy.Time.now()
                self.path.header.frame_id = 'odom'
		self.this_pose_stamped = PoseStamped()
		self.marker = Marker()
		#self.point = Point()
		#self.goal_quat = Quaternion()

	def callback(self, data):
		#rospy.loginfo("data_received "+str(data.x)+" "+str(data.y))
		self.drawpath(data)

	def drawpath(self, data):
		self.this_pose_stamped.pose.position.x = data.x
		self.this_pose_stamped.pose.position.y = data.y
        	#self.goal_quat = tf.createQuaternionMsgFromYaw(data.theta)
	        q = tf.transformations.quaternion_from_euler(0, 0, data.theta)
        	goal_quat = Quaternion(*q)
		self.this_pose_stamped.pose.orientation.x = goal_quat.x
		self.this_pose_stamped.pose.orientation.y = goal_quat.y
		self.this_pose_stamped.pose.orientation.z = goal_quat.z
		self.this_pose_stamped.pose.orientation.w = goal_quat.w
		self.this_pose_stamped.header.stamp = rospy.Time.now()
		self.this_pose_stamped.header.frame_id = 'odom'
		self.path.poses.append(self.this_pose_stamped)
		#rospy.loginfo(str(len(self.path.poses)))
		self.pub.publish(self.path)
		self.marker.header.frame_id = 'odom'
		self.marker.header.stamp = rospy.Time.now()
		self.marker.id = 0
		self.marker.ns = "basic_shapes"
		self.marker.type = 4
		self.marker.action = 0
		point = Point()
		point.x = data.x
		point.y = data.y
		point.z = 0.0
		self.marker.frame_locked = True
		#self.marker.pose.position.z = self.point.z = 0.0
		self.marker.pose.orientation.w = 1.0
		self.marker.color.r = 0.0
		self.marker.color.g = 1.0
		self.marker.color.b = 0.0
		self.marker.color.a = 1.0
		#self.marker.colors.append(self.marker.color)
		self.marker.scale.x = 0.03
		self.marker.points.append(point)
		#self.marker.scale.y = 0.02
		#self.marker.scale.z = 0.001
		self.marker.lifetime.secs = 100
		self.marker.lifetime.nsecs = 0.0
		#self.markers.markers.append(self.marker)
		self.marker_pub.publish(self.marker)

if __name__ == '__main__':
	try:
		showpath()
		rospy.spin()
	except:
		pass
