from django.db import models

# 类3
class Article(models.Model):#若没有设置主键，数据库中会自动增加id主键属性
    title=models.CharField(max_length=32,default='title')
    content=models.TextField(null=True)
    pub_time=models.DateTimeField(auto_now=True)#属性pub_time为现在的时间

def __str__(self):#在
         return  self.title


