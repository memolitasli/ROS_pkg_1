#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 281, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_dur = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_dur.setObjectName("btn_dur")
        self.gridLayout.addWidget(self.btn_dur, 1, 1, 1, 1)
        self.btn_ileri = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_ileri.setObjectName("btn_ileri")
        self.gridLayout.addWidget(self.btn_ileri, 0, 1, 1, 1)
        self.btn_geri = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_geri.setObjectName("btn_geri")
        self.gridLayout.addWidget(self.btn_geri, 2, 1, 1, 1)
        self.btn_sagDon = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sagDon.setObjectName("btn_sagDon")
        self.gridLayout.addWidget(self.btn_sagDon, 1, 2, 1, 1)
        self.btn_solDon = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_solDon.setObjectName("btn_solDon")
        self.gridLayout.addWidget(self.btn_solDon, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Kontrol"))
        self.btn_dur.setText(_translate("MainWindow", "dur"))
        self.btn_ileri.setText(_translate("MainWindow", "ileri"))
        self.btn_geri.setText(_translate("MainWindow", "geri"))
        self.btn_sagDon.setText(_translate("MainWindow", "sagDon"))
        self.btn_solDon.setText(_translate("MainWindow", "solDon"))
        
        self.hizMesaji = Twist()
        rospy.init_node("arayuzKontrol")
        self.pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)

        self.btn_ileri.clicked.connect(self.ileriGit)
        self.btn_geri.clicked.connect(self.geriGit)
        self.btn_solDon.clicked.connect(self.solDon)
        self.btn_sagDon.clicked.connect(self.sagDon)
        self.btn_dur.clicked.connect(self.dur)
    def ileriGit(self):
        self.hizMesaji.linear.x = 1.0
        self.hizMesaji.linear.y = 0.0
        self.hizMesaji.linear.z = 0.0
        self.hizMesaji.angular.z =0.0
        self.pub.publish(self.hizMesaji)
    def geriGit(self):
        self.hizMesaji.linear.x = -1.0
        self.hizMesaji.linear.y = 0.0
        self.hizMesaji.linear.z = 0.0
        self.hizMesaji.angular.z =0.0
        self.pub.publish(self.hizMesaji)
    def sagDon(self):
        self.hizMesaji.linear.x = 0.0
        self.hizMesaji.linear.y = 0.0
        self.hizMesaji.linear.z = 0.0
        self.hizMesaji.angular.z = -0.5
        self.pub.publish(self.hizMesaji)
    def solDon(self):
        self.hizMesaji.linear.x = 0.0
        self.hizMesaji.linear.y = 0.0
        self.hizMesaji.linear.z = 0.0
        self.hizMesaji.angular.z = 0.5
        self.pub.publish(self.hizMesaji)
    def dur(self):
        self.hizMesaji.linear.x = 0.0
        self.hizMesaji.linear.y = 0.0
        self.hizMesaji.linear.z = 0.0
        self.hizMesaji.angular.z =0.0
        self.pub.publish(self.hizMesaji)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
