#!/usr/bin/env python

import rospy, time
from std_msgs.msg import Int32
import RPi.GPIO as GPIO

def shield_position():
   pub=rospy.Publisher('move_servos', Int32, queue_size=10)
   rospy.init_node('shield_talker', anonymous=True)
   rate =  rospy.Rate(5)
   while not rospy.is_shutdown():
     time.sleep(5)
     rospy.loginfo("move to max position: 180")
     pub.publish(600)
     time.sleep(25)
     rospy.loginfo("move to min position: 0")
     pub.publish(150)
     time.sleep(25)



if __name__=='__main__':
   try:
     shield_position()
   except rospy.ROSInterruptException:
     pass
