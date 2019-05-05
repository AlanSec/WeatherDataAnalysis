import numpy as np
import pandas as pd
from pyecharts import Line

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
v = []
for i in range(4):
    filename = 'air_' + citys[i] + '_2018.csv'
    df = pd.read_csv(filename, header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])

    dom = df[['Date', 'AQI']]
    list1 = []
    for j in dom['Date']:
        time = j.split('-')[1]
        list1.append(time)
    df['month'] = list1

    month_message = df.groupby(['month'])
    month_com = month_message['AQI'].agg(['mean'])
    month_com.reset_index(inplace=True)
    month_com_last = month_com.sort_index()

    v1 = np.array(month_com_last['mean'])
    v1 = ["{}".format(int(i)) for i in v1]
    v.append(v1)

attr = ["{}".format(str(i) + '月') for i in range(1, 12)]

line = Line("2018年北上广深AQI全年走势图", title_pos='center', title_top='0', width=800, height=400)
line.add("北京", attr, v[0], line_color='red', legend_top='8%')
line.add("上海", attr, v[1], line_color='purple', legend_top='8%')
line.add("广州", attr, v[2], line_color='blue', legend_top='8%')
line.add("深圳", attr, v[3], line_color='orange', legend_top='8%')
line.render("2018年北上广深AQI全年走势图.html")
