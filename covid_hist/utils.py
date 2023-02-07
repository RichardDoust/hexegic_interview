import urllib.request
import shutil


def get_state_names() -> list:

    state_names_url = 'https://healthdata.gov/resource/j8mb-icvb.csv?$query=SELECT%20%60state_name%60%2C%20count' \
                  '(%60state_name%60)%20AS%20%60count_state_name%60%20GROUP%20BY%20%60state_name%60'

    state_names_data = urllib.request.urlopen(state_names_url)
    state_names = []
    for line in state_names_data:
        state = line.decode('ascii').replace('"','').split(',')[0]
        state_names.append(state)

    no_header = 1
    return state_names[no_header:]


def zip_output_files(output_folder):
    shutil.make_archive(output_folder, 'zip', output_folder)


if __name__ == '__main__':
    print(get_state_names())
