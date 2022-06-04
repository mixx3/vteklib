import pandas as pd
import numpy as np
from vteklib.regressions import PlotData
from vteklib.drawer import Drawer

df = pd.DataFrame()
with open('2_232.txt', 'r') as file:
    lines = file.read().split('\n')
    time = []
    V = []
    pressure = []
    for line in lines[2:-1:]:
        line = line.split()
        time.append(float(line[0]))
        V.append(float(line[1]))
        pressure.append(float(line[2]))
    df['time'] = time
    df['volts'] = V
    df['pressure'] = pressure


vmax = np.max(df['volts'])
vmin = np.min(df['volts'])
pmin = np.min(df['pressure'])
pmax = np.max(df['pressure'])
p1 = (pmax - pmin) / 2
v1 = (vmax - vmin) / 2
volumes = []
for v in df['volts']:
    volumes.append(345 - 15*((v - vmin)/(vmax-vmin)))
df['volumes'] = volumes

print(vmin, vmax)
print(pmin, pmax)
print(p1)
print(np.sin(2.79))


def p_v1():
    plot_data = PlotData(np.array(df['volumes']), np.array(df['pressure']),
                         title='График цикла реальной машины Стирлинга, второе измерение',
                         x_name='V, см³',
                         y_name='P, Па')
    drawer = Drawer()
    drawer.add_figure(plot_data, connect_pts=True)
    drawer.save_pic('3')


def p_t_and_v_t():
    plot_data = PlotData(np.array(df['time'][10:-10]),
                         np.array(df['pressure'][10:-10]),
                         title='Зависимости P(t) и V(t), второе измерение',
                         y_name='P, Па',
                         x_name='t, с',
                         label='P(t)')
    plot_data2 = PlotData(np.array(df['time'][10:-10]),
                          np.array(df['volumes'][10:-10]),
                          y_name='V, см³',
                          label='V(t)',
                          title='')
    drawer = Drawer()
    ax = drawer.add_figure(plot_data)
    ax2 = ax.twinx()
    drawer.add_subplot_to_fig(ax2, plot_data2)
    ax2.legend(loc=0)
    ax.legend(loc=2)
    drawer.save_pic('4')


if __name__ == '__main__':
    p_v1()

