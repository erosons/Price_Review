from glob import glob
import os
from datetime import datetime

# means all if need specific format then *.csv


def get_latest_file_from_folder(current_year, month_year_of_year):
    list_of_files = glob(os.path.join(
        r'H:\Corp\Dept\Choice\Operations\Transactions\DTE\CenterPoint\WNF', current_year, month_year_of_year, '*.csv'))
    lastest_file = max(list_of_files, key=os.path.getctime)
    return lastest_file


