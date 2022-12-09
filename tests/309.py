import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np
from functools import lru_cache


def plot_1():
    c = np.array([97.9, 489, 927])  # nf
    dc = np.array([5.5, 2.48, 4.68])
    tsq = np.array([1.15, 2.61, 3.77]) ** 2
    dtsq = np.array([0.02] * len(tsq))
    pd = PlotData(
        c,
        tsq,
        title="Зависимость квадрата периода T^2 от емкости конденсатора С при R=0",
        x_name="C, нФ",
        y_name="Т^2, c^2",
        label="T^2(C)",
        x_error=dc,
        y_error=dtsq**2,
    )
    pd.approximate(Linear())
    d = Drawer()
    d.add_figure(pd, errors=True)
    d.save_pic("309_1")


def plot_2():
    c = np.array([97.9, 489, 927])  # nf
    dc = np.array([5.5, 2.48, 4.68])
    tsq = np.array([1.17, 2.57, 3.61]) ** 2
    dtsq = np.array([0.02] * len(tsq))
    pd = PlotData(
        c,
        tsq,
        title="Зависимость квадрата периода T^2 от емкости конденсатора С при R=R1",
        x_name="C, нФ",
        y_name="Т^2, c^2",
        label="T^2(C)",
        x_error=dc,
        y_error=dtsq**2,
    )
    pd.approximate(Linear())
    d = Drawer()
    d.add_figure(pd, errors=True)
    d.save_pic("309_2")


def plot_3():
    c = np.array([97.9, 489, 927])  # nf
    dc = np.array([5.5, 2.48, 4.68])
    tsq = np.array([1.15, 2.65, 3.69]) ** 2
    dtsq = np.array([0.02] * len(tsq))
    pd = PlotData(
        c,
        tsq,
        title="Зависимость квадрата периода T^2 от емкости конденсатора С при R=R2",
        x_name="C, нФ",
        y_name="Т^2, c^2",
        label="T^2(C)",
        x_error=dc,
        y_error=dtsq**2,
    )
    pd.approximate(Linear())
    d = Drawer()
    d.add_figure(pd, errors=True)
    d.save_pic("309_3")


def calc():
    l = np.array([407, 425, 418])
    print(np.std(l))


if __name__ == "__main__":
    calc()
