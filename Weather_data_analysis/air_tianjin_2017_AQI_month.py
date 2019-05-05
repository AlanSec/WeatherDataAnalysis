import numpy as np
import pandas as pd
from pyecharts import Line

df = pd.read_csv('air_tianjin_2017.csv', header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])

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

attr = ["{}".format(str(i) + '月') for i in range(1, 13)]
v1 = np.array(month_com_last['mean'])
v1 = ["{}".format(int(i)) for i in v1]

line = Line("2017年天津月均AQI走势图", title_pos='center', title_top='18', width=800, height=400)
line.add("", attr, v1, mark_point=["max", "min"])
line.render("2017年天津月均AQI走势图.html")
