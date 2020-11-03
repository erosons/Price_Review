from glob import glob
import os
from datetime import datetime

# means all if need specific format then *.csv


def get_latest_file_poolfile():
    list_of_files = glob(os.path.join(r'C:\Users\00936124\downloads', '*.csv'))
    lastest_file = max(list_of_files, key=os.path.getctime)
    return lastest_file
