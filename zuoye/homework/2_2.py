# -*- coding: utf-8 -*-

"""
Created on Sat May 18 17:56:25 2019

@author: lenovo
"""
import abc
import math
class graphics(metaclass=abc.ABCMeta):
    @abc.abstractmethod  #抽象方法
    def CalculateArea(self):#计算面积
        pass

    def CalculateVolume(self):#计算体积
        pass
    def Calculatelength(self):#计算周长
        pass
class point:
    x=0.0
    y=0.0
    def _init_(self,x,y):
        self.x=x
        self.y=y
    #坐标获取及设置方法、显示方法等；
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def showPoint(self):
       #print("圆心位置为("+str(self.getX())+","+str(self.y)+")")
       print("圆心位置:(",self.getX(),",",self.getY(),")")
    def setXY(self,x,y):
        self.x=x
        self.y=y
class circle(point):
    #以点类为基类派生圆类，增加表示半径的数据成员，半径获取及设置方法，重载显示函数，并可计算周长和面积等；
    radius=0.0#半径
    x=0.0
    y=0.0
    def _init_(self,x,y,radius):
         super()._init_(x,y)
         self.radius=radius
    def getRadius(self):
        return self.radius
    def setCircle(self,radius,x,y):
        super().setXY(x,y)
        self.radius=radius
    def showCircle(self):
         super().showPoint()
         print("半径为",self.radius)
    def CalculateArea(self):#计算面积
        return math.pi*(self.radius**2)
    def Calculatelength(self):#计算周长
        return math.pi*self.radius*2
#以圆类为基础派生球类、圆柱类、圆锥类；要求派生类球、圆柱、圆锥中都含有输入和输出显示方法；并可计算体积、面积。
class ball(circle,graphics):
     radius=0.0#半径
     x=0.0
     y=0.0
     def _init_(self,x,y,radius):
          super()._init_(x,y,radius)
     def setBall(self,radius,x,y):
        super().setCircle(radius,x,y)
     def showBall(self):
         print("球")
         super().showCircle()
         print("面积为",self.CalculateArea())
         print("体积为",self.CalculateVolume())
     def CalculateArea(self):#计算面积
        return math.pi*4*(self.radius**2)

     def CalculateVolume(self):#计算体积
          return (4*math.pi*(self.radius**3))/3
class cylindrical(circle,graphics):#圆柱
     radius=0.0#半径
     x=0.0
     y=0.0
     h=0.0#圆柱的高
     def _init_(self,x,y,radius,h):
          super()._init_(x,y,radius)
          self.h=h
     def setCylindrical(self,radius,x,y,h):
        super().setCircle(radius,x,y)
        self.h=h
     def showCylindrical(self):
         print("圆柱")
         super().showCircle()
         print("面积为",self.CalculateArea())
         print("体积为",self.CalculateVolume())
     def CalculateArea(self):#计算面积
        return 2*super().CalculateArea()+self.h*super().Calculatelength()

     def CalculateVolume(self):#计算体积
          return math.pi*(self.radius**2)*self.h
class cone(circle,graphics):#圆柱
     radius=0.0#半径
     x=0.0
     y=0.0
     h=0.0#圆柱的高
     def _init_(self,x,y,radius,h):
          super()._init_(x,y,radius)
          self.h=h
     def setCone(self,radius,x,y,h):
        super().setCircle(radius,x,y)
        self.h=h
     def showCone(self):
         print("圆锥")
         super().showCircle()
         print("面积为",self.CalculateArea())
         print("体积为",self.CalculateVolume())
     def CalculateArea(self):#计算面积
        return math.pi*self.radius*self.h+math.pi*(self.radius**2)

     def CalculateVolume(self):#计算体积
          return (math.pi*(self.radius**2)*self.h)/3
ball=ball()
ball.setBall(2,5,4)
ball.showBall()
c1=cylindrical()
c1.setCylindrical(3,4,5,3)
c1.showCylindrical()
c2=cone()
c2.setCone(2,3,5,5)
c2.showCone()


    
       
     
    
    
    


