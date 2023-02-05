import urllib.request
import datetime
import dateutil.relativedelta
import io
import pandas as pd


class StateData(object):
    def __init__(self, state_name):
        self.state_name = state_name

    @staticmethod
    def _get_last_month() -> str:
        today = datetime.date.today()
        last_month = today - dateutil.relativedelta.relativedelta(months=1)
        last_month_str = last_month.strftime("%Y-%m-%d")

        return last_month_str

    def _get_last_months_url(self) -> str:

        last_month = self._get_last_month()

        state_data_last_month_url = f'https://healthdata.gov/resource/j8mb-icvb.csv?$query=SELECT%0A%20%20%60state' \
                                    f'%60%2C%0A%20%20%60state_name%60%2C%0A%20%20%60state_fips%60%2C%0A%20%20%60fe' \
                                    f'ma_region%60%2C%0A%20%20%60overall_outcome%60%2C%0A%20%20%60date%60%2C%0A%20' \
                                    f'%20%60new_results_reported%60%2C%0A%20%20%60total_results_reported%60%2C%0A%' \
                                    f'20%20%60geocoded_state%60%0AWHERE%0A%20%20(%60state_name%60%20IN%20(%22' \
                                    f'{self.state_name}%22))%0A%20%20AND%20(%60date%60%20%3E%20%22{last_month}T11%' \
                                    f'3A09%3A54%22%20%3A%3A%20floating_timestamp)%0AORDER%20BY%20%60date%60%20DESC' \
                                    f'%20NULL%20LAST%2C%20%60overall_outcome%60%20ASC%20NULL%20LAST'

        return state_data_last_month_url

    def get_last_months_data(self):
        data = urllib.request.urlopen(self._get_last_months_url())
        output = io.StringIO()
        for line in data:
            output.write(line.decode('ascii'))
            print(line)

        output.seek(0)
        output_df = pd.read_csv(output)
        print(output_df)

        return output_df

    def get_last_five_days_data(self):



if __name__ == '__main__':
    target_url = 'https://healthdata.gov/resource/j8mb-icvb.csv?$query=SELECT%0A%20%20%60state%60%2C%0A%20%20%60' \
                 'state_name%60%2C%0A%20%20%60state_fips%60%2C%0A%20%20%60fema_region%60%2C%0A%20%20%60overall_' \
                 'outcome%60%2C%0A%20%20%60date%60%2C%0A%20%20%60new_results_reported%60%2C%0A%20%20%60total_' \
                 'results_reported%60%2C%0A%20%20%60geocoded_state%60'


    state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                   "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana",
                   "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Marshall Islands", "Maryland", "Massachusetts",
                   "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
                   "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands",
                   "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina",
                   "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia",
                   "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    state_data_url = 'https://healthdata.gov/resource/j8mb-icvb.csv?$query=SELECT%0A%20%20%60state%60%2C%0A%20%20%60' \
                     'state_name%60%2C%0A%20%20%60state_fips%60%2C%0A%20%20%60fema_region%60%2C%0A%20%20%60overall_' \
                     'outcome%60%2C%0A%20%20%60date%60%2C%0A%20%20%60new_results_reported%60%2C%0A%20%20%60' \
                     'total_results_reported%60%2C%0A%20%20%60geocoded_state%60%0AWHERE%20%60state_name' \
                     '%60%20IN%20(%22Alabama%22)'


    cov_data = StateData('Alabama')
    print(cov_data.state_name)
    print(cov_data._get_last_months_url())
    cov_data.get_last_months_data()
