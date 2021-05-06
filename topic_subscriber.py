#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):
    print (msg.data)

rospy.init_node('topic_subscriber')

sub = rospy.Subscriber('counter', Int32, callback)

rospy.spin()
# 구독이 시작되면 Ros에게 제어를 넘긴다.
