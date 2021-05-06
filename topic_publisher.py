#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')

pub = rospy.Publisher('counter', Int32)

rate = rospy.Rate(2)

count = 0

while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()

# is_shutdown() : 노드가 종료될 상황이면 True를 반환하고, 아니면 False를 반환하여
# while 반복문을 빠져 나갈지 여부를 결정할 수 있게 한다.
# rate.sleep() : 대략 2Hz 주기로 while 반복문 몸체를 실행할 수 있을 정도로 충분한
# 시간만큼 일시정지한다.
