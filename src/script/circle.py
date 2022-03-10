#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
#import sys

def turtle_circle():
    rospy.init_node('circle', anonymous=True)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    
    vel = Twist()
    rate = rospy.Rate(10)
    #clockwise = True
    linevel=0.1
    angvel=0.4
    
    while not rospy.is_shutdown():
        vel.linear.x= linevel
        vel.linear.y= 0
        vel.linear.z= 0

        vel.angular.x= 0
        vel.angular.y= 0
        vel.angular.z= angvel
        #rospy.loginfo("Linear", line_vel)
        #rospy.loginfo("Ang", ang_vel)
        pub.publish(vel)
        rate.sleep()
    

if __name__ == '__main__':

    try:
        turtle_circle()
    except rospy.ROSInterruptException:
        rospy.loginfo("Terminate")