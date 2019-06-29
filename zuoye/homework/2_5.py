# -*- coding: utf-8 -*-
class Point:
    x=0
    y=0
   # p=Point()
    #def _init_(self,x,y,p):
     #   self.x=x
     #   self.y=y
     #   self.p=p 
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def setPoint(self,x,y):
        self.x=x
        self.y=y
    def getPoint(self):
        return self.x,self.y
    def add(self,p):
        return self.x+p.x,self.y+p.y
    def reduce(self,p):
        return self.x-p.x,self.y-p.y
    def multiplicate(self,p):
        return self.x*p.x,self.y*p.y
p1=Point()
p1.setPoint(2,3)
p2=Point()
p2.setPoint(3,4)
print(p2.getPoint(),"+",p1.getPoint(),"=",p2.add(p1))
print(p2.getPoint(),"-",p1.getPoint(),"=",p2.reduce(p1))
print(p2.getPoint(),"*",p1.getPoint(),"=",p2.multiplicate(p1))
