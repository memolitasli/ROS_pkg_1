#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from memoli_paket.msg import lidarmesaj
class lidarClass():
    def __init__(self):
        rospy.init_node("lazerNode")
        rospy.Subscriber("scan",LaserScan,self.lazerCallBack)
        self.pub = rospy.Publisher("lidarBilgi",lidarmesaj,queue_size=10)
        self.lidarMesaj = lidarmesaj()
        rospy.spin()
    def lazerCallBack(self,mesaj):
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])
        on = sol_on + sag_on
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])
        arka = list(mesaj.ranges[170:190])
        min_on = min(on)
        min_sol = min(sol)
        min_sag = min(sag)
        min_arka = min(arka)
        rospy.loginfo("on : " + str(min_on))
        rospy.loginfo("arka : " + str(min_arka))
        rospy.loginfo("sol : " + str(min_sol))
        rospy.loginfo("sag : " + str(min_sag))
        self.lidarMesaj.on = min_on
        self.lidarMesaj.arka = min_arka
        self.lidarMesaj.sag = min_sag
        self.lidarMesaj.sol = min_sol
        self.lidarMesaj.solOn = min(sol_on)
        self.lidarMesaj.sagOn = min(sag_on)
        self.pub.publish(self.lidarMesaj)
       
            
        
lidarNesne = lidarClass()
        
