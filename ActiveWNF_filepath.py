import os
from pathlib import Path
import pandas as pd


class NewPath:

    def wnf_path(self):
        mypath=os.path.join(r"H:\Corp\Dept\Choice\Operations\Transactions\DTE\CenterPoint\WNF_csv_format",'WNF.csv')
        return mypath



    def con_path(self):
        mypath=os.path.join(r"H:\Corp\Dept\Choice\Operations\Transactions\CMS\Tableau_Con_Files",'CON.csv')
        return mypath


