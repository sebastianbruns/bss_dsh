



# Task 1:  Data crunching on data from Deutscher Wetterdienst

### Package structure:
```
    dwd/
    |-- __init__.py
    |-- extract.py     The "E" in ETL. Extractors fetch and cache file-based data from online resources.
    |-- pipeline.py    The glue that sticks "E" and "T" together.
    |-- transform.py   The "T" in ETL. Specific transformation logic returning pandas dataframe.
```
### Notebook:
- View source code statuc in [github](dwd.ipynb) or [notebook viewer](https://nbviewer.org/github/sebastianbruns/bss_dsh/blob/master/dwd.ipynb)
- Run the notebook online on [binder](https://mybinder.org/v2/gh/sebastianbruns/bss_dsh/5c9e09bd468407177fe0551d86bcd57feace6040)

# Task 2: Function to calculate working hours


https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/

- Input: A start and an end date 
- Output:  A  pandas  dataframe  of  monthly  mean  air  temperature  per  month  (rows) between start month and end month per federal state (columns).