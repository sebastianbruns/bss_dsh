
import unittest
from datetime import time, datetime
from workinghours.workinghours import working_hours


class Testing(unittest.TestCase):

    FORMAT = "%Y-%m-%d %H:%M:%S"

    def setUp(self):        
         self.wh = working_hours

    def test_given_example1(self):
        """First example, the 15 minutes get ignored"""
        START_DATE = datetime.strptime('2019-12-02 08:00:00', self.FORMAT)
        END_DATE = datetime.strptime('2019-12-04 12:15:00', self.FORMAT)
        hours = working_hours(
            start_date = START_DATE,
            end_date = END_DATE
            )
        self.assertEqual(hours, 19)

    def test_given_example2(self):
        """Second example, where the first and last day are weekends"""
        START_DATE = datetime.strptime('2019-12-01 09:30:00', self.FORMAT)
        END_DATE = datetime.strptime('2019-12-07 12:15:00', self.FORMAT)
        hours = working_hours(
            start_date = START_DATE,
            end_date = END_DATE
            )
        self.assertEqual(hours, 40)

    def test_start_data_before_end_date(self):
        """Function throws an error if start date is after end date"""
        START_DATE = datetime.strptime('2019-11-21 12:00:00', self.FORMAT)
        END_DATE = datetime.strptime('2019-11-12 12:00:00', self.FORMAT)
        self.assertRaises(AssertionError, working_hours, START_DATE, END_DATE)

    def test_one_single_working_day(self):
        """On one single day no day calculations are taking place"""
        START_DATE = datetime.strptime('2021-04-07 08:00:00', self.FORMAT)
        END_DATE = datetime.strptime('2021-04-07 12:00:00', self.FORMAT)
        self.assertEqual(working_hours(START_DATE, END_DATE), 3)

    def test_one_single_weekend_day(self):
        """On single weekend days result is always 0"""
        START_DATE = datetime.strptime('2021-04-17 08:00:00', self.FORMAT)
        END_DATE = datetime.strptime('2021-04-17 12:00:00', self.FORMAT)
        self.assertEqual(working_hours(START_DATE, END_DATE), 0)

    def test_two_working_days(self):
        """Standard case of two normal working days with less work"""
        START_DATE = datetime.strptime('2021-10-12 10:00:00', self.FORMAT)
        END_DATE = datetime.strptime('2021-10-13 16:00:00', self.FORMAT)
        self.assertEqual(working_hours(START_DATE, END_DATE), 14)

    def test_two_days_with_one_weekend_day(self):
        """Two days of which on is a weekend"""
        START_DATE = datetime.strptime('2021-10-17 21:00:00', self.FORMAT)
        END_DATE = datetime.strptime('2021-10-18 18:00:00', self.FORMAT)
        self.assertEqual(working_hours(START_DATE, END_DATE), 8)

    def test_two_days_both_weekend_days(self):
        START_DATE = datetime.strptime('2021-10-16 14:10:00', self.FORMAT)
        END_DATE = datetime.strptime('2021-10-17 17:01:00', self.FORMAT)
        self.assertEqual(working_hours(START_DATE, END_DATE), 0)


if __name__ == '__main__':
    unittest.main()