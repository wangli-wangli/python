# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570 * 2, 324 * 2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370 * 2, 10 * 2, 191 * 2, 271 * 2))
        self.label.setStyleSheet("* {\n"
"    border: 0px solid black;\n"
"    font-size: 6px;"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10 * 2, 10 * 2, 341 * 2, 271 * 2))
        self.label_2.setStyleSheet("* {\n"
"    border: 1px solid black;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10 * 2, 80 * 2, 341 * 2, 16 * 2))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn51 = QtWidgets.QPushButton(self.centralwidget)
        self.btn51.setGeometry(QtCore.QRect(20 * 2, 240 * 2, 41 * 2, 31 * 2))
        self.btn51.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn51.setText("")
        self.btn51.setObjectName("btn51")
        self.btn41 = QtWidgets.QPushButton(self.centralwidget)
        self.btn41.setGeometry(QtCore.QRect(90 * 2, 240 * 2, 41 * 2, 31 * 2))
        self.btn41.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn41.setText("")
        self.btn41.setObjectName("btn41")
        self.btn31 = QtWidgets.QPushButton(self.centralwidget)
        self.btn31.setGeometry(QtCore.QRect(160 * 2, 240 * 2, 41 * 2, 31 * 2))
        self.btn31.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn31.setText("")
        self.btn31.setObjectName("btn31")
        self.btn21 = QtWidgets.QPushButton(self.centralwidget)
        self.btn21.setGeometry(QtCore.QRect(230 * 2, 240 * 2, 41 * 2, 31 * 2))
        self.btn21.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn21.setText("")
        self.btn21.setObjectName("btn21")
        self.btn11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn11.setGeometry(QtCore.QRect(300 * 2, 240 * 2, 41 * 2, 31 * 2))
        self.btn11.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn11.setText("")
        self.btn11.setObjectName("btn11")
        self.btn52 = QtWidgets.QPushButton(self.centralwidget)
        self.btn52.setGeometry(QtCore.QRect(20 * 2, 200 * 2, 41 * 2, 31 * 2))
        self.btn52.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn52.setText("")
        self.btn52.setObjectName("btn52")
        self.btn42 = QtWidgets.QPushButton(self.centralwidget)
        self.btn42.setGeometry(QtCore.QRect(90 * 2, 200 * 2, 41 * 2, 31 * 2))
        self.btn42.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn42.setText("")
        self.btn42.setObjectName("btn42")
        self.btn32 = QtWidgets.QPushButton(self.centralwidget)
        self.btn32.setGeometry(QtCore.QRect(160 * 2, 200 * 2, 41 * 2, 31 * 2))
        self.btn32.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn32.setText("")
        self.btn32.setObjectName("btn32")
        self.btn22 = QtWidgets.QPushButton(self.centralwidget)
        self.btn22.setGeometry(QtCore.QRect(230 * 2, 200 * 2, 41 * 2, 31 * 2))
        self.btn22.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn22.setText("")
        self.btn22.setObjectName("btn22")
        self.btn12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn12.setGeometry(QtCore.QRect(300 * 2, 200 * 2, 41 * 2, 31 * 2))
        self.btn12.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn12.setText("")
        self.btn12.setObjectName("btn12")
        self.btn13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn13.setGeometry(QtCore.QRect(300 * 2, 160 * 2, 41 * 2, 31 * 2))
        self.btn13.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn13.setText("")
        self.btn13.setObjectName("btn13")
        self.btn14 = QtWidgets.QPushButton(self.centralwidget)
        self.btn14.setGeometry(QtCore.QRect(300 * 2, 124 * 2, 41 * 2, 31 * 2))
        self.btn14.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn14.setText("")
        self.btn14.setObjectName("btn14")
        self.btn16 = QtWidgets.QPushButton(self.centralwidget)
        self.btn16.setGeometry(QtCore.QRect(300 * 2, 50 * 2, 41 * 2, 31 * 2))
        self.btn16.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn16.setText("")
        self.btn16.setObjectName("btn16")
        self.btn17 = QtWidgets.QPushButton(self.centralwidget)
        self.btn17.setGeometry(QtCore.QRect(300 * 2, 13 * 2, 41 * 2, 31 * 2))
        self.btn17.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn17.setText("")
        self.btn17.setObjectName("btn17")
        self.btn15 = QtWidgets.QPushButton(self.centralwidget)
        self.btn15.setGeometry(QtCore.QRect(300 * 2, 89 * 2, 41 * 2, 31 * 2))
        self.btn15.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn15.setText("")
        self.btn15.setObjectName("btn15")
        self.btn27 = QtWidgets.QPushButton(self.centralwidget)
        self.btn27.setGeometry(QtCore.QRect(230 * 2, 13 * 2, 41 * 2, 31 * 2))
        self.btn27.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn27.setText("")
        self.btn27.setObjectName("btn27")
        self.btn26 = QtWidgets.QPushButton(self.centralwidget)
        self.btn26.setGeometry(QtCore.QRect(230 * 2, 50 * 2, 41 * 2, 31 * 2))
        self.btn26.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn26.setText("")
        self.btn26.setObjectName("btn26")
        self.btn25 = QtWidgets.QPushButton(self.centralwidget)
        self.btn25.setGeometry(QtCore.QRect(230 * 2, 90 * 2, 41 * 2, 31 * 2))
        self.btn25.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn25.setText("")
        self.btn25.setObjectName("btn25")
        self.btn24 = QtWidgets.QPushButton(self.centralwidget)
        self.btn24.setGeometry(QtCore.QRect(230 * 2, 125 * 2, 41 * 2, 31 * 2))
        self.btn24.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn24.setText("")
        self.btn24.setObjectName("btn24")
        self.btn23 = QtWidgets.QPushButton(self.centralwidget)
        self.btn23.setGeometry(QtCore.QRect(230 * 2, 160 * 2, 41 * 2, 31 * 2))
        self.btn23.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn23.setText("")
        self.btn23.setObjectName("btn23")
        self.btn44 = QtWidgets.QPushButton(self.centralwidget)
        self.btn44.setGeometry(QtCore.QRect(89 * 2, 127 * 2, 41 * 2, 31 * 2))
        self.btn44.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn44.setText("")
        self.btn44.setObjectName("btn44")
        self.btn33 = QtWidgets.QPushButton(self.centralwidget)
        self.btn33.setGeometry(QtCore.QRect(159 * 2, 161 * 2, 41 * 2, 31 * 2))
        self.btn33.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn33.setText("")
        self.btn33.setObjectName("btn33")
        self.btn43 = QtWidgets.QPushButton(self.centralwidget)
        self.btn43.setGeometry(QtCore.QRect(89 * 2, 162 * 2, 41 * 2, 31 * 2))
        self.btn43.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn43.setText("")
        self.btn43.setObjectName("btn43")
        self.btn34 = QtWidgets.QPushButton(self.centralwidget)
        self.btn34.setGeometry(QtCore.QRect(159 * 2, 126 * 2, 41 * 2, 31 * 2))
        self.btn34.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn34.setText("")
        self.btn34.setObjectName("btn34")
        self.btn47 = QtWidgets.QPushButton(self.centralwidget)
        self.btn47.setGeometry(QtCore.QRect(90 * 2, 16 * 2, 41 * 2, 31 * 2))
        self.btn47.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn47.setText("")
        self.btn47.setObjectName("btn47")
        self.btn36 = QtWidgets.QPushButton(self.centralwidget)
        self.btn36.setGeometry(QtCore.QRect(160 * 2, 50 * 2, 41 * 2, 31 * 2))
        self.btn36.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn36.setText("")
        self.btn36.setObjectName("btn36")
        self.btn46 = QtWidgets.QPushButton(self.centralwidget)
        self.btn46.setGeometry(QtCore.QRect(90 * 2, 51 * 2, 41 * 2, 31 * 2))
        self.btn46.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn46.setText("")
        self.btn46.setObjectName("btn46")
        self.btn37 = QtWidgets.QPushButton(self.centralwidget)
        self.btn37.setGeometry(QtCore.QRect(160 * 2, 15 * 2, 41 * 2, 31 * 2))
        self.btn37.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn37.setText("")
        self.btn37.setObjectName("btn37")
        self.btn45 = QtWidgets.QPushButton(self.centralwidget)
        self.btn45.setGeometry(QtCore.QRect(89 * 2, 91 * 2, 41 * 2, 31 * 2))
        self.btn45.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn45.setText("")
        self.btn45.setObjectName("btn45")
        self.btn35 = QtWidgets.QPushButton(self.centralwidget)
        self.btn35.setGeometry(QtCore.QRect(159 * 2, 90 * 2, 41 * 2, 31 * 2))
        self.btn35.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn35.setText("")
        self.btn35.setObjectName("btn35")
        self.btn53 = QtWidgets.QPushButton(self.centralwidget)
        self.btn53.setGeometry(QtCore.QRect(20 * 2, 163 * 2, 41 * 2, 31 * 2))
        self.btn53.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn53.setText("")
        self.btn53.setObjectName("btn53")
        self.btn54 = QtWidgets.QPushButton(self.centralwidget)
        self.btn54.setGeometry(QtCore.QRect(20 * 2, 128 * 2, 41 * 2, 31 * 2))
        self.btn54.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn54.setText("")
        self.btn54.setObjectName("btn54")
        self.btn56 = QtWidgets.QPushButton(self.centralwidget)
        self.btn56.setGeometry(QtCore.QRect(20 * 2, 51 * 2, 41 * 2, 31 * 2))
        self.btn56.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn56.setText("")
        self.btn56.setObjectName("btn56")
        self.btn57 = QtWidgets.QPushButton(self.centralwidget)
        self.btn57.setGeometry(QtCore.QRect(20 * 2, 16 * 2, 41 * 2, 31 * 2))
        self.btn57.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn57.setText("")
        self.btn57.setObjectName("btn57")
        self.btn55 = QtWidgets.QPushButton(self.centralwidget)
        self.btn55.setGeometry(QtCore.QRect(21 * 2, 92 * 2, 41 * 2, 31 * 2))
        self.btn55.setStyleSheet("* {\n"
"    background-color: red;\n"
"    border: 1px solid #f1f1f1;\n"
"    border-radius: 30px;\n"
"}")
        self.btn55.setText("")
        self.btn55.setObjectName("btn55")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380 * 2, 40 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440 * 2, 43 * 2, 101 * 2, 16 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380 * 2, 80 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440 * 2, 80 * 2, 91 * 2, 20 * 2))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380 * 2, 110 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440 * 2, 110 * 2, 41 * 2, 22 * 2))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(440 * 2, 140 * 2, 41 * 2, 22 * 2))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380 * 2, 140 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490 * 2, 110 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490 * 2, 140 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(380 * 2, 200 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        # 总题数
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440 * 2, 200 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(380 * 2, 230 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        # 已答题数
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(440 * 2, 230 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(380 * 2, 260 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        # 已答对数
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(440 * 2, 260 * 2, 61 * 2, 21 * 2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_11")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420 * 2, 180 * 2, 61 * 2, 21 * 2))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570 * 2, 18 * 2))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "剩余时间："))
        self.label_4.setText(_translate("MainWindow", "00:00"))
        self.label_5.setText(_translate("MainWindow", "设置名称："))
        self.label_6.setText(_translate("MainWindow", "题目数量："))
        self.label_10.setText(_translate("MainWindow", "总题数："))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "已答题数："))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "答对数："))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.comboBox.setCurrentText(_translate("MainWindow", "1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7"))
        self.label_7.setText(_translate("MainWindow", "选择时间："))
        self.label_8.setText(_translate("MainWindow", "个"))
        self.label_9.setText(_translate("MainWindow", "分钟"))
        self.pushButton.setText(_translate("MainWindow", "开始答题"))
