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
