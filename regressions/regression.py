from abc import ABC, abstractmethod
import pandas as pd
from pandas import Series
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, SplineTransformer
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from pandas import Series
from numpy import ndarray
import numpy as np


class Regression(ABC):
    @abstractmethod
    def fit(self, x_data, y_data):
        ...

    @abstractmethod
    def predict(self, x_data):
        ...


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


class Poly(Regression, ABC):
    def __init__(self):
        self.reg = make_pipeline(PolynomialFeatures(), Ridge(alpha=1e-3))
        self.equation = 'polynomial y(x)'

    def fit(self, x_data: Series, y_data: Series):
        self.reg.fit(np.matrix(x_data).T.A, y_data)

    def predict(self, x_data) -> ndarray:
        return self.reg.predict(np.matrix(x_data).T.A)

    @classmethod
    def __repr__(cls):
        return 'polynomial'