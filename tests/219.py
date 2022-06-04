from vteklib.regressions.linear import Linear
from vteklib.plot_data import PlotData, format_input
from vteklib.drawer import Drawer
import numpy as np


def plot1():
    W = format_input("""0,0204
    0,06695
    0,1386
    0,23575
    0,3654
    0,5412
    0,7714""")

    R = format_input("""3,1875
    3,961538462
    4,277777778
    4,456521739
    4,660714286
    4,96969697
    5,342105263""")
    dR = format_input("""0,044194174
0,027196415
0,03928371
0,015371887
0,012626907
0,021427478
0""")

    pld = PlotData(W, R, y_error=dR, x_name='W, Вт', y_name='R, Ом', title='Зависимость сопротивления от мощности', label='R(W)')
    drawer = Drawer()
    pld.approximate(Linear(), x_train=W[1::], y_train=R[1::], repr_equation=True)

    drawer.add_figure(pld, errors=True)
    drawer.save_pic('1')


def plot2():
    deltaP = format_input("""225,4
    196
    147
    127,4
    """)
    Q = format_input("""0,9
0,8
0,5
0,4""")
    dq = np.array([0.01]* len(Q))
    pld = PlotData(deltaP, Q,
                   x_name='ΔP, Па', y_name='Q, см³/с',
                   title='Зависимость объемного потока воздуха от разницы давлений',
                   y_error=dq,
                   label='Q(ΔP)')
    drawer = Drawer()
    pld.approximate(Linear(), repr_equation=True)
    drawer.add_figure(pld)
    drawer.save_pic('2')


def find_eta():
    a = 0.0052
    r = 0.05
    l = 23
    da = 0.0001
    print(np.pi * r ** 4 * da / (8 * l * a ** 2))


def find_reynolds():
    print(2*1.24e-3*0.9 / (np.pi * 0.05 * 2.05e-5))


def find_cv():
    print(0.5 * (0.018 / 2.05e-5) / 32)


if __name__ == '__main__':
    find_cv()
