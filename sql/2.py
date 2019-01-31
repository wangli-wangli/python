# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Product(Base):
    __tablename__='Product'
    id = Column(String(20), primary_key=True)  # 字段
    name = Column(String(20))  # 字段
    type= Column(String(20))  # 字段
    
engine = create_engine('mssql+pymssql://sa:root@localhost:1433/world')#初始化数据库连接
DBSession=sessionmaker(bind=engine)#创建DBsesson类型
Base.metadata.create_all(engine)#创建表结构

#向数据库写入
session=DBSession()#创建session对象
new_user=Product(id='1233445',name='宁夏一日游',type='景+酒')#创建新Product对象
session.add(new_user)#添加到session
session.commit()#提交即保存到数据库


#创建Query查询。filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
student=session.query(Product).filter(Product.id=='1233445').one()
#打印对象的name,class_name属性
print('name:',student.name)
print('class_name：',student.type)


#查询并更新数据
session.query(Product).filter(Product.id=='1233445').update({Product.name:"宁夏中卫一日游"})
session.commit()


#查询并删除数据
#session.query(Product).filter(Product.id='1233445').delete()
session.commit()
session.close()
