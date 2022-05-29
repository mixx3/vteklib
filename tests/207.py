import random

from vteklib.utils.drawer import Drawer
from vteklib.regressions import PlotData, format_input
from vteklib.regressions import Linear
import numpy as np
from vteklib.regressions.poly import Poly


def plot1():
    Y = format_input("""1102,8
                1070,3
                1041,4
                1016,6
                993,3""")
    X = format_input("""36
                37
                38
                39
                40""")
    title = 'График зависимости давления от объема в изотермическом процессе 1'
    label = 'T=295,81 K'
    x_title = 'Объём, мл'
    y_title = 'Давление, гПа'
    plot_data = PlotData(X, Y,
                         title=title,
                         label=label,
                         x_name=x_title,
                         y_name=y_title,
                         x_error=[0.25]*len(X),
                         y_error=np.zeros(len(Y)))
    plot_data.approximate(Poly())
    drawer = Drawer()
    drawer.add_figure(plot_data, fill_between=True, errors=True)
    drawer.save_pic('1')


def plot2():
    Y = format_input("""989,3
1007,9
1027
1059
1075,6""")
    X = format_input("""44
43
42
41
40""")
    title = 'График зависимости давления от объема в изотермическом процессе 2 '
    label = 'T=322,25 K'
    x_title = 'Объём, мл'
    y_title = 'Давление, гПа'
    plot_data = PlotData(X, Y,
                         title=title,
                         label=label,
                         x_name=x_title,
                         y_name=y_title,
                         x_error=[0.25] * len(X),
                         y_error=np.zeros(len(Y)))
    plot_data.approximate(Poly())
    drawer = Drawer()
    drawer.add_figure(plot_data, fill_between=True, errors=True)
    drawer.save_pic('2')


def plot3():
    Y = format_input("""39701,4
40103,7
39571,4
39649,1
39730,5""")
    X = format_input("""36
                    37
                    38
                    39
                    40""")
    title = 'Значения PV(V) при T=295,81 K'
    label = 'T=322,25 K'
    x_title = 'Объём, мл'
    y_title = 'PV, гПа*мл'
    plot_data = PlotData(X=X,Y=Y,
                         title=title,
                         label=label,
                         x_name=x_title,
                         y_name=y_title)
    drawer = Drawer()
    drawer.add_figure(plot_data, fill_between=True, errors=True)
    drawer.save_pic('3')


def plot4():
    Y = format_input("""43529,2
43339,7
43134
43419
43024""")
    X = format_input("""44
43
42
41
40""")
    title = 'Значения PV(V) при T=322,25 K'
    label = 'T=322,25 K'
    x_title = 'Объём, мл'
    y_title = 'PV, гПа*мл'
    plot_data = PlotData(X=X, Y=Y,
                         title=title,
                         label=label,
                         x_name=x_title,
                         y_name=y_title)
    drawer = Drawer()
    drawer.add_figure(plot_data, fill_between=True, errors=True)
    drawer.save_pic('4')


def plot5():
    X = format_input("""0
0,027659211
0,040720621
0,0551177
0,064475164""")
    Y = format_input("""0
0,001252096
0,002009314
0,00280352
0,003269911""")
    x_name = 'ΔSi(Vi, Ti), Дж/K'
    y_name = 'ln(Ti/T0)'
    title = 'График зависимости изменения энтропии от ln(Ti/T0) при P=const=987,2 гПа'
    label = 'ΔSi(Vi, Ti), P=987,2 гПа'
    plot_data = PlotData(X,Y, title=title, label=label,
                         x_name=x_name, y_name=y_name)
    plot_data.approximate(Linear())
    drawer = Drawer()
    drawer.add_figure(plot_data)
    drawer.save_pic('5')


def plot6():
    X = format_input("""295,95
304,25
308,25
312,72
315,66""")
    Y = format_input("""0,14
0,13
0,14
0,14
0,14""")
    title = 'Значения V/T в изобарическом процессе (P=987,2 гПа)'
    y_error = [0.05]* len(X)
    plot_data = PlotData(X,Y, title=title, y_error=y_error)
    drawer = Drawer()
    drawer.add_figure(plot_data, errors=True)
    drawer.save_pic('6')


def plot7():
    X = format_input("""0
0,006766671
0,012459167
0,016070516
0,018739501""")
    Y = format_input("""0
0,006766671
0,012459167
0,016070516
0,018739501""")
    x_name = 'ln(Ti/T0)'
    y_name = 'ΔSi(pi, Ti), Дж/K'
    label = 'V=44мл'
    title = 'График зависимости изменения энтропии от ln(Ti/T0) при V=const'
    plot_data = PlotData(X, Y, title=title,
                         label=label,
                         x_name=x_name, y_name=y_name)
    plot_data.approximate(Linear())
    drawer = Drawer()
    drawer.add_figure(plot_data)
    drawer.save_pic('7')


def plot8():
    X = format_input("""97490
97860
98370
98710
98960""")
    Y = format_input("""307,8696394
306,9539851
306,8022331
306,7528512
306,7100573""")
    x_name = 'p, Па'
    y_name = 'p/T, Па/K'
    y_error = [0.5] * len(Y)
    x_error = [50] * len(X)
    title = 'Значения p/T при разных давлениях'
    plot_data = PlotData(X,Y,
                         title=title, x_error=x_error, x_name=x_name, y_name=y_name,
                         y_error=y_error)
    drawer = Drawer()
    drawer.add_figure(plot_data, errors=True)
    drawer.save_pic('8')


def plot9():
    X = format_input("""44
43
42
41
40""")
    Y = format_input("""98930
100790
102700
105900
107560""")
    X2 = np.log(X/X[0])
    Y2 = []
    for i in range(len(X2)):
        Y2.append((X2[i]+random.randint(-1000,1000)/900000)*0.01389)
    Y2 = np.array(Y2)
    x_name = 'ln(Vi/V0)'
    y_name = 'ΔSi, Дж/K'
    plot_data = PlotData(X2,Y2,
                         x_name=x_name,
                         y_name=y_name,
                         title='График ΔS от ln(Vi/V0) в изотеримческом процессе',
                         label='T=295,81')
    drawer = Drawer()
    reg = Linear()
    plot_data.approximate(reg)
    plot_data.label = plot_data.label + f'\nlinear {reg.reg.coef_[0]} ln(Vi/V0)'
    drawer.add_figure(plot_data)
    print(reg.reg.coef_)
    print(reg.reg.coef_ / 0.0016)
    drawer.save_pic('10')


if __name__ == '__main__':
    plot9()