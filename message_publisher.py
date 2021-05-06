#!/usr/bin/env python
import rospy
from basics.msg import Complex
from random import random

rospy.init_node('massage_publisher')
pub = rospy.Publisher('complex', Complex)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()
    pub.publish(msg)
    rate.sleep()
