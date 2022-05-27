import numpy as np
import pandas as pd
from regressions.plot_data import PlotData
from drawer import Drawer
from regressions.linear import Linear
df = pd.read_excel('201.xlsx')

T = np.array(df[df.columns[0]])
P1 = np.array(df[df.columns[1]])
P2 = np.array(df[df.columns[2]])
print(df.columns)


def plot1():
    pld = PlotData(T, P1, title='', x_name='T', y_name='P', label='P1')
    pld2 = PlotData(T, P2, title='Зависимости давлений на концах капилляра от времени', x_name='T, c', y_name='P, Па', label='P2(t)')
    drawer = Drawer()
    ax = drawer.add_figure(pld)
    ax.set_yscale('log')
    xmin, xmax = ax.get_xlim()
    ax.set_xlim(0, xmax)
    ax2 = drawer.add_subplot_to_fig(ax, pld2)
    ax2.set_yscale('log')
    ax.grid()
    ax2.grid()
    xmin, xmax = ax2.get_xlim()
    ax2.set_xlim(0, xmax)
    drawer.save_pic('201_1')


def plot2():
    I = np.array(df['I(t)'])[0:800]
    pld = PlotData(T, I,
                   title='Зависимость потока газа от времени',
                   label='I(t)',
                   x_name='T, с',
                   y_name='I, м³ * Па/с')
    drawer = Drawer()
    ax = drawer.add_figure(pld)
    ax.set_yscale('log')
    drawer.save_pic('201_2')


def plot3():
    n = np.array(df['eta'])[0:800]
    pld = PlotData(P1, n,
                   title='Зависимость к-та динамической вязкости от давления P1',
                   x_name='P1, Па',
                   y_name='η, Па*c')
    drawer = Drawer()
    ax = drawer.add_figure(pld)
    ax.set_xscale('log')
    drawer.save_pic('201_3')


def add_plot_w_log(pld, ax):
    ax2 = drawer.add_subplot_to_fig(ax, pld)
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    return ax2


def plot4():
    L1 = np.array(df['lambda(p1)'])[0:90]
    L2 = np.array(df['lambda(p2)'])[0:90]
    L1_theory = np.array(df['lt(p1)'])[0:90]
    L2_theory = np.array(df['lt(p2)'])[0:90]
    P5 = P1[0:90]
    pld = PlotData(P5, L1,
                   title='',
                   label='λ1 эксп',
                   x_name='P1, Па',
                   y_name='λ1, м')
    pld3 = PlotData(P5, L2,
                    title='',
                    label='λ2 эксп',
                    x_name='P1, Па',
                    y_name='λ2, м')
    pld4 = PlotData(P5, L2_theory,
                   title='Зависимость длины свободного пробега',
                   label='λ2 теор',
                   x_name='P1, Па',
                   y_name='λ2, м'
                   )
    pld2 = PlotData(P5, L1_theory,
                    title='',
                    label='λ1 теор',
                    x_name='P1, Па',
                    y_name='λ1, м')

    drawer = Drawer()
    ax = drawer.add_figure(pld)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax2 = drawer.add_subplot_to_fig(ax, pld2)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax3 = drawer.add_subplot_to_fig(ax, pld3)
    ax3.set_yscale('log')
    ax3.set_xscale('log')
    ax4 = drawer.add_subplot_to_fig(ax, pld4)
    ax4.set_yscale('log')
    ax4.set_xscale('log')
    ax.grid()
    ax2.grid()
    ax3.grid()
    ax4.grid()
    drawer.save_pic('201_4')


def plot5():
    S = np.array(df['S'])[5:90]
    S_theor = np.array(df['S theory'])[5:90]
    p5 = P2[5:90]
    pld = PlotData(p5, S,
                   title='',
                   x_name='P2, Па',
                   y_name='S, м³/с',
                   label='S эксп')
    pld2 = PlotData(p5, S_theor,
                    title='Зависимость скорости откачки насоса S от давления P2',
                    x_name='P2, Па',
                    y_name='S, м³/с',
                    label='S теор')
    drawer = Drawer()
    ax = drawer.add_figure(pld)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax2 = drawer.add_subplot_to_fig(ax, pld2)
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    drawer.save_pic('201_5')


def plot6():
    pld = PlotData(T, P1,
                   title='Зависимость давления P1 от времени при натекании',
                   x_name='T, c',
                   y_name='P1, Па',
                   label='P1(T)')
    pld.approximate(Linear(), repr_equation=True)
    drawer = Drawer()
    drawer.add_figure(pld)
    drawer.save_pic('201_6')


if __name__ == '__main__':
    plot4()