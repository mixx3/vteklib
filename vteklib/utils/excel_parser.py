import numpy as np
import pandas
import pandas as pd


class ExcelFile:
    def __init__(self, excel_fp: str):
        self.df: pd.DataFrame = pandas.read_excel(excel_fp)
        self.df: pd.DataFrame = pandas.read_excel('/Users/new/PycharmProjects/vteklib/219.xlsx')
        self.series: dict = dict()
        for col in self.df.columns:
            name = col
            vals = []
            pt = 0
            curr = self.df[col][pt]
            while not pd.isna(curr) or type(curr) == str:
                vals.append(curr)
                pt += 1
                curr = self.df[col][pt]
            if vals:
                self.series[name] = vals


if __name__ == '__main__':
    ef = ExcelFile('219.xlsx')
