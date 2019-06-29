#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl  #用于修改x轴坐标
def topCountOuput():
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
    plt.style.use('ggplot')   #默认绘图风格很难看，替换为好看的ggplot风格
    fig = plt.figure(figsize=(8,5))   #设置图片大小
    colors1 = '#6D6D6D'  #设置图表title、text标注的颜色

    columns = ['index', 'thumb', 'name', 'star', 'time', 'area', 'score']  #设置表头
    df = pd.read_csv('maoyan_top100.csv',encoding = "utf-8",header = None,names =columns,index_col = 'index')  #打开表格
    area_count = df.groupby(by = 'area').area.count().sort_values(ascending = False)

    # 绘图方法1
    area_count.plot.bar(color = '#4652B1')  #设置为蓝紫色
    pl.xticks(rotation=0)   #x轴名称太长重叠，旋转为纵向


    # 绘图方法2
    for x,y in enumerate(list(area_count.values)):
        plt.text(x,y+0.5,'%s' %round(y,1),ha = 'center',color = colors1)
    plt.title('各国/地区电影数量排名',color = colors1)
    plt.xlabel('国家/地区')
    plt.ylabel('数量(部)')
    plt.show()

