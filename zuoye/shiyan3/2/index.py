# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import Ui_MainWindow
from random import randint

class MyMainWindow(QMainWindow, Ui_MainWindow):
	questionNum = 0
	currentNum = 0
	info = ""
	def __init__(self):
		super(MyMainWindow, self).__init__()
		self.setupUi(self)
		self.timer = QTimer(self) #初始化一个定时器
		self.timer.timeout.connect(self.timePicker)
		self.pushButton.clicked.connect(self.start)
		self.initAbs()

	def initAbs(self):
		for name in vars(self).items():
			if name[0] == 'pushButton':
				continue
			if type(name[1]) == type(self.btn11):
				eval("self." + name[0]).clicked.connect(self.buttonClick)
				if name[0][-1] == '5' or name[0][-1] == '7':
					# self.label.setHidden(True)
					eval("self." + name[0]).setHidden(True)
				else:
					eval("self." + name[0]).setHidden(False)

	def timePicker(self):
		currentTime = self.label_4.text()
		if currentTime == "00:00":
			self.end("timeout")
		snum = int(currentTime.split(":")[0]) * 60 + int(currentTime.split(":")[1])
		# print(snum)
		snum -= 1
		msnum = "0" + str(snum // 60) + ":" + ("0" if snum % 60 < 10 else "") + str(snum % 60)
		# print(msnum)
		self.label_4.setText(msnum)
	def start(self):
		name = self.lineEdit.text()
		num = self.comboBox.currentText()
		time = self.comboBox_2.currentText()
		self.label_11.setText(num)
		self.questionNum = int(num)
		self.label_4.setText("0" + time + ":00")
		self.timer.start(1000)
		self.lineEdit.setDisabled(True)
		self.comboBox.deleteLater()
		self.label_7.deleteLater()
		self.comboBox_2.setHidden(True)
		self.label_9.deleteLater()
		self.label_8.setGeometry(440 * 2, 110 * 2, 100 * 2, 22 * 2)
		self.label_8.setText(self.getEquation() + " = ?")
		# self.label_8.setText("1 + 2 = ?")
		# self.label_6.setText("第一题：")
		self.pushButton.setText("提交")
		self.pushButton.disconnect()
		self.pushButton.clicked.connect(self.judge)
		# print(name, num, time)

	def getEquation(self):
		if self.currentNum == self.questionNum:
			self.end("havenoquestion")
		self.currentNum += 1
		self.label_6.setText("第{}题：".format(self.currentNum))
		left = randint(0, 100)
		right = randint(0, 100)
		oper = randint(0, 1)
		if oper == 0:
			return str(left) + " + " + str(right)
		else:
			while True:
				if left >= right:
					break
				else:
					right = randint(0, 100)
			return str(left) + " - " + str(right)

	# 获取算盘上的得数
	def getAbacusNum(self):
		num = ""
		for i in range(1, 6):
			num = str(self.getOneColumn(i)) + num
		return int(num)

	# 获取某一列的值
	def getOneColumn(self, num):
		t = 0
		for i in range(1, 6):
			if eval("self.btn" + str(num) + str(i)).isHidden() == True:
				t = 5 - i
				break
		if eval("self.btn" + str(num) + "6").isHidden() == True:
			t += 5
		else:
			pass
		return t

	def judge(self):
		equation = self.label_8.text()[:-3]
		self.info += str(self.currentNum) + ". " + self.label_8.text() + "；您的答案：" + str(self.getAbacusNum()) + "；正确答案：" + str(eval(equation)) + "；"
		self.label_13.setText(str(int(self.label_13.text()) + 1))
		# print(self.getAbacusNum())
		# print(eval(equation))
		if int(self.getAbacusNum()) == eval(equation):
			self.info += "正确！\n"
			self.label_15.setText(str(int(self.label_15.text()) + 1))
			self.timer.stop()
			message = QMessageBox()
			message.setWindowTitle('恭喜')
			message.setText("回答正确！")
			# 自定义对话框按钮：
			# 必须要指定按钮的 Role 属性，不能忘
			message.addButton("下一题", QMessageBox.AcceptRole)
			reply = message.exec_()
			if reply == 0:
				self.initAbs()
				self.timer.start()
				self.label_8.setText(self.getEquation() + " = ?")
			#     self.now_grade.setText(str(int(self.now_grade.text()) + int(self.left_time.text())))
			#     self.now_rightcount.setText(str(int(self.now_rightcount.text()) + 1))
			#     self.left_time.setText(str(GAMETIME))
			#     self.equationLabel.setText("")
			#     Refresh(self)
		else:
			self.info += "错误！\n"
			self.timer.stop()
			message = QMessageBox()
			message.setWindowTitle('提示')
			message.setText("回答错误")
			# 自定义对话框按钮：
			# 必须要指定按钮的 Role 属性，不能忘
			message.addButton("下一题", QMessageBox.AcceptRole)
			reply = message.exec_()
			if reply == 0:
				self.initAbs()
				self.timer.start()
				self.label_8.setText(self.getEquation() + " = ?")
		print(self.info)
	def end(self, method):
		self.timer.stop()
		name = self.lineEdit.text()
		result = "用户名：" + name + "\n"
		result += "题目数量：" + str(self.questionNum) + "\n"
		result += "已答题数量：" + self.label_13.text() + "\n"
		result += "答对数量：" + self.label_15.text() + "\n"
		currentTime = self.label_4.text()
		snum = int(currentTime.split(":")[0]) * 60 + int(currentTime.split(":")[1])
		totalTime = int(self.comboBox_2.currentText()) * 60
		useTime = totalTime - snum
		msnum = "0" + str(useTime // 60) + ":" + ("0" if useTime % 60 < 10 else "") + str(useTime % 60)
		result += "用时：" + msnum + "\n"
		result += "得分：" + self.label_15.text() + "\n"
		result += "答题详情如下：\n" + self.info
		if method == "timeout":
			message = QMessageBox()
			message.setWindowTitle('游戏结束')
			result = "时间到！\n" + result
			message.setText(result)
			# 自定义对话框按钮：
			# 必须要指定按钮的 Role 属性，不能忘
			message.addButton("确定", QMessageBox.AcceptRole)
			reply = message.exec_()
			if reply == 0:
				sys.exit()
		elif method == "havenoquestion":
			message = QMessageBox()
			message.setWindowTitle('游戏结束')
			result = "回答完毕！\n" + result
			message.setText(result)
			# 自定义对话框按钮：
			# 必须要指定按钮的 Role 属性，不能忘
			message.addButton("确定", QMessageBox.AcceptRole)
			reply = message.exec_()
			if reply == 0:
				sys.exit()
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