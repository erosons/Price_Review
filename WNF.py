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
try:
    latest_file =GetLatestFile().get_latest_file_from_folder(
    year, current_month_year)
except:
    latest_file =GetLatestFile().get_latest_file_from_folder(
    year, previous_month_year)
# Get Latest file from current month
df = pd.read_csv(latest_file, delimiter="|")
df['Month'] = current_month_year
df
# Loading the pdf values into the table
df["DeliveryLoad_Factor"] = np.where(
    df["Unit of Measure"] == "CCF", gas_req_dict().get('DeliveryLoadfactor'), "")

# Values from the lastest GRF pdf file
df['DailyDeliveryRequirement(MMBtu)'] = np.where(
    df["Unit of Measure"] == "CCF", gas_req_dict().get('DailyDeliveryRequirement(MMBtu)'), "")

df['StaticBTUfactor'] = np.where(
    df["Unit of Measure"] == "CCF", gas_req_dict().get("StaticBTUfactor"), "")

# print(df.head(10))

# The old and the recent file are join together
#df2 = pd.read_csv(pathfinder())
#df_update = df.append(df2, ignore_index=True)
#del df_update['Unnamed: 0']

# Update WNF file is created (comprises of recent and previous months files)
mypath = os.path.join(NewPath().wnf_path())
df.to_csv(path_or_buf=mypath)

