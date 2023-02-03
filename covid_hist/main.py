import urllib.request


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

    data = urllib.request.urlopen(state_data_url)
    x = 1
    for line in data:
        print(x)
        x += 1
        str_line = line.decode('ascii')
        print(str_line, end='')
    # print(len(list(data)))

    state_data_date_url = 'https://healthdata.gov/resource/j8mb-icvb.csv?$query=SELECT%0A%20%20%60state%60%2C%0A%20%' \
                          '20%60state_name%60%2C%0A%20%20%60state_fips%60%2C%0A%20%20%60fema_region%60%2C%0A%20%20%6' \
                          '0overall_outcome%60%2C%0A%20%20%60date%60%2C%0A%20%20%60new_results_reported%60%2C%0A%20%' \
                          '20%60total_results_reported%60%2C%0A%20%20%60geocoded_state%60%0AWHERE%0A%20%20(%60' \
                          'state_name%60%20IN%20(%22Alabama%22))%0A%20%20AND%20(%60date%60%20%3E%20%222023-01-25T11%' \
                          '3A09%3A54%22%20%3A%3A%20floating_timestamp)'

    state_data_last_month_url = 'https://healthdata.gov/resource/j8mb-icvb.csv?$query=SELECT%0A%20%20%60state%60%2C%' \
                                '0A%20%20%60state_name%60%2C%0A%20%20%60state_fips%60%2C%0A%20%20%60fema_region%60%2' \
                                'C%0A%20%20%60overall_outcome%60%2C%0A%20%20%60date%60%2C%0A%20%20%60new_results_rep' \
                                'orted%60%2C%0A%20%20%60total_results_reported%60%2C%0A%20%20%60geocoded_state%60%0A' \
                                'WHERE%0A%20%20(%60state_name%60%20IN%20(%22Alabama%22))%0A%20%20AND%20(%60date%60%2' \
                                '0%3E%20%222023-01-03T11%3A09%3A54%22%20%3A%3A%20floating_timestamp)%0AORDER%20BY%20' \
                                '%60date%60%20DESC%20NULL%20LAST%2C%20%60overall_outcome%60%20ASC%20NULL%20LAST'
