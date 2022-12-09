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
    print(ef.to_json())


def plot_1(series):
    U = np.array(series[0].data)
    I = np.array(series[1].data)
    pd = PlotData(
        U, I, title="ВАХ диода", x_name="U, B", y_name="I, мА", label="I = f(U)"
    )
    drawer = Drawer()
    drawer.add_figure(pd, connect_pts=True)
    drawer.save_pic("322_1")


def plot_2(series):
    U = np.array(series[2].data)
    I = np.array(series[1].data)
    pd = PlotData(
        U,
        I,
        title="Зависимость силы тока от U^3/2",
        x_name="U3/2, В3/2",
        y_name="I, мА",
        label="I = f(U)",
    )
    pd.approximate(Linear(), repr_equation=True)
    drawer = Drawer()
    drawer.add_figure(pd)
    drawer.save_pic("322_2")


def plot_3(series):
    I1 = np.array(series[11].data)
    B1 = np.array(series[10].data)
    I2 = np.array(series[14].data)
    B2 = np.array(series[13].data)
    I3 = np.array(series[17].data)
    B3 = np.array(series[16].data)
    pd1 = PlotData(
        B1,
        I1,
        title="Зависимость нодного тока от индукции магнитного поля",
        x_name="B, мТл",
        y_name="I, мА",
        label="U=30B",
    )
    pd2 = PlotData(B2, I2, label="U=40B")
    pd3 = PlotData(B3, I3, label="U=50B")
    drawer = Drawer()
    ax = drawer.add_figure(pd3)
    drawer.add_subplot_to_fig(ax, pd2)
    drawer.add_subplot_to_fig(ax, pd1)
    drawer.save_pic("322_3")


def q_2():
    vals = np.array([2.07, 1.831, 1.837])
    print(np.std(vals))
    print(np.mean(vals))


if __name__ == "__main__":
    get_data("322.xlsx")
