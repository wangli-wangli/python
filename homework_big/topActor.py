#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl  #用于修改x轴坐标
def topActorOutnput():
        plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
        plt.style.use('ggplot')   #默认绘图风格很难看，替换为好看的ggplot风格
        fig = plt.figure(figsize=(8,5))   #设置图片大小
        colors1 = '#6D6D6D'  #设置图表title、text标注的颜色

        columns = ['index', 'thumb', 'name', 'star', 'time', 'area', 'score']  #设置表头
        df = pd.read_csv('maoyan_top100.csv',encoding = "utf-8",header = None,names =columns,index_col = 'index')  #打开表格

        #表中的演员位于同一列，用逗号分割符隔开。需进行分割然后全部提取到list中
        starlist  =  []
        star_total  =  df.star
        for  i  in  df.star.str.replace('  ','').str.split(','):
                starlist.extend(i)

        starall  =  set(starlist)

        starall2  =  {}
        for  i  in  starall:
                if  starlist.count(i)>1:
                        #  筛选出电影数量超过1部的演员
                        starall2[i]  =  starlist.count(i)

        starall2  =  sorted(starall2.items(),key  =  lambda  starlist:starlist[1]  ,reverse  =  True)

        starall2  =  dict(starall2[:10])    #将元组转为字典格式

        #  绘图
        x_star  =  list(starall2.keys())            #x轴坐标
        y_star  =  list(starall2.values())        #y轴坐标

        plt.bar(range(10),y_star,tick_label  =  x_star)
        pl.xticks(rotation  =  270)
        for  x,y  in  enumerate(y_star):
                plt.text(x,y+0.1,'%s'  %round(y,1),ha  =  'center',color  =  colors1)

        plt.title('演员电影作品数量排名',color  =  colors1)
        plt.xlabel('演员')
        plt.ylabel('数量(部)')
        plt.tight_layout()
        plt.show()
