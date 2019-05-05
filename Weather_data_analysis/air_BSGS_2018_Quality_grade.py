import numpy as np
import pandas as pd
from pyecharts import Pie, Grid

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
v = []
attrs = []
for i in range(4):
    filename = 'air_' + citys[i] + '_2018.csv'
    df = pd.read_csv(filename, header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])

    rank_message = df.groupby(['Quality_grade'])
    rank_com = rank_message['Quality_grade'].agg(['count'])
    rank_com.reset_index(inplace=True)
    rank_com_last = rank_com.sort_values('count', ascending=False)

    attr = rank_com_last['Quality_grade']
    attr = np.array(rank_com_last['Quality_grade'])
    attrs.append(attr)
    v1 = rank_com_last['count']
    v1 = np.array(rank_com_last['count'])
    v.append(v1)

pie1 = Pie("北京", title_pos="28%", title_top="24%")
pie1.add("", attrs[0], v[0], radius=[25, 40], center=[30, 27], legend_pos="27%", legend_top="51%", legend_orient="horizontal",)

pie2 = Pie("上海", title_pos="58%", title_top="24%")
pie2.add("", attrs[1], v[1], radius=[25, 40], center=[60, 27], is_label_show=False, is_legend_show=False)

pie3 = Pie("广州", title_pos='28%', title_top='77%')
pie3.add("", attrs[2], v[2], radius=[25, 40], center=[30, 80], is_label_show=False, is_legend_show=False)

pie4 = Pie("深圳", title_pos='58%', title_top='77%')
pie4.add("", attrs[3], v[3], radius=[25, 40], center=[60, 80], is_label_show=False, is_legend_show=False)

grid = Grid("2018年北上广深全年空气质量情况", width=1200)
grid.add(pie1)
grid.add(pie2)
grid.add(pie3)
grid.add(pie4)
grid.render('2018年北上广深全年空气质量情况.html')
