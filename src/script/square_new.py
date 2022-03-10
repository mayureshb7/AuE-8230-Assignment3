#!/usr/bin/env python3

PI = 3.1415926535897
import rospy
from geometry_msgs.msg import Twist
#PI = 3.1415926535897
 
def drive():
    rospy.init_node('square_node',anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    velocity = Twist()

    #Drawing square by user
    #print("Drive turtle in square")
    speed = 0.1
    distance = 0.4
    #ForwardCheck = 1
    speed_ang= 0.25
    #angle = float(input("Input desired rotation degrees: "))
    #Clockwisecheck = 1

    #Defining angular velocity of the turtle
    #ang_speed_turtle = 0.25
    #PI = 3.1415926535897

    #Defining angle of the turtle
    #turtle_angle = 90*2*PI/360

    #considering initial velocity zero except x linear 		
    velocity.linear.x = 0
    velocity.linear.y = 0
    velocity.linear.z = 0
    velocity.angular.x = 0
    velocity.angular.y = 0
    velocity.angular.z = 0
 	
 	
    while not rospy.is_shutdown():

        for i in range(4):
            
            #Travelling in a straight path
            
            t0 = rospy.Time.now().to_sec()
            dis_now = 0
            velocity.linear.x = speed

            while(dis_now < distance):
                velocity_publisher.publish(velocity)
                #Record time
                t1 = rospy.Time.now().to_sec()
                dis_now = speed * (t1-t0)
                #calculating distance travelled based on the time and velocity


            velocity.linear.x = 0
            velocity_publisher.publish(velocity)

            # Rotation
            velocity.angular.z = speed_ang
            t0 = rospy.Time.now().to_sec()
            ang_now = 0

            turtle_angle = 90*2*PI/360

            while(ang_now < turtle_angle):
                velocity_publisher.publish(velocity)
                
                t1 = rospy.Time.now().to_sec()

                ang_now = speed_ang * (t1-t0)

            velocity.angular.z = 0
            velocity_publisher.publish(velocity)

        rospy.spin()

 	
if __name__ == '__main__':
    try:
        
        drive()
    except rospy.ROSInterruptException: 
        pass
 
