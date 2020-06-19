#! /usr/bin/env python

import rospy
import math 
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyRequest
rospy.init_node('key_vel_publisher')
rospy.sleep(5)
pub = rospy.Publisher('/key_vel',Twist, queue_size=1000)
rospy.wait_for_service('/global_localization')
rospy.wait_for_service('/move_base/clear_costmaps') 
global_localization_service = rospy.ServiceProxy('/global_localization',Empty)   
clear_costmaps_service = rospy.ServiceProxy('/move_base/clear_costmaps',Empty)
empty_request = EmptyRequest()
global_localization_service(empty_request) 
cmd = Twist()
while (pub.get_num_connections() == 0):
    continue  
rate = rospy.Rate(rospy.get_param('~hz', 10)) 
cmd.linear.x = 0
cmd.linear.y = 0
cmd.angular.z = -0.4
last_time = rospy.get_time() 
while rospy.get_time()-last_time<math.pi*5:
    pub.publish(cmd)
    rate.sleep()
# rospy.sleep(5)
# cmd.linear.x = 1
# cmd.linear.y = 0
# cmd.angular.z = 0
# last_time = rospy.get_time()
# while rospy.get_time()-last_time<2:
#     pub.publish(cmd)
#     rate.sleep()
# cmd.linear.x = 0
# cmd.linear.y = 0
# cmd.angular.z = 0.2
# last_time = rospy.get_time() 
# while rospy.get_time()-last_time<10*math.pi:
#     pub.publish(cmd)
#     rate.sleep()

'''
cmd.linear.x = 0
cmd.linear.y = 0.1
cmd.angular.z = 0
last_time = rospy.get_time()
while rospy.get_time()-last_time<4:
    pub.publish(cmd)
    rate.sleep()
cmd.linear.x = 0
cmd.linear.y = 0
cmd.angular.z = 0.4
last_time = rospy.get_time()
while rospy.get_time()-last_time<5*math.pi:
    pub.publish(cmd)
    rate.sleep()
cmd.linear.x = 0.1
cmd.linear.y = 0
cmd.angular.z = 0
last_time = rospy.get_time()
while rospy.get_time()-last_time<4:
    pub.publish(cmd)
    rate.sleep()
cmd.linear.x = 0
cmd.linear.y = 0
cmd.angular.z = 0.4
last_time = rospy.get_time()
while rospy.get_time()-last_time<5*math.pi:
    pub.publish(cmd)
    rate.sleep()
cmd.linear.x = 0
cmd.linear.y = -0.1
cmd.angular.z = 0
last_time = rospy.get_time()
while rospy.get_time()-last_time<4:
    pub.publish(cmd)
    rate.sleep()
'''

clear_costmaps_service(empty_request)

