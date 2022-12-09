import json

import matplotlib.pyplot as plt

from vteklib.utils.excel_parser import ExcelFile
from vteklib.plot_data import PlotData
from vteklib.drawer import Drawer
from vteklib.regressions.linear import Linear
import numpy as np


def plot_2():
    t = """
    373
    378
    380
    381,5
    382,7
    383
    383,6
    384
    385
    385,5
    386,4
    386,6
    391
    393
    395
    397
    398
    403
    408
    413
    418
    423
    428
    433
    438
    443"""
    u = """
    -305
    -139
    -83
    -42
    -13
    0,42
    4,5
    17
    38
    43
    54
    82
    111
    126
    144
    159
    164
    173
    181
    175
    167
    156
    142
    128
    117
    107
    """
    pd = PlotData(
        t,
        u,
        title="Зависимость U от температуры",
        x_name="T, K",
        y_name="U, mB",
        label="U(T)",
    )
    d = Drawer()
    d.add_figure(pd)
    d.save_pic("308")


def plot_1():
    u1 = np.array(
        [
            4.5,
            4.65,
            99.7,
            133.9,
            172.9,
            212.9,
            248.4,
            282.6,
            317.5,
        ]
    )
    b1 = np.array(
        [
            0,
            43,
            90,
            138,
            182,
            228,
            274,
            315,
            357,
        ]
    )
    u2 = np.array(
        [
            8.7,
            89.6,
            172.5,
            253,
            337,
            415,
            484,
            513,
            519,
        ]
    )
    b2 = np.array(
        [
            0,
            44,
            90,
            138,
            181,
            228,
            274,
            315,
            357,
        ]
    )
    u3 = np.array(
        [
            0,
            117,
            251,
            381,
            500,
        ]
    )
    b3 = np.array(
        [
            0,
            43,
            89,
            138,
            182,
        ]
    )
    u4 = np.array(
        [
            5,
            172,
            335,
            500,
        ]
    )
    b4 = np.array(
        [
            0,
            43,
            89,
            138,
        ]
    )
    u5 = np.array(
        [
            10,
            175,
            407,
            500,
        ]
    )
    b5 = np.array(
        [
            0,
            43,
            82,
            138,
        ]
    )
    plt.scatter(b1, u1, label="5mA")
    plt.scatter(b2, u2, label="10mA")
    plt.scatter(b3, u3, label="15mA")
    plt.scatter(b4, u4, label="20mA")
    plt.scatter(b5, u5, label="25mA")
    plt.grid()
    plt.xlabel("B, мТл")
    plt.ylabel("U, мВ")
    plt.legend()
    plt.title("Зависимость U от величины магнитной индукции B")
    plt.savefig("308_1.png")


if __name__ == "__main__":
    plot_1()
