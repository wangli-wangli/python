# -*- coding: utf-8 -*-
# @Author: GuoXu
# @Date:   2019-06-13 22:44:48
# @FileDescription: Description
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import Ui_MainWindow
from img2Str import file2Str

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        txt = file2Str("3.jpg")
        self.label.setText(txt)
        for name in vars(self).items():
        	if type(name[1]) == type(self.btn11):
        		eval("self." + name[0]).clicked.connect(self.buttonClick)
        	if name[0][-1] == '5' or name[0][-1] == '7':
        		# self.label.setHidden(True)
        		eval("self." + name[0]).setHidden(True)

    def buttonClick(self):
    	sender = self.sender()
    	# print(sender.objectName())
    	index = int(sender.objectName()[-1])
    	index2 = sender.objectName()[-2]
    	if index == 1:
    		if eval("self.btn" + index2 + str(index + 1)).isHidden() == True:
    			sender.setHidden(True)
    			eval("self.btn" + index2 + str(index + 1)).setHidden(False)
    	elif index == 5:
    		if eval("self.btn" + index2 + str(index - 1)).isHidden() == True:
    			sender.setHidden(True)
    			eval("self.btn" + index2 + str(index - 1)).setHidden(False)
    	elif index == 6:
    		if eval("self.btn" + index2 + str(index + 1)).isHidden() == True:
    			sender.setHidden(True)
    			eval("self.btn" + index2 + str(index + 1)).setHidden(False)
    	elif index == 7:
    		if eval("self.btn" + index2 + str(index - 1)).isHidden() == True:
    			sender.setHidden(True)
    			eval("self.btn" + index2 + str(index - 1)).setHidden(False)
    	else:
    		if eval("self.btn" + index2 + str(index - 1)).isHidden() == True:
    			sender.setHidden(True)
    			eval("self.btn" + index2 + str(index - 1)).setHidden(False)
    		elif eval("self.btn" + index2 + str(index + 1)).isHidden() == True:
    			sender.setHidden(True)
    			eval("self.btn" + index2 + str(index + 1)).setHidden(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    app.exec_()