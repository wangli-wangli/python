# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:48:59 2019

@author: lenovo
"""

class Cexception(Exception):    # 创建一个新的exception类来抛出自己的异常。
    # 异常应该继承自 Exception 类，包括直接继承，或者间接继承
    def __init__(self, errorinfor):
        self.error = errorinfor
       
    def __str__(self):
        return self.error
class Date():
    year=0
    month=0
    day=0
    def runnian(year):
        if (year%4==0&year%100!=0)|year%400==0:
            return True
        else:
            return False
            
    def _init_(self,year,month,day):
        iss=False
        if type(year)!=int:
            raise Cexception("year 不正确")
        if type(month)!=int:
            raise Cexception("month 不正确")
        if type(day)!=int:
            raise Cexception("day 不正确")
        a={1,3,5,7,8,10,12}
        b={4,6,9,11}
        if year>=10000|year<1000:
            raise Cexception("year 不正确")
        else:
            if month>12|month<=0:
                raise Cexception("month 不正确")
            else:
                if (month in a)&(day>31|day<=0):
                     raise Cexception("day 不正确")
                elif (month in b)&(day>30|day<=0):
                     raise Cexception("day 不正确")
                elif month==2:
                    if (runnian(year)==False)&(day > 28 |day <= 0):
                        raise Cexception("day 不正确")
                    elif  runnian(year)==True&(day > 29 | day <= 0):
                        raise Cexception("day 不正确")
                    else:
                        iss=True
                else:
                    iss=True
        if iss==True:
           self.year=year
           self.month=month
           self.day=fay
    def setDate(self,year,month,day):
        iss=False
        if type(year)!=int:
            raise Cexception("year 不正确")
        if type(month)!=int:
            raise Cexception("month 不正确")
        if type(day)!=int:
            raise Cexception("day 不正确")
        a={1,3,5,7,8,10,12}
        b={4,6,9,11}
        if year>=10000|year<1000:
            raise Cexception("year 不正确")
        else:
            if month>12|month<=0:
                raise Cexception("month 不正确")
            else:
                if (month in a)&(day>31|day<=0):
                     raise Cexception("day 不正确")
                elif (month in b)&(day>30|day<=0):
                     raise Cexception("day 不正确")
                elif month==2:
                    if (runnian(year)==False)&(day > 28 |day <= 0):
                        raise Cexception("day 不正确")
                    elif  runnian(year)==True&(day > 29 | day <= 0):
                        raise Cexception("day 不正确")
                    else:
                        iss=True
                else:
                    iss=True
        if iss==True:
           self.year=year
           self.month=month
           self.day=fay
    def getDate():
           if self.year!=0&self.month!=0&self.day!=0:
               print(year,"年",month,"月",day,"日")
d1=Date()
d1.setDate('1221',12,1)
d1.getDate()
d2=Date()
d2.setDate(-1222,12,1)
d2.getDate()
d2=Date()
d2.setDate(2008,2,28)
d2.getDate()

               

     
                    
                        
                    
                    
        
        