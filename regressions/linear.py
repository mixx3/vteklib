from abc import ABC
from pandas import Series
from sklearn.linear_model import LinearRegression
from pandas import Series
from numpy import ndarray
from regressions.regression import Regression
import numpy as np


class Linear(Regression, ABC):
    def __init__(self):
        self.reg = LinearRegression()
        self.equation = 'linear y(x)'

    def fit(self, x_data: Series, y_data: Series):
        self.reg.fit(np.matrix(x_data).T.A, y_data)

    def predict(self, x_data: Series) -> ndarray:
        return self.reg.predict(np.matrix(x_data).T.A)

    @classmethod
    def __repr__(cls):
        return 'linear'

