import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np
from functools import lru_cache


@lru_cache(None)
def get_data():
    ef_data = json.loads(ExcelFile('308.xlsx').to_json())
    return ef_data


def repr_data(ef_data):
    for d in ef_data.keys():
        print(d, ef_data[d])


def plot_1(ef):
    b1 = np.array(ef['B, мТл'])
    u1 = np.array(ef['UH, мВ'])
    b2 = np.array(ef['B, мТл(1)'])
    u2 = np.array(ef['UH, мВ(2)']) * -1
    b3 = np.array(ef['B, мТл(2)'])
    u3 = np.array(ef['UH, мВ(3)'])
    b4 = np.array(ef['B, мТл(3)'])
    u4 = np.array(ef['UH, мВ(4)'])
    b5 = np.array(ef['B, мТл(4)'])
    u5 = np.array(ef['UH, мВ(5)'])
    pd1 = PlotData(b1, u1, label='5mA')
    pd1.approximate(Linear(), repr_equation=True)
    pd2 = PlotData(b2, u2, label='-5mA')
    pd2.approximate(Linear(), repr_equation=True)
    pd3 = PlotData(b3, u3, label='10mA')
    pd3.approximate(Linear(), repr_equation=True)
    pd4 = PlotData(b4, u4, label='-10mA')
    pd4.approximate(Linear(), repr_equation=True)
    pd5 = PlotData(b5, u5, label='15mA')
    pd5.approximate(Linear(), repr_equation=True)

    d = Drawer()
    ax = d.add_figure(pd1)
    d.add_subplot_to_fig(ax, pd2)
    d.add_subplot_to_fig(ax, pd3)
    d.add_subplot_to_fig(ax, pd4)
    d.add_subplot_to_fig(ax, pd5)
    d.save_pic("308_1")


def plot_2():
    pass


if __name__ == '__main__':
    ef = get_data()
    repr_data(ef)
    plot_1(ef)
