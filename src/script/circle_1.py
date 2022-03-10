#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def turtle_circle():
	
	rospy.init_node('circle', anonymous=True)
	pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
	vel_msg = Twist()
	rate = rospy.Rate(10) # this line keeps the while loop running at exact 10 hertz.
	
	#print("Gandalf has nothing on me. I will pass.")
	radius = 0.5 
	speed = 0.5 
	
	while not rospy.is_shutdown():
		vel_msg.linear.x = radius
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = speed
		#rospy.loginfo("Radius %f: ", radius) # Displays radius and coordinates of turtle.
		pub.publish(vel_msg)
		rate.sleep()
		
if __name__ == '__main__':

	try:
		turtle_circle()

	except rospy.ROSInterruptException:
		rospy.loginfo("Node terminated")
		
