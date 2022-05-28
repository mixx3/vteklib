from src.plot_data import PlotData, format_input
from src.drawer import Drawer
from src.regressions.linear import Linear


def plot1():
    V1 = format_input("""14,724
12,212
10,014
8,4126
7,816
6,56
5,461
5,1627
4,8487
4,5347
4,2207
3,9067
3,5927
3,2787
2,9647
2,6507
2,3367
2,0227
1,7087
1,3947
0,594
0,47468
0,40874
0,3428
0,31454""")
    P1 = format_input("""10
12
14
16
17
19
21
21,4
21,4
21,4
21,4
21,4
21,4
21,4
21,4
21,4
21,4
21,7
21,7
21,9
23
24
25
27
29""")
    V2 = format_input("""14,724
12,4004
10,328
8,7109
7,5177
6,4187
5,41704
4,519
4,048
3,734
3,42
3,106
2,792
2,478
2,164
1,85
1,536
0,9708
0,6254
0,53434
0,49352
0,48096
0,4527
0,44328""")
    P2 = format_input("""10,5
12
14
16
18
20
22
23
24
25
25,3
25,5
25,3
25,3
25,5
25,5
25,5
26
27
28
29
30
31
32""")
    V3 = format_input("""14,724
12,4632
10,4693
8,9464
7,7532
6,6542
5,7436
4,8958
4,1108
3,42
3,106
2,792
2,478
2,164
1,85
1,222
0,83578
0,6411
0,58772
0,57516
0,55004
0,53748
0,52492
0,51236""")
    P3 = format_input("""10,7
12,7
14,7
16,7
18,7
20,7
22,7
24,7
26,7
27,9
28,1
28,1
28,1
28,1
28,1
28,1
29
30
31
32
33
34
35
36""")
    drawer = Drawer()
    pd1 = PlotData(V1, P1,
                   label='297 K',
                   title='',
                   x_name='V, см³',
                   y_name='P, бар')
    ax = drawer.add_figure(pd1, connect_pts=True)
    xmin, xmax = ax.get_xlim()
    ax.plot([5.1627, -2], [21.4, 21.4], c='black', linestyle='dashed')
    ax.plot([4.048, -2], [25.3, 25.3], c='grey', linestyle='dashed')
    ax.plot([3.106, -2], [28.1, 28.1], c='red', linestyle='dashed')
    ax.set_xlim(xmin, xmax)
    pd2 = PlotData(V2, P2,
                   label='302,7 K',
                   title='',
                   x_name='V, см³',
                   y_name='P, бар')
    pd3 = PlotData(V3, P3,
                   label='308 K',
                   x_name='V, см³',
                   y_name='P, бар',
                   title='Изотермы SF₆ при разных температурах в осях P(V)')
    drawer.add_subplot_to_fig(ax, pd2, connect_pts=True)
    drawer.add_subplot_to_fig(ax, pd3, connect_pts=True)
    drawer.save_pic('1')


def plot2():
    P1 = format_input("""17	
18	
18,7	""")
    P_error = [0.5] * len(P1)
    T = format_input("""297
302,7
308""")
    P2 = format_input("""12	
12,5	
12,7	""")
    pd1 = PlotData(T, P1, y_error=P_error,
                  title='Зваисимость давления от температуры T для двух объемов V',
                  x_name='T, K',
                  y_name='P, бар',
                   label='V = 7,5 см³\n ')
    pd2 = PlotData(T, P2, y_error=P_error, title='Зваисимость давления от температуры T для двух объемов V',
                   x_name='T, K',
                   y_name='P, бар',
                   label='V = 12,3 см³')
    pd1.approximate(Linear(), repr_equation=True)
    pd2.approximate(Linear(), repr_equation=True)
    drawer = Drawer()
    ax = drawer.add_figure(pd1, errors=True)
    ax.grid()
    drawer.add_subplot_to_fig(ax, pd2, errors=True)
    drawer.save_pic('2')


if __name__ == '__main__':
    plot1()
