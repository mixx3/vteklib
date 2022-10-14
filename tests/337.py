import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData, format_input
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
from vteklib.regressions.poly import Poly
import numpy as np
from functools import lru_cache

# garbadge excel file! so let's hardcode data!!! :]


def plot_1():
    d = """0	5	10	15	20	25	35	45	55	65"""
    d2 = """0	5	10	15	20	25"""
    f1 = """6378	6514	6631	6741	6818	6902	7018	7095	7110	7108"""
    dd = np.array([0.5]* 10)
    df = np.zeros(10)
    df2 = np.zeros(6)
    f2 = """8279	8016	7791	7628	7492	7378"""
    dd2 = np.array([0.5] * 6)
    f0 = """7145	7149	7141	7143	7131	7128	7098	7095	7110	7108"""
    pd1 = PlotData(d, f1, x_error=dd, y_error=df, title='', x_name='x, см', y_name='f, Гц', label='f1')
    pd2 = PlotData(d2, f2, x_error=dd2, y_error=df2, title='', x_name='x, см', y_name='f, Гц', label='f2')
    pd3 = PlotData(d, f0, y_error=df,
                   x_error=dd,
                   title='Зависимость нормальных (собственных) частот \n'
                         'связанных контуров f от расстояния между катушками d',
                   x_name='x, см', y_name='f, Гц', label='f0')
    d = Drawer()
    ax = d.add_figure(pd2, connect_pts=True)
    ax2 = d.add_subplot_to_fig(ax, pd1, connect_pts=True)
    ax2.grid()
    lax = d.add_subplot_to_fig(ax2, pd3, connect_pts=True)
    lax.grid()
    d.save_pic("337_1")


def plot_2():
    d = """0 5 10 15 20 25 35 45 55 65"""
    l12 = """0,268 0,215 0,168 0,129 0,099 0,070 0,000 0,000 0,000 0,000"""
    pd = PlotData(d, l12, title='Зависимость взаимной индукции катушек от расстояния между ними', label="L12(d)",
                  x_name='x, см', y_name='L12, мГн')
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("337_2")


def plot_3():
    d = """0 5 10 15 20 25 35 45 55 65"""
    k = """0,255	0,205	0,160	0,123	0,094	0,066	0,000	0,000	0,000	0,000"""
    pd = PlotData(d, k, title='Зависимость коэффициента связи катушек от расстояния между ними', label="K(d)",
                  x_name='x, см', y_name='K')
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("337_3")


def plot_4():
    x = """1,0	1,4	2,1	6,5	9,1"""
    y = """0,206	0,341	0,501	1,512	2,063"""
    pd = PlotData(x, y, title='Зависимость разности квадратов частот от 2/Cсв', label="f022-f012(2/Cсв)",
                  y_name='f022-f012, 10^8 Гц2', x_name='2/Cсв, мкФ-1')
    d = Drawer()
    pd.approximate(Linear(), repr_equation=True)
    d.add_figure(pd)
    d.save_pic("337_4")


def plot_5():
    k = """0,187	0,251	0,331	0,603	0,681"""
    f1_e = """7113	7113	7113	7113	7113"""
    f1_t = """7162	7162	7162	7162	7162"""
    f2_e = """8439	9202	10033	14206	16027"""
    f2_t = """8656	9259	10102	14381	16445"""
    pd1 = PlotData(k, f1_e, title='Зависимость резоенансных частот от коэффициента связи K', label="f1exp",
                  x_name='', y_name='f, Гц')
    pd2 = PlotData(k, f1_t, title='Зависимость резоенансных частот от коэффициента связи K', label="f1theory",
                   x_name='', y_name='f, Гц')
    pd3 = PlotData(k, f2_e, title='Зависимость резоенансных частот от коэффициента связи K', label="f2exp",
                   x_name='', y_name='f, Гц')
    pd4 = PlotData(k, f2_t, title='Зависимость резоенансных частот от коэффициента связи K', label="f2theory",
                   x_name='', y_name='f, Гц')
    d = Drawer()
    pd1.approximate(Linear())
    pd2.approximate(Linear())
    pd3.approximate(Poly())
    pd4.approximate(Poly())
    ax = d.add_figure(pd1)
    d.add_subplot_to_fig(ax, pd2)
    d.add_subplot_to_fig(ax, pd3)
    lax = d.add_subplot_to_fig(ax, pd4)
    lax.grid()
    d.save_pic("337_5")


if __name__ == '__main__':
    plot_5()
