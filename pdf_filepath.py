from glob import glob
import os
from datetime import datetime

# means all if need specific format then *.csv


def get_latest_gas_requirement_file(current_year, month_year_of_year):
    list_of_files = glob(os.path.join(r'H:\Corp\Dept\Choice\Operations\Transactions\DTE\CenterPoint\Gasrequirement', current_year, month_year_of_year, '*.pdf'))
    lastest_file = max(list_of_files, key=os.path.getctime)
    return lastest_file


