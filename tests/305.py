import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np


def plot_1():
    x = """20,50825124
19,55332158
20,09899567
22,32716487
20,91750681
12,64144977
5,502213747
2,864788976"""
    y = """2,217703704
2,217703704
2,242074074
2,315185185
2,315185185
1,99837037
1,389111111
0,7067407407"""
    pd = PlotData(
        x,
        y,
        title="Кривая намагниченности",
        x_name="Hs, А/м",
        y_name="Bs, Тл",
        label="B(H)",
    )
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("305")


def plot_2():
    t = """25
30
35
40
45
50
55
60
65
70
75
80
86
90
94"""
    b = """1,663277778
1,626722222
1,443944444
1,498777778
1,626722222
1,425666667
1,370833333
1,297722222
1,261166667
1,188055556
1,169777778
1,078388889
0,9687222222
0,8773333333
0,7493888889"""
    pd = PlotData(
        t,
        b,
        title="Зависимость магнитной индукции ферромагнетика от температуры",
        x_name="T, c",
        y_name="Bs, Тл",
        label="Bs(T)",
    )
    pd.approximate(Linear(), repr_equation=True)
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("305_2")


if __name__ == "__main__":
    plot_2()
