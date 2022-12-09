from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from functools import lru_cache
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
from vteklib.regressions.poly import Poly
import numpy as np
import pandas as pd


@lru_cache(None)
def get_data(path: str):
    ef = ExcelFile(path)
    series = ef.get_series()
    for s in series:
        print(s)
    return series


def plot_1(series):
    I = np.array(series[2].data)
    V = np.array(series[0].data)
    I2 = np.array(series[6].data)
    V2 = np.array(series[4].data)
    plot_data1 = PlotData(
        V, I, title="ВАХ диода, прямая ветвь", x_name="U, B", y_name="I, мА"
    )
    d1 = Drawer()
    d1.add_figure(plot_data1)
    plot_data2 = PlotData(
        V2, I2, title="ВАХ диода, обратная ветвь", x_name="U, B", y_name="I, мА"
    )
    d1.add_figure(plot_data2)
    d1.save_pic("323_1")


def plot_2(series):
    I = np.array(series[2].data)
    V = np.array(series[0].data)
    pd1 = PlotData(V, I, title="Зависимость тока через диод I от напряжения на нём U")
    d1 = Drawer()
    reg = pd1.approximate(
        Linear(),
        repr_equation=True,
        x_train=pd1.df[pd1.x_name][11::],
        y_train=pd1.df[pd1.y_name][11::],
        x_test_range=[pd1.df[pd1.x_name][11], 0.75, 10],
    )
    d1.add_figure(pd1)
    d1.save_pic("323_2")


def plot_3(series):
    ln_i = np.array(series[7].data[:11])
    V = np.array(series[0].data[10::])
    pd1 = PlotData(
        V,
        ln_i,
        title="Зависимость ln(I) от напряжения на диоде U",
        x_name="U, B",
        y_name="ln(I)",
    )
    d = Drawer()
    pd1.approximate(Linear(), repr_equation=True)
    d.add_figure(pd1)
    d.save_pic("323_3")


def plot_4(series):
    c_base = np.array(series[9].data)
    V = np.array(series[8].data)
    pd1 = PlotData(
        V,
        c_base,
        title="Зависимость барьерной ёмкости конденсатора при обратном подключении",
        x_name="U, B",
        y_name="Сб, нФ",
    )
    pd1.approximate(Poly(), repr_equation=True)
    d = Drawer()
    d.add_figure(pd1)
    d.save_pic("323_4")


def plot_5(series):
    U = np.array(series[11].data)
    T = np.array(series[10].data) + 273
    sT = np.array(series[12].data)
    sU = np.array(series[13].data)
    pd = PlotData(
        T,
        U,
        x_error=sT,
        y_error=sU,
        title="Зависимость напряжения на диоде от температуры",
        x_name="T, K",
        y_name="U, B",
    )
    pd.approximate(Linear(), repr_equation=True)
    drawer = Drawer()
    drawer.add_figure(pd)
    drawer.save_pic("323_5")


if __name__ == "__main__":
    series = get_data("323.xlsx")
    plot_5(series)
