import json

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np
from functools import lru_cache


@lru_cache(None)
def get_data():
    ef_data = json.loads(ExcelFile("308.xlsx").to_json())
    return ef_data


def repr_data(ef_data):
    for d in ef_data.keys():
        print(d, ef_data[d])


def plot_1():
    r = np.array([1, 5.1, 10, 22])
    invq = np.array([0.11, 0.16, 0.24, 0.43])
    pd = PlotData(
        r,
        invq,
        title="Зависимость величины, обратной к дрбротности \n"
        " от активного сопротивления контура",
        x_name="R, Ом",
        y_name="Q^-1",
        label="Q^-1(R)",
    )
    pd.approximate(Linear(), repr_equation=True)
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("339_1")


def plot_2():
    f = np.array([7051, 4731, 3239, 2134, 1409])
    q = np.array([7.9, 5.56, 3.86, 2.58, 1.79])
    dq = np.array([2.8, 1.4, 0.67, 0.31, 0.16])
    pd = PlotData(
        f,
        q,
        y_error=dq,
        title="Зависимость добротности колебательного контура от разонансной частоты",
        x_name="fрез, Гц",
        y_name="Q",
        label="Q(fрез)",
    )
    pd.approximate(Linear(), repr_equation=True)
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("339_2")


if __name__ == "__main__":
    plot_2()
