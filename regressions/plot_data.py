import numpy as np
import pandas as pd
from dataclasses import dataclass
from numpy import ndarray
from regressions.regression import Regression
from regressions.poly import Poly
from regressions.linear import Linear


class PlotData:
    def __init__(self,
                 X: ndarray | str,
                 Y: ndarray | str,
                 title: str = 'plot by MikeP',
                 label: str = 'y=f(x)',
                 x_name: str = 'x',
                 y_name: str = 'y',
                 x_error: ndarray | None = None,
                 y_error: ndarray | None = None
                 ):
        self.df = pd.DataFrame()
        self.df[x_name] = format_input(X)
        self.df[y_name] = format_input(Y)
        self.df['x_error'] = x_error
        self.df['y_error'] = y_error
        self.x_name = x_name
        self.y_name = y_name
        self.title = title
        self.label = label
        self.approximated: bool = False
        self.approx_col_name = ''

    def approximate(self, reg: Regression):
        if not self.approximated:
            reg.fit(self.df[self.x_name], self.df[self.y_name])
            self.approx_col_name: str = f"{reg} {self.y_name}({self.x_name})"
            self.df[self.approx_col_name] = reg.predict(self.df[self.x_name])
            self.approximated = True
            return self.approx_col_name

    def __repr__(self):
        return self.df.__str__()


def format_input(args: str | ndarray) -> ndarray | list[ndarray]:
    if type(args) == ndarray:
        return args
    return np.array(args.replace(',', '.').split(), dtype=float)


def test_figures():
    Y = format_input("""110280
        107030
        104140
        101660
        99330""")
    X = format_input("""36
        37
        38
        39
        40""")
    title = 'График зависимости давления от объема в изотермическом процессе'
    label = 'T=const'
    x_title = 'Объём, мл'
    y_title = 'Давление, гПа'
    plot_data = PlotData(X, Y,
                         title=title,
                         label=label,
                         x_name=x_title,
                         y_name=y_title)
    print(type(plot_data.df[plot_data.x_name]))
    plot_data.approximate(Linear())
    print(plot_data)


if __name__ == '__main__':
    test_figures()