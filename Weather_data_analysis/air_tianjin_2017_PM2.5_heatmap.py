import datetime
import numpy as np
import pandas as pd
from pyecharts import HeatMap

df = pd.read_csv('air_tianjin_2017.csv', header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])
v1 = ["{}".format(int(i)) for i in np.array(df['PM'])]

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)

data = [[str(begin + datetime.timedelta(days=i)), v1[i]] for i in range((end - begin).days + 1)]
heatmap = HeatMap("2017年天津PM2.5指数日历图", title_pos='40%', title_top='10', width=800, height=400)
heatmap.add(
    "",
    data,
    is_calendar_heatmap=True,
    visual_text_color="#000",
    visual_range_text=["", ""],
    visual_range=[0, 300],
    calendar_cell_size=["auto", 30],
    is_visualmap=True,
    calendar_date_range="2017",
    visual_orient="horizontal",
    visual_pos="26%",
    visual_top="70%",
    is_piecewise=True,
    visual_split_number=6,
)
heatmap.render('2017年天津PM2.5指数日历图.html')