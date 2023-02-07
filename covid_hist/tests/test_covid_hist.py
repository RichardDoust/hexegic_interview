from unittest import TestCase
from covid_hist.main import StateData


class TestCovidHistStateData(TestCase):

    def test_get_last_month(self):
        state_data_alabama = StateData('Alabama')
        date = state_data_alabama._get_last_month()
        year = int(date.split('-')[0])
        self.assertGreater(year, 2022)
