from vteklib.drawer import Drawer
from vteklib.plot_data import PlotData, format_input
from vteklib.regressions.linear import Linear


def plot1():
    t = format_input(
        """5
6
8
10
15
20
30"""
    )
    ln = format_input(
        """1,485
1,64
1,79
1,95
2,29
2,61
3,20"""
    )
    pld = PlotData(
        t,
        ln,
        title="Зависимость ln(Δp1/Δp)",
        label="ln(Δp1/Δp)(t)",
        x_name="t, с",
        y_name="ln(Δp1/Δp)",
    )
    pld.approximate(Linear(), repr_equation=True)
    drawer = Drawer()
    drawer.add_figure(pld)
    drawer.save_pic("240_1")


if __name__ == "__main__":
    plot1()
