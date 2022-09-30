import matplotlib.pyplot as plt
import math

import matplotlib.style


def f(x):
    return math.exp(-3 * x * x) - x


if __name__ == '__main__':
    X = [i / 100 for i in range(-100, 100, 1)]
    Y = [f(i) for i in X]
    print(matplotlib.style.available)
    plt.style.use('seaborn-white')
    plt.plot(X, Y)
    plt.grid()
    plt.savefig(f"{__name__}")
