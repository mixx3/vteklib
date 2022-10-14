import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np
from functools import lru_cache


@lru_cache(None)
def get_data():
    ef_data = json.loads(ExcelFile('304.xlsx').to_json())
    return ef_data


def repr_data(ef_data):
    for d in ef_data.keys():
        print(d, ef_data[d])


def plot_1(ef):
    I = np.array(ef['I, А'])
    U = np.array(ef['Ux, мВ'])
    pd = PlotData(I, U, title="Завиимость Ux(I)", x_name='I, А', y_name='Ux, мВ', label='Ux(I)')
    pd.approximate(Linear(), repr_equation=True)
    d = Drawer()
    d.add_figure(pd)
    d.save_pic('304_1')


def plot_2(ef):
    x = np.array(ef['z, см(1)']) - 10
    b = np.array(ef['B, мТл(2)'])
    pd = PlotData(x,
                  b,
                  title="Зависимость индукции магнитного поля "
                        "\nна оси длинного соленоида от расстояния до торца",
                  x_name='z, см',
                  y_name='B, мТл',
                  label='B(z)'
                  )
    d = Drawer()
    d.add_figure(pd, connect_pts=True)
    d.save_pic("304_2")


def plot3(ef):
    z = np.array(ef['z, см(4)'])
    b_e = np.array(ef['B, мТл(4)'])
    b_t = np.array(ef['Bтеор, мВ'])
    pd1 = PlotData(z,
                   b_e,
                   title="Зависимость индукции магнитного поля \n"
                         "на оси короткого соленоида от расстояния до торца",
                   x_name='z, см',
                   y_name='B, мТл',
                   label='Bэксп(z)')
    pd2 = PlotData(z, b_t,title="Зависимость индукции магнитного поля \n"
                         "на оси короткого соленоида от расстояния до торца",
                   x_name='z, см',
                   y_name='B, мТл',
                   label="Bтеор(z)")
    d = Drawer()
    ax = d.add_figure(pd1, connect_pts=True)
    ax2 = d.add_subplot_to_fig(ax, pd2, connect_pts=True)
    ax2.grid()
    d.save_pic('304_3')


def plot_4(ef):
    x = np.array(ef['z, см'])
    b_e = np.array(ef['B, мТл'])
    b_t = np.array(ef['Bтеор, мТл'])
    pd1 = PlotData(x,
                   b_e,
                   title="Зависимость индукции магнитного поля \n"
                         "одной катушки Гельмгольца от расстояния",
                   x_name='x, см',
                   y_name='B, мТл',
                   label='Bэксп(x)')
    pd2 = PlotData(x, b_t,
                   title="Зависимость индукции магнитного поля \n"
                         "одной катушки Гельмгольца от расстояния",
                   x_name='x, см',
                   y_name='B, мТл',
                   label="Bтеор(x)")
    d = Drawer()
    ax = d.add_figure(pd1, connect_pts=True)
    ax2 = d.add_subplot_to_fig(ax, pd2, connect_pts=True)
    ax2.grid()
    d.save_pic("304_4")


def plot_5(ef):
    x = np.array(ef['z, см(2)'])
    b_l = np.array(ef['Bтеор, мТл(1)'])
    db_l = np.array(ef['dBтеор, мТл(1)'])
    b_r = np.array(ef['Bтеор, мТл(2)'])
    db_r = np.array(ef['dBтеор, мТл(2)'])
    b_t = np.array(ef['Bтеор, мТл(3)'])
    db_t = np.array(ef['dBтеор, мТл(3)'])
    b_e = np.array(ef['B, мТл(1)'])
    db_e = np.array(ef['dB, мТл(1)'])
    pd1 = PlotData(x, b_l, title='', label='Левая катушка', x_name='x, см', y_name='B, мТл', y_error=db_l)
    pd2 = PlotData(x, b_r, title='', label='Правая катушка', x_name='x, см', y_name='B, мТл', y_error=db_r)
    pd3 = PlotData(x, b_t, title='', label='Сумма двух катушек', x_name='x, см', y_name='B, мТл', y_error=db_t)
    pd4 = PlotData(x, b_e, label='Эксперимент', x_name='x, см', y_name='B, мТл', y_error=db_e,
                        title='Зависимость индукции магнитного\n поля между катушками Гельмгольца (d=R) от расстояния')
    d = Drawer()
    ax = d.add_figure(pd1)
    d.add_subplot_to_fig(ax, pd2)
    d.add_subplot_to_fig(ax, pd3)
    axl = d.add_subplot_to_fig(ax, pd4)
    axl.grid()
    d.save_pic("304_5")


def plot_6(ef):
    x = np.array(ef['z, см(5)'])
    b_e = np.array(ef['B, мТл(5)'])
    pd = PlotData(x,
                  b_e,
                  title='Зависимость индукции магнитного\n'
                        ' поля между катушками Гельмгольца (d=R + 2 см) от расстояния',
                  x_name='x, см', y_name='B, мТл',
                  label='B(x)'
                  )
    d = Drawer()
    d.add_figure(pd, connect_pts=True)
    d.save_pic("304_6")


def plot_7(ef):
    x = np.array(ef['z, см(6)'])
    b_e = np.array(ef['B, мТл(6)'])
    pd = PlotData(x,
                  b_e,
                  title='Зависимость индукции магнитного\n'
                        ' поля между катушками Гельмгольца (d=R - 2 см) от расстояния',
                  x_name='x, см', y_name='B, мТл',
                  label='B(x)'
                  )
    d = Drawer()
    d.add_figure(pd, connect_pts=True)
    d.save_pic("304_7")


if __name__ == '__main__':
    ef_data = get_data()
    repr_data(ef_data)
    plot_6(ef_data)
    plot_7(ef_data)


