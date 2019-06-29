# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:37:59 2019

@author: lenovo
"""

class Teacher():
   
    worktime=0.0#工作时间
    birthday=' '#出生年月
    title=' '#职称
    name='  '
    sex=' '
    wage1=0.0#固定工资
    wage2=0.0#课时补贴
  
    def _init_(self,name,sex,birthday,title,worktime):
        self.name=name
        self.sex=sex
        self.worktime=worktime
        if title=="教授":
          wage1=5000
          wage2=50
        elif title=="副教授":
          wage1=3000
          wage2=30
        elif title=="讲师":
          wage1=2000
          wage2=20
    def input(self,name,sex,birthday,title,worktime):
        self.name=name
        self.sex=sex
        self.worktime=worktime
        self.birthday=birthday
        self.title=title
        self.worktime=worktime
        if title=="教授":
          self.wage1=5000
          self.wage2=50
        elif title=="副教授":
          self.wage1=3000
          self.wage2=30
        elif title=="讲师":
          self.wage1=2000
          self.wage2=20
    def output(self):
        print("姓名：",self.name)
        print("性别：",self.sex)
        print("出生年月",self.birthday)
        print("职称",self.title)
        print("工作量",self.worktime)
        print("工资",self.wage1+(self.wage2*self.worktime))
t1=Teacher()
t1.input("小明","男","1882-12-23","教授",23)
t1.output()
print()
t2=Teacher()
t2.input("小刚","男","1882-12-23","副教授",23)
t2.output()
print()
t3=Teacher()
t3.input("小强","男","1882-12-23","讲师",23)
t3.output()
       
