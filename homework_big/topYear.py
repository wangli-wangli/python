#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl  #用于修改x轴坐标
def topYearOuput():
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
    plt.style.use('ggplot')   #默认绘图风格很难看，替换为好看的ggplot风格
    fig = plt.figure(figsize=(8,5))   #设置图片大小
    colors1 = '#6D6D6D'  #设置图表title、text标注的颜色

    columns = ['index', 'thumb', 'name', 'star', 'time', 'area', 'score']  #设置表头
    df = pd.read_csv('maoyan_top100.csv',encoding = "utf-8",header = None,names =columns,index_col = 'index')  #打开表格

    print( df['time'])
    # 从日期中提取年份
    df['year'] = df['time'].map(lambda x:x.split('-')[0])
    print(df['year'])
    # print(df.info())
    # print(df.head())

    # 统计各年上映的电影数量
    grouped_year = df.groupby('year')
    grouped_year_amount = grouped_year.year.count()
    top_year = grouped_year_amount.sort_values(ascending = False)


    # 绘图
    top_year.plot(kind = 'bar',color = 'orangered') #颜色设置为橙红色
    for x,y in enumerate(list(top_year.values)):
        plt.text(x,y+0.1,'%s' %round(y,1),ha = 'center',color = colors1)
    plt.title('电影数量年份排名',color = colors1)
    plt.xlabel('年份(年)')
    plt.ylabel('数量(部)')

    plt.tight_layout()
    # plt.savefig('电影数量年份排名.png')

    plt.show()