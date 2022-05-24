import matplotlib.figure
import matplotlib.pyplot as plt
from regressions.regression import Poly
from regressions.plot_data import PlotData, format_input


class Drawer:
    def __init__(self):
        plt.style.use('vtek_style.mplstyle')
        self.figures: list[matplotlib.figure.Figure] = []

    def add_figure(self, user_data: PlotData):
        fig = plt.figure(figsize=[9.6, 7.2])
        fig.set(facecolor='white')
        ax = fig.add_subplot()
        ax.grid()
        ax.scatter(user_data.df[user_data.x_name], user_data.df[user_data.y_name])
        if user_data.approximated:
            ax.plot(user_data.df[user_data.x_name], user_data.df[user_data.approx_col_name])
        ax.set_title(user_data.title)
        ax.set_xlabel(user_data.x_name)
        ax.set_ylabel(user_data.y_name)
        self.figures.append(fig)

    def show(self):
        for fig in self.figures:
            fig.show()


def test_can_add_a_subplot():
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
    plot_data.approximate(Poly())
    drawer = Drawer()
    drawer.add_figure(plot_data)
    drawer.show()


if __name__ == '__main__':
    test_can_add_a_subplot()


