#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'robot_bilgi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import rospy
from memoli_paket.msg import bilgi
from memoli_paket.msg import lidarmesaj
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 600)
        MainWindow.setMinimumSize(QtCore.QSize(425, 600))
        MainWindow.setMaximumSize(QtCore.QSize(425, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.le_konumY = QtWidgets.QLineEdit(self.centralwidget)
        self.le_konumY.setObjectName("le_konumY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_konumY)
        self.le_konumX = QtWidgets.QLineEdit(self.centralwidget)
        self.le_konumX.setObjectName("le_konumX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_konumX)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_konumX_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_konumX_2.setObjectName("le_konumX_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_konumX_2)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.le_linearHizX = QtWidgets.QLineEdit(self.centralwidget)
        self.le_linearHizX.setObjectName("le_linearHizX")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_linearHizX)
        self.le_linearHizY = QtWidgets.QLineEdit(self.centralwidget)
        self.le_linearHizY.setObjectName("le_linearHizY")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_linearHizY)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_linearHizZ = QtWidgets.QLineEdit(self.centralwidget)
        self.le_linearHizZ.setObjectName("le_linearHizZ")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_linearHizZ)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_angularHiz = QtWidgets.QLineEdit(self.centralwidget)
        self.le_angularHiz.setObjectName("le_angularHiz")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_angularHiz)
        self.gridLayout.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.le_lidarOn = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lidarOn.setObjectName("le_lidarOn")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_lidarOn)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.le_lidarArka = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lidarArka.setObjectName("le_lidarArka")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_lidarArka)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.le_lidarSol = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lidarSol.setObjectName("le_lidarSol")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_lidarSol)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.le_lidarSag = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lidarSag.setObjectName("le_lidarSag")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_lidarSag)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.le_lidarSolOn = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lidarSolOn.setObjectName("le_lidarSolOn")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_lidarSolOn)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.le_lidarSagOn = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lidarSagOn.setObjectName("le_lidarSagOn")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_lidarSagOn)
        self.gridLayout.addLayout(self.formLayout_3, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Bilgi Paneli"))
        self.label_4.setText(_translate("MainWindow", "Konum Bilgileri"))
        self.label.setText(_translate("MainWindow", "Konum X : "))
        self.label_2.setText(_translate("MainWindow", "konum Y : "))
        self.label_3.setText(_translate("MainWindow", "konum Z : "))
        self.label_9.setText(_translate("MainWindow", "Hız Bilgileri : "))
        self.label_5.setText(_translate("MainWindow", "Linear Hız X : "))
        self.label_6.setText(_translate("MainWindow", "Linear Hız  Y : "))
        self.label_7.setText(_translate("MainWindow", "Linear Hız  Z : "))
        self.label_8.setText(_translate("MainWindow", "Açısal Hız   : "))
        self.label_16.setText(_translate("MainWindow", "Lidar Bilgileri"))
        self.label_10.setText(_translate("MainWindow", "On : "))
        self.label_11.setText(_translate("MainWindow", "Arka  : "))
        self.label_12.setText(_translate("MainWindow", "Sol : "))
        self.label_13.setText(_translate("MainWindow", "Sağ  : "))
        self.label_14.setText(_translate("MainWindow", "Sol On : "))
        self.label_15.setText(_translate("MainWindow", "Sağ On : "))
        rospy.init_node("bilgiPencereNode")
        rospy.Subscriber("lidarBilgi",lidarmesaj,self.lidarCallBack)
        rospy.Subscriber("bilgiMesajTopic",bilgi,self.konumCallBack)
        
    def lidarCallBack(self,mesaj):
        self.le_lidarOn.setText(str(mesaj.on))
        self.le_lidarArka.setText(str(mesaj.arka))
        self.le_lidarSol.setText(str(mesaj.sol))
        self.le_lidarSag.setText(str(mesaj.sag))
        self.le_lidarSolOn.setText(str(mesaj.solOn))
        self.le_lidarSagOn.setText(str(mesaj.sagOn))
    def konumCallBack(self,mesaj):
        self.le_konumX.setText(str(mesaj.konumX))
        self.le_konumY.setText(str(mesaj.konumY))
        self.le_konumX_2.setText(str(mesaj.konumZ))
        self.le_linearHizX.setText(str(mesaj.linearHizX))
        self.le_linearHizY.setText(str(mesaj.linearHizY))
        self.le_linearHizZ.setText(str(mesaj.linearHizZ))
        self.le_angularHiz.setText(str(mesaj.angularHiz))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())