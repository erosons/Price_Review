from glob import glob
import os
from datetime import datetime, timedelta
from get_latest_WNF import GetLatestFile
from ActiveWNF_filepath import NewPath
import pandas as pd
import numpy as np
from get_pdf_values_file import gas_req_dict

# Current month creation e.g October 2020
now = datetime.now()
year = str(now.year)
current_month_year = str(now.strftime("%B"))+" "+str(now.year)

# Previous month creation e.g September 2020
previous_month_name = datetime.now()-timedelta(31)
previous_month_year = str(previous_month_name.strftime("%B"))+" "+str(now.year)



# Get the latest file from dir and when there is no current use the previous month last updated file

latest_file =GetLatestFile().get_latest_file_from_Con_folder(year)

# Get Latest file from current month
df = pd.read_excel(latest_file)
df['Month'] = current_month_year
print(df)