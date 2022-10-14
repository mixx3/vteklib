import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np


def plot_1(ef_data: dict):
    pd1 = PlotData(np.array(ef_data["B, мТл"]),
                   np.array(ef_data['UH, мВ']),
                   x_name="B, мТл",
                   y_name='UH, мВ',
                   title="Зависимость ЭДС Холла от индукции магнитного поля")
    pd2 = PlotData(np.array(ef_data['B, мТл(1)']), np.array(ef_data['UH, мВ(2)']) * -1)
    pd3 = PlotData(np.array(ef_data['B, мТл(2)']), np.array(ef_data['UH, мВ(3)']))
    pd4 = PlotData(np.array(ef_data['B, мТл(3)']), np.array(ef_data['UH, мВ(4)']))
    pd5 = PlotData(np.array(ef_data['B, мТл(4)']), np.array(ef_data['UH, мВ(5)']))
    pd6 = PlotData(np.array(ef_data['B, мТл(5)']), np.array(ef_data['UH, мВ(6)']))
    d = Drawer()
    ax = d.add_figure(pd1)
    pd1.approximate(Linear(), repr_equation=True)
    pd2.approximate(Linear(), repr_equation=True)
    pd3.approximate(Linear(), repr_equation=True)
    pd4.approximate(Linear(), repr_equation=True)
    pd5.approximate(Linear(), repr_equation=True)
    pd6.approximate(Linear(), repr_equation=True)
    d.add_subplot_to_fig(ax, pd2)
    d.add_subplot_to_fig(ax, pd3)
    d.add_subplot_to_fig(ax, pd4)
    d.add_subplot_to_fig(ax, pd5)
    d.add_subplot_to_fig(ax, pd6)
    d.save_pic('308')


if __name__ == '__main__':
    ef_data = json.loads(ExcelFile('308.xlsx').to_json())
    print(ef_data)
    plot_1(ef_data)
