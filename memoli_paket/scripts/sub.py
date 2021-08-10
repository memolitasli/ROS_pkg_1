#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from memoli_paket.msg import bilgi

class subClass():
    def __init__(self):
        rospy.init_node("subsriberNode")
        rospy.Subscriber("bilgiMesajTopic",bilgi,self.bilgiCallBack)
        rospy.spin()
    def bilgiCallBack(self,mesaj):
        rospy.loginfo("Dron adi : " + str(mesaj.isim))
        rospy.loginfo("konum X : " + str(mesaj.konumX))
        rospy.loginfo("konum Y : " + str(mesaj.konumY))
        rospy.loginfo("konum Z : " + str(mesaj.konumZ))
        rospy.loginfo("Lineer Hiz X : " + str(mesaj.linearHizX))
        rospy.loginfo("Lineer Hiz Y : " + str(mesaj.linearHizY))
        rospy.loginfo("Lineer Hiz Z : " + str(mesaj.linearHizZ))
        rospy.loginfo("Acisal Hiz : " + str(mesaj.angularHiz))
subNesne = subClass()