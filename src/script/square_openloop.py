#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897
 
def drive():
 	rospy.init_node('square_node',anonymous=True)
 	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
 	velocity = Twist()
 	
 	#Drawing square by user
 	#print("Drive turtle in square")
 	speed = 0.3
 	distance = 1.5
 	ForwardCheck = 1
 	speed_ang= 0.3
 	#angle = float(input("Input desired rotation degrees: "))
 	Clockwisecheck = 1
 	
 	#Defining angular velocity of the turtle
 	ang_speed_turtle = 0.3
 	
 	#Defining angle of the turtle
 	turtle_angle = 91*2*PI/360
 	
 	#considering initial velocity zero except x linear 		
 	velocity.linear.y = 0
 	velocity.linear.z = 0
 	velocity.angular.x = 0
 	velocity.angular.y = 0
 	velocity.angular.z = 0
 	i=0
 	
 	while (i<4):
 	
 #code to move in the straight line
 
 		time0 = rospy.Time.now().to_sec()
 		distance_now = 0
 		
 		while(distance_now<distance):
 			if(ForwardCheck):
 				
 				velocity.linear.x = abs(speed)
 			else:
 				speed = 0.3
 				velocity.linear.x = -abs(speed)
 				
 			velocity_publisher.publish(velocity)
 			time1 = rospy.Time.now().to_sec()
 			distance_now = speed*(time1-time0)
 			print(velocity)
 		velocity.linear.x = 0
 		velocity_publisher.publish(velocity)
 
 #Code for rotation	
 		if(Clockwisecheck):
 			velocity.angular.z = -abs(ang_speed_turtle)
 		else:
 			velocity.angular.z = abs(ang_speed_turtle)
 		time2 = rospy.Time.now().to_sec() 			
 		angle_now = 0 
 	
 		while(angle_now<turtle_angle):
 			velocity_publisher.publish(velocity)
 			time3 = rospy.Time.now().to_sec()
 			angle_now = ang_speed_turtle *(time3-time2)
 			print(velocity)
 	
 		velocity.angular.z = 0
 		velocity_publisher.publish(velocity)
 		#rospy.sleep(1)
 		rospy.spin()
 		i=i+1
 	
if __name__ == '__main__':
 	#try:
 	drive()
 	#except rospy.ROSInterruptException: pass
 
