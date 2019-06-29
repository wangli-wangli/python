# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:30:01 2019

@author: lenovo
"""
class People:
    name='  '
    sex=' '
    age=0
    def _init_(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
class Student(People):
    number=' '
    time=' '
    score=' '
    def _init_(self,name,sex,age,number,time,score):
        super()._init_(name,sex,age)
        self.number=number
        self.time=time
        self.score=score
class Teacher(People):
    position=' '
    department=' '
    worktime=' '
    def _init_(self,name,sex,age,position,department,worktime):
        super()._init_(name,sex,age)
        self.position=position
        self.department=department
        self.worktime=worktime
    def output(self):
        print("姓名：",self.name)
        print("性别：",self.sex)
        print("年龄：",self.age)
        print("职位：",self.position)
        print("部门：",self.department)
        print("工作时间：",self.worktime)
class GradOnWork(People):
    position=' '#职位
    department=' '#部门
    worktime=' '#工作时间
    number=' '#学号
    time=' '#入学时间
    score=' '#成绩
    def _init_(self,name,sex,age,position,department,worktime,number,time,score):
        super()._init_(name,sex,age)
        self.position=position
        self.department=department
        self.worktime=worktime
        self.number=number
        self.time=time
        self.score=score
    def output(self):
        print("姓名：",self.name)
        print("性别：",self.sex)
        print("年龄：",self.age)
        print("职位：",self.position)
        print("部门：",self.department)
        print("工作时间：",self.worktime)
        print("学号：",self.number)
        print("入学时间：",self.time)
        print("入学成绩：",self.score)
class Graduate(Student):
    directionOfResearch=' '
    teacher=Teacher()
    def _init_(self,name,sex,age,number,time,score, directionOfResearch,teacher):
        super()._init_(name,sex,age,number,time,score)
        self.directionOfResearch=directionOfResearch
        self.teacher=teacher
    def output(self):
        print("姓名：",self.name)
        print("性别：",self.sex)
        print("年龄：",self.age)
        print("学号：",self.number)
        print("入学时间：",self.time)
        print("入学成绩：",self.score)
        print("研究方向：",self.directionOfResearch)
        print("指导老师：")
        self.teacher.output()
g=Graduate()
g.name="王莉"
g.sex="女"
g.age=21
g.number="20163623"
g.time="2017-01-02"
g.score="43"
g.directionOfResearch="中国历史"

t=Teacher()
t.name="小明"
t.age=21
t.position="讲师"
t.sex="男"
t.worktime="2002-02-21"
t.position="普通人"
t.department="软工"
g.teacher=t
g.output()

h=GradOnWork()
h.name="小刚"
h.age=21
h.position="讲师"
h.sex="男"
h.worktime="2002-02-21"
h.position="普通人"
h.department="软工"
h.number="20149323"
h.time="2016-12-12"
h.score="243"
h.output()




    
