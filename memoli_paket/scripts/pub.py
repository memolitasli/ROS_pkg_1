#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from memoli_paket.msg import bilgi
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rospy.core import is_shutdown
from rospy.timer import Rate

class pubClass():
    def __init__(self):
        self.yayinlanacakMesaj = bilgi()
       
        rospy.init_node("publisherNode")
        self.pub = rospy.Publisher("bilgiMesajTopic",bilgi,queue_size=10)
        self.rate = rospy.Rate(10)
        rospy.Subscriber("odom", Odometry, self.odomcallback)
        rospy.Subscriber("cmd_vel",Twist,self.TwistCallBack)
        while not rospy.is_shutdown():
            self.yayinlanacakMesaj.isim = "memoli_dron"
            self.pub.publish(self.yayinlanacakMesaj)
            self.rate.sleep()

    def TwistCallBack(self,mesaj):
        self.yayinlanacakMesaj.linearHizX = mesaj.linear.x
        self.yayinlanacakMesaj.linearHizY = mesaj.linear.y
        self.yayinlanacakMesaj.linearHizZ = mesaj.linear.z
        self.yayinlanacakMesaj.angularHiz = mesaj.angular.z
    def odomcallback(self,mesaj):
        self.yayinlanacakMesaj.konumX = mesaj.pose.pose.position.x
        self.yayinlanacakMesaj.konumY = mesaj.pose.pose.position.y
        self.yayinlanacakMesaj.konumZ = mesaj.pose.pose.position.z

pubNesne = pubClass()
        