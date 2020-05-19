# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainApp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_charts = QVBoxLayout()
        self.verticalLayout_charts.setObjectName(u"verticalLayout_charts")

        self.horizontalLayout.addLayout(self.verticalLayout_charts)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.main)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(150, 0))
        self.widget_3.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.lcdNumber_3 = QLCDNumber(self.widget_3)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.verticalLayout_7.addWidget(self.lcdNumber_3)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(150, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_6.addWidget(self.lcdNumber)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(self.main)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(150, 0))
        self.widget_2.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.lcdNumber_2 = QLCDNumber(self.widget_2)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.verticalLayout_8.addWidget(self.lcdNumber_2)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.opcionesTabWidget = QTabWidget(self.main)
        self.opcionesTabWidget.setObjectName(u"opcionesTabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.opcionesTabWidget.sizePolicy().hasHeightForWidth())
        self.opcionesTabWidget.setSizePolicy(sizePolicy1)
        self.opcionesTabWidget.setMaximumSize(QSize(16777215, 220))
        self.conf1 = QWidget()
        self.conf1.setObjectName(u"conf1")
        self.horizontalLayout_3 = QHBoxLayout(self.conf1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dial_PEEP = QDial(self.conf1)
        self.dial_PEEP.setObjectName(u"dial_PEEP")
        self.dial_PEEP.setMaximumSize(QSize(16777215, 60))
        self.dial_PEEP.setMaximum(20)

        self.gridLayout_2.addWidget(self.dial_PEEP, 2, 4, 1, 1)

        self.lcdNumber_PIP = QLCDNumber(self.conf1)
        self.lcdNumber_PIP.setObjectName(u"lcdNumber_PIP")
        self.lcdNumber_PIP.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_PIP, 1, 3, 1, 1)

        self.lcdNumber_VT = QLCDNumber(self.conf1)
        self.lcdNumber_VT.setObjectName(u"lcdNumber_VT")
        self.lcdNumber_VT.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_VT, 1, 5, 1, 1)

        self.label_RR = QLabel(self.conf1)
        self.label_RR.setObjectName(u"label_RR")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_RR.setFont(font2)
        self.label_RR.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_RR, 0, 0, 1, 1)

        self.label_17 = QLabel(self.conf1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 0, 5, 1, 1)

        self.label_16 = QLabel(self.conf1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 0, 4, 1, 1)

        self.label_13 = QLabel(self.conf1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)

        self.dial_PIP = QDial(self.conf1)
        self.dial_PIP.setObjectName(u"dial_PIP")
        self.dial_PIP.setMaximumSize(QSize(16777215, 60))
        self.dial_PIP.setMinimum(15)
        self.dial_PIP.setMaximum(50)

        self.gridLayout_2.addWidget(self.dial_PIP, 2, 3, 1, 1)

        self.dial_RR = QDial(self.conf1)
        self.dial_RR.setObjectName(u"dial_RR")
        self.dial_RR.setMaximumSize(QSize(16777215, 60))
        self.dial_RR.setMinimum(10)
        self.dial_RR.setMaximum(30)

        self.gridLayout_2.addWidget(self.dial_RR, 2, 0, 1, 1)

        self.lcdNumber_AF = QLCDNumber(self.conf1)
        self.lcdNumber_AF.setObjectName(u"lcdNumber_AF")
        self.lcdNumber_AF.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_AF, 1, 2, 1, 1)

        self.lcdNumber_RR = QLCDNumber(self.conf1)
        self.lcdNumber_RR.setObjectName(u"lcdNumber_RR")
        self.lcdNumber_RR.setMinimumSize(QSize(0, 35))
        self.lcdNumber_RR.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_RR, 1, 0, 1, 1)

        self.dial_FIO2 = QDial(self.conf1)
        self.dial_FIO2.setObjectName(u"dial_FIO2")
        self.dial_FIO2.setMaximumSize(QSize(16777215, 60))
        self.dial_FIO2.setMinimum(23)
        self.dial_FIO2.setMaximum(100)

        self.gridLayout_2.addWidget(self.dial_FIO2, 2, 6, 1, 1)

        self.dial_VT = QDial(self.conf1)
        self.dial_VT.setObjectName(u"dial_VT")
        self.dial_VT.setMaximumSize(QSize(16777215, 60))
        self.dial_VT.setMinimum(200)
        self.dial_VT.setMaximum(1000)
        self.dial_VT.setSingleStep(100)
        self.dial_VT.setPageStep(100)

        self.gridLayout_2.addWidget(self.dial_VT, 2, 5, 1, 1)

        self.label_14 = QLabel(self.conf1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_18 = QLabel(self.conf1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_18, 0, 6, 1, 1)

        self.lcdNumber_PEEP = QLCDNumber(self.conf1)
        self.lcdNumber_PEEP.setObjectName(u"lcdNumber_PEEP")
        self.lcdNumber_PEEP.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_PEEP, 1, 4, 1, 1)

        self.dial_IE = QDial(self.conf1)
        self.dial_IE.setObjectName(u"dial_IE")
        self.dial_IE.setMaximumSize(QSize(16777215, 60))
        self.dial_IE.setMinimum(1)
        self.dial_IE.setMaximum(5)

        self.gridLayout_2.addWidget(self.dial_IE, 2, 1, 1, 1)

        self.dial_AF = QDial(self.conf1)
        self.dial_AF.setObjectName(u"dial_AF")
        self.dial_AF.setMaximumSize(QSize(16777215, 60))
        self.dial_AF.setMinimum(5)
        self.dial_AF.setMaximum(15)

        self.gridLayout_2.addWidget(self.dial_AF, 2, 2, 1, 1)

        self.label_15 = QLabel(self.conf1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 1)

        self.lcdNumber_IE = QLCDNumber(self.conf1)
        self.lcdNumber_IE.setObjectName(u"lcdNumber_IE")
        self.lcdNumber_IE.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_IE, 1, 1, 1, 1)

        self.lcdNumber_FIO2 = QLCDNumber(self.conf1)
        self.lcdNumber_FIO2.setObjectName(u"lcdNumber_FIO2")
        self.lcdNumber_FIO2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_FIO2, 1, 6, 1, 1)

        self.label_19 = QLabel(self.conf1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 0, 7, 1, 1)

        self.lcdNumber_PT = QLCDNumber(self.conf1)
        self.lcdNumber_PT.setObjectName(u"lcdNumber_PT")
        self.lcdNumber_PT.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_PT, 1, 7, 1, 1)

        self.dial_PT = QDial(self.conf1)
        self.dial_PT.setObjectName(u"dial_PT")
        self.dial_PT.setMaximumSize(QSize(16777215, 60))
        self.dial_PT.setMinimum(1)
        self.dial_PT.setMaximum(10)

        self.gridLayout_2.addWidget(self.dial_PT, 2, 7, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.opcionesTabWidget.addTab(self.conf1, "")
        self.conf2 = QWidget()
        self.conf2.setObjectName(u"conf2")
        self.verticalLayout_3 = QVBoxLayout(self.conf2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_maxp = QSpinBox(self.conf2)
        self.spinBox_maxp.setObjectName(u"spinBox_maxp")

        self.gridLayout.addWidget(self.spinBox_maxp, 1, 1, 1, 1)

        self.label = QLabel(self.conf2)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_5 = QLabel(self.conf2)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.conf2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.conf2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.conf2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.spinBox_minp = QSpinBox(self.conf2)
        self.spinBox_minp.setObjectName(u"spinBox_minp")

        self.gridLayout.addWidget(self.spinBox_minp, 2, 1, 1, 1)

        self.spinBox_minvm = QSpinBox(self.conf2)
        self.spinBox_minvm.setObjectName(u"spinBox_minvm")

        self.gridLayout.addWidget(self.spinBox_minvm, 0, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.opcionesTabWidget.addTab(self.conf2, "")

        self.verticalLayout_2.addWidget(self.opcionesTabWidget, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.tabWidget.addTab(self.main, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dial_RR.valueChanged.connect(self.lcdNumber_RR.display)
        self.dial_PIP.valueChanged.connect(self.lcdNumber_PIP.display)
        self.dial_PEEP.valueChanged.connect(self.lcdNumber_PEEP.display)
        self.dial_VT.valueChanged.connect(self.lcdNumber_VT.display)
        self.dial_FIO2.valueChanged.connect(self.lcdNumber_FIO2.display)
        self.dial_PT.valueChanged.connect(self.lcdNumber_PT.display)

        self.tabWidget.setCurrentIndex(0)
        self.opcionesTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"RR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Compliance", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vt", None))
#if QT_CONFIG(whatsthis)
        self.label_RR.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hello</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_RR.setText(QCoreApplication.translate("MainWindow", u"RR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"VT", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PEEP", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"IE", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"AirFlow", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"FiO2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PIP", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"PT", None))
        self.opcionesTabWidget.setTabText(self.opcionesTabWidget.indexOf(self.conf1), QCoreApplication.translate("MainWindow", u"1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Volumen-Minuto minimo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Presion maxima", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Modo", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CPAP", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CMV", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"PCV", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"PSV", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Presion minima", None))
        self.opcionesTabWidget.setTabText(self.opcionesTabWidget.indexOf(self.conf2), QCoreApplication.translate("MainWindow", u"2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("MainWindow", u"Principal", None))
    # retranslateUi

