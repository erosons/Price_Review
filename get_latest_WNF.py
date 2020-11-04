from glob import glob
import os
from datetime import datetime

# means all if need specific format then *.csv

class GetLatestFile():

    def get_latest_file_from_folder(self,current_year, month_year_of_year):
        list_of_files = glob(os.path.join(
            r'H:\Corp\Dept\Choice\Operations\Transactions\DTE\CenterPoint\WNF', current_year, month_year_of_year, '*.csv'))
        lastest_file = max(list_of_files, key=os.path.getctime)
        return lastest_file

    def get_latest_file_from_Con_folder(self,current_year):
        list_of_files = glob(os.path.join(
            r'H:\Corp\Dept\Choice\Operations\Transactions\CMS\CON_Files', current_year,'*.xlsx'))
        lastest_file = max(list_of_files, key=os.path.getctime)
        return lastest_file

    def get_gasreq_con(self):
        list_of_files = glob(os.path.join(
            r'H:\Corp\Dept\Choice\Operations\Transactions\CMS\GasRequirementFile','*.xlsx'))
        lastest_file = max(list_of_files, key=os.path.getctime)
        return lastest_file




