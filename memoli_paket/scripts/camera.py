#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class robotCamera():
    def __init__(self):
        rospy.init_node("cameraNode")
        rospy.Subscriber("camera/rgb/image_raw",Image,self.imageCallBack)
        self.bridge = CvBridge()
        rospy.spin()
    def imageCallBack(self,mesaj):
        self.foto =self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        cv2.imshow("robot Kamerasi",self.foto)
        cv2.waitKey(1)
camNesne = robotCamera()