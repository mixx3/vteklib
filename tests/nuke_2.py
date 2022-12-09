import json
from typing import Tuple, List, Any

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np
from functools import lru_cache


def get_data_from_file(path) -> tuple[list[Any], list[Any]]:
    x_data = []
    y_data = []
    with open(path) as file:
        text = file.readlines()
        for t in text:
            x, y = [int(i) for i in t.split()]
            x_data.append(x)
            y_data.append(y)
    return x_data, y_data


def plot_1():
    x = np.array([349, 446, 480, 569, 844])
    y = np.array([4.782, 5.305, 5.49, 6.002, 7.687])
    pd = PlotData(
        np.array(x),
        np.array(y),
        title="Зависимость E(МэВ) от номера канала",
        x_name="номер канала",
        y_name="Е(МэВ)",
    )
    pd.approximate(Linear(), repr_equation=True)
    d = Drawer()
    ax = d.add_figure(pd)
    # ax.set_xlim(0)
    # ax.set_ylim(0)
    d.save_pic(f"3_1")


def print_data(suff):
    x, y = get_data_from_file(f"parfenovma/parfenovma{suff}.txt")
    pd = PlotData(
        np.array(x), np.array(y), title=f"{suff}", x_name="номер канала", y_name="N"
    )
    d = Drawer()
    ax = d.add_figure(pd)
    ax.set_xlim(0)
    ax.set_ylim(0)
    d.save_pic(f"{suff}_1")


def get_all():
    suff = ["1", "1_1", "1_3"]
    for s in suff:
        print_data(s)


def plot_3():
    r_mm = np.arange(0, 31, 2)
    e1 = np.array(
        [
            217,
            223,
            225,
            246,
            227,
            250,
            204,
            16,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
    )
    e1_r = np.array([15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0])
    e2 = np.array(
        [652, 588, 622, 623, 604, 570, 612, 600, 609, 643, 401, 252, 232, 56, 0, 0]
    )
    rr = [25] * 15
    rr.append(0)
    e2_r = np.array(rr)
    e3 = np.array(
        [223, 224, 220, 240, 225, 220, 233, 205, 243, 203, 219, 249, 211, 211, 218, 215]
    )
    e3_r = np.array([15] * 16)
    pd1 = PlotData(
        r_mm,
        e1,
        title="",
        label="E1=4,78MeV",
        x_name="R, mm",
        y_name="counts",
        y_error=e1_r,
    )
    pd2 = PlotData(
        r_mm,
        e2,
        title="",
        label="E2=5,3-5,49MeV",
        x_name="R, mm",
        y_name="counts",
        y_error=e2_r,
    )
    pd3 = PlotData(
        r_mm,
        e3,
        title="График зависимости интенсивности\n от расстояния между детектором и источником",
        label="E3=6MeV",
        x_name="R, mm",
        y_name="counts",
        y_error=e3_r,
    )
    d = Drawer()
    ax = d.add_figure(pd1, connect_pts=True, errors=True)
    ax.set_xlim(0)
    ax.set_ylim(0, 660)
    d.add_subplot_to_fig(ax, pd2, connect_pts=True, errors=True)
    d.add_subplot_to_fig(ax, pd3, connect_pts=True, errors=True)
    d.save_pic("3_2")


def plot_4():
    r = np.array([14, 23])
    e3_2 = np.sqrt(np.array([4.78, 5.4]) ** 3)
    pd = PlotData(e3_2, r)
    pd.approximate(Linear(), repr_equation=True)
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("4_2")


if __name__ == "__main__":
    plot_4()
