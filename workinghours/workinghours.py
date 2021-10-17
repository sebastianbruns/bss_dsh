"""
Function to calculate working hours.
The working hours are from 9:00:00 to 17:00:00 and working days are Monday to Friday.
"""

from pandas import bdate_range, Timestamp

def working_hours(start_date, end_date):

    assert start_date < end_date, "end date is before start date"

    date_range = bdate_range(
        Timestamp(start_date),
        Timestamp(end_date),
        freq="BH",
        closed="left",
        normalize=False
        )

    # dont consider incomplete working hours
    offset = 1 if end_date.weekday() not in [5,6] and end_date.time().minute > 0 else 0

    return date_range.to_series().count()-offset