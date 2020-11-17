from glob import glob
import os
from datetime import datetime, timedelta
from get_latest_WNF import GetLatestFile
from ActiveWNF_filepath import con_path
import pandas as pd
import numpy as np
from gas_req_con import con_gas_reqt

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
# Loading the CPE gas requirment values into the table
df["BTU Average"] = np.where(df["Supplier"] == "CPE", con_gas_reqt().get('BTU Average'), "")
df["Normalization Adjustment"] = np.where(df["Supplier"] == "CPE", con_gas_reqt().get('Normalization Adjustment'), "")
df["Cold Weather Design Adjustment"] = np.where(df["Supplier"] == "CPE", con_gas_reqt().get('Cold Weather Design Adjustment'), "")
df["Allowance Factor"] = np.where(df["Supplier"] == "CPE", con_gas_reqt().get('Allowance Factor'), "")
df["Normalized & Adjusted (CW Adj) MMBtu/Day"] = np.where(df["Supplier"] == "CPE", con_gas_reqt().get('Normalized & Adjusted (CW Adj) MMBtu/Day'), "")
df
#Write to path
df.to_csv(path_or_buf=con_path())

#print("successful")