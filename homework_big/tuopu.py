import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl  #用于修改x轴坐标
def tuopuOutput():
        colors1 = '#6D6D6D'
        plt.title('前30部电影与演员之间的关系', color=colors1)
        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.sans-serif'] = ['SimHei']

        columns = ['index', 'thumb', 'name', 'star', 'time', 'area', 'score']  #设置表头
        df = pd.read_csv('maoyan_top100.csv',encoding = "utf-8",header = None,names =columns,index_col = 'index')  #打开表格
        starlist  =  []
        namelist=[]
        for  i  in  df.star.str.replace('  ','').str.split(','):
                starlist.extend(i)

        for  i  in  df.name.str.replace('  ','').str.split(','):
                namelist.extend(i)
        finallist=[]
        finallist=zip(starlist,namelist)
        final2list=[]
        i=0
        for gg in finallist:

                if i==30:
                        break
                final2list.append(gg)
                i=i+1
        #print(final2list)
        #         print(gg)
        # 定义空图
        g = nx.Graph()

        # 导入所有边，每条边分别用tuple表示
        #g.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 8), (5, 8), (3, 7)])
        g.add_edges_from(final2list,length=50)
        nx.draw(g,
                with_labels=True,
                edge_color='r',
                node_color='g',
                length=60,
                node_size=100)
        # 如果你想保存图片，去除这句的注释
        # plt.savefig('./generated_image.png')
        plt.show()