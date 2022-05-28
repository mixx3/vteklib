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
    """
    An abstract base class for regression.
    You can inherit this class for specific regression type.
    In this case overloading abstract methods required.
    """
    @abstractmethod
    def fit(self, x_data: Series, y_data: Series):
        """
        Trains regression model on given dataset
        :param x_data:
        :param y_data:
        :return:
        """
        ...

    @abstractmethod
    def predict(self, x_data: Series) -> ndarray:
        """
        Returns ndarray with predicted values
        :param x_data:
        :return:
        """
        ...
