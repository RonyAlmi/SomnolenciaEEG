# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comunicacion(object):
    def setupUi(self, comunicacion):
        comunicacion.setObjectName("comunicacion")
        comunicacion.resize(328, 165)
        self.layoutWidget = QtWidgets.QWidget(comunicacion)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 127, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.comboB = QtWidgets.QComboBox(self.layoutWidget)
        self.comboB.setStyleSheet("")
        self.comboB.setObjectName("comboB")
        self.horizontalLayout_3.addWidget(self.comboB)
        self.radioButton_Muse = QtWidgets.QRadioButton(comunicacion)
        self.radioButton_Muse.setGeometry(QtCore.QRect(220, 30, 101, 21))
        self.radioButton_Muse.setChecked(True)
        self.radioButton_Muse.setObjectName("radioButton_Muse")
        self.radioButton_MW = QtWidgets.QRadioButton(comunicacion)
        self.radioButton_MW.setGeometry(QtCore.QRect(40, 30, 82, 17))
        self.radioButton_MW.setMouseTracking(True)
        self.radioButton_MW.setChecked(False)
        self.radioButton_MW.setObjectName("radioButton_MW")
        self.label = QtWidgets.QLabel(comunicacion)
        self.label.setGeometry(QtCore.QRect(100, 10, 131, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(comunicacion)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 151, 16))
        self.label_4.setObjectName("label_4")
        self.button_aceptar = QtWidgets.QPushButton(comunicacion)
        self.button_aceptar.setGeometry(QtCore.QRect(110, 130, 91, 31))
        self.button_aceptar.setObjectName("button_aceptar")
        self.line = QtWidgets.QFrame(comunicacion)
        self.line.setGeometry(QtCore.QRect(160, 110, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(comunicacion)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 151, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(comunicacion)
        self.line_3.setGeometry(QtCore.QRect(140, 40, 20, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(comunicacion)
        self.line_4.setGeometry(QtCore.QRect(150, 40, 20, 81))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(comunicacion)
        self.line_5.setGeometry(QtCore.QRect(110, 30, 31, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(comunicacion)
        self.line_6.setGeometry(QtCore.QRect(0, 30, 31, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(comunicacion)
        self.line_7.setGeometry(QtCore.QRect(160, 30, 51, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(comunicacion)
        self.line_8.setGeometry(QtCore.QRect(270, 30, 51, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_5 = QtWidgets.QLabel(comunicacion)
        self.label_5.setGeometry(QtCore.QRect(170, 60, 151, 16))
        self.label_5.setObjectName("label_5")
        self.layoutWidget_2 = QtWidgets.QWidget(comunicacion)
        self.layoutWidget_2.setGeometry(QtCore.QRect(170, 80, 127, 28))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.comboB_muse = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboB_muse.setStyleSheet("")
        self.comboB_muse.setObjectName("comboB_muse")
        self.horizontalLayout_6.addWidget(self.comboB_muse)

        self.retranslateUi(comunicacion)
        QtCore.QMetaObject.connectSlotsByName(comunicacion)

    def retranslateUi(self, comunicacion):
        _translate = QtCore.QCoreApplication.translate
        comunicacion.setWindowTitle(_translate("comunicacion", "comunicacion EEG"))
        self.label_3.setText(_translate("comunicacion", "Puerto"))
        self.radioButton_Muse.setText(_translate("comunicacion", "Muse"))
        self.radioButton_MW.setText(_translate("comunicacion", "MindWave"))
        self.label.setText(_translate("comunicacion", "Seleccione el dispositivo"))
        self.label_4.setText(_translate("comunicacion", "Seleccione el puerto COM"))
        self.button_aceptar.setText(_translate("comunicacion", "ACEPTAR"))
        self.label_5.setText(_translate("comunicacion", "Seleccione Sensores"))
        self.label_8.setText(_translate("comunicacion", "Utilizar"))