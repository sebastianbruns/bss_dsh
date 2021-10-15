"""
Pipeline class
This is the glue to stick it all together
"""

import pandas as pd
from dwd import extract, transform

class Pipeline():

    def __init__(self, type='dwd'):
        assert type == 'dwd', 'Currently only [dwd] is implemented.'
        self._extractor = extract.dwd_extractor()
        self._transformer = transform.dwd_transformer()

    def run(self, start_date, end_date):
        assert start_date <= end_date, 'start date {} after end date {}'.format(start_date, end_date)

        data = list()
        for month in list(range(start_date.month, end_date.month+1)):
            tmp = self._extractor.get_file_for_month(month)
            data.append(pd.read_csv(tmp, skiprows=[0], delimiter=";"))

        df = pd.concat(data)

        df_transformed = self._transformer.transform(df, start_date, end_date)

        return df_transformed