import pandas as pd
from pyecharts import Boxplot

df = pd.read_csv('air_tianjin_2017.csv', header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])

dom = df[['Date', 'AQI']]
data = [[], [], [], []]
dom1, dom2, dom3, dom4 = data
for i, j in zip(dom['Date'], dom['AQI']):
    time = i.split('-')[1]
    if time in ['01', '02', '03']:
        dom1.append(j)
    elif time in ['04', '05', '06']:
        dom2.append(j)
    elif time in ['07', '08', '09']:
        dom3.append(j)
    else:
        dom4.append(j)

boxplot = Boxplot("2017年天津季度AQI箱形图", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['第一季度', '第二季度', '第三季度', '第四季度']
y_axis = [dom1, dom2, dom3, dom4]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render("2017年天津季度AQI箱形图.html")
