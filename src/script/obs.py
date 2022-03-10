#! /usr/bin/env python3

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist	

pub = None

def LIDAR(msg):
    regions = {
        'Forward':  min(min(msg.ranges[359:361]), 10)
    }
    take_action(regions)
    
def take_action(regions):

   msg = Twist()
   linear_x = 0
   linear_y = 0
   linear_z = 0
   
   angular_x = 0
   angular_y = 0   
   angular_z = 0
   
   if regions['Forward'] > 2:
       linear_x = 0.3
       angular_z = 0
       
   elif regions['Forward'] < 2:
       linear_x = 0
       angular_z = 0
       rospy.loginfo(regions)
       
   msg.linear.x = linear_x
   msg.linear.y = linear_y
   msg.linear.z = linear_z
   msg.angular.x = angular_x
   msg.angular.y = angular_y
   msg.angular.z = angular_z
   pub.publish(msg)
   
def main():
    global pub
    rospy.init_node('obs')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/scan', LaserScan, LIDAR)
    rospy.spin()

if __name__ == '__main__':
    main()  
    

