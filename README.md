# Demonstration of my python skills by solving two coding tasks

## Task 1:  Data crunching on data from Deutscher Wetterdienst

### Package structure:
```
    dwd/
    |-- __init__.py
    |-- extract.py     The "E" in ETL. Extractors fetch and cache file-based data from online resources.
    |-- pipeline.py    The glue that sticks "E" and "T" together.
    |-- transform.py   The "T" in ETL. Specific transformation logic returning pandas dataframe.
```
### Notebook:
- View source code in [github](dwd.ipynb) or [notebook viewer](https://nbviewer.org/github/sebastianbruns/two_tasks/blob/master/dwd.ipynb)
- Run interactively on [binder](https://mybinder.org/v2/gh/sebastianbruns/two_tasks/a3c46e4dd3dfbbace856fb0776db680c70080aa5?filepath=dwd.ipynb)
---
## Task 2: Function to calculate working hours

### Package structure
```
    workinghours/
    |-- __init__.py
    |-- workinghours.py             Contains the function to calculate the working hours
    |-- tests
        |-- __init__.py
        |-- test_workinghours.py    Run the tests for working hours function
```
### Run tests

    python -m unittest discover workinghours/tests/

### Notebook:
- View source code in [github](working_hours.ipynb) or [notebook viewer](https://nbviewer.org/github/sebastianbruns/two_tasks/blob/master/working_hours.ipynb)
- Run interactively on [binder](https://mybinder.org/v2/gh/sebastianbruns/two_tasks/a3c46e4dd3dfbbace856fb0776db680c70080aa5?filepath=working_hours.ipynb)