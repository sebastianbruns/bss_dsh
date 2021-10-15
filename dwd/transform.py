"""
Transformation class
"""


class dwd_transformer:

    def __init__(self):
        pass

    def transform(self, df, start_date, end_date):
        df = df[(df.Jahr >= start_date.year) & (df.Jahr <= end_date.year)]
        df = df.loc[:, ~df.columns.isin(['Unnamed: 19', 'Deutschland'])]
        df = df.groupby(['Jahr', 'Monat']).mean().reset_index()
        return df