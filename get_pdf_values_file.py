from glob import glob
import os
from datetime import datetime, timedelta
from pdf_filepath import get_latest_gas_requirement_file
import pandas as pd
import numpy as np
from tabula import convert_into


def gas_req_dict():
    now = datetime.now()

    year = str(now.year)
    current_month_year = str(now.strftime("%B"))+" "+str(now.year)

    previous_month_name = datetime.now()-timedelta(31)
    previous_month_year = str(
        previous_month_name.strftime("%B"))+" "+str(now.year)

    # Latest file from current month or using the previous month file
    try:
        latest_file = get_latest_gas_requirement_file(year, current_month_year)
    except:
        latest_file = get_latest_gas_requirement_file(
            year, previous_month_year)

    # takes the pdf file and convert to csv
    convert_into(latest_file, "gas_req_file.csv",
                 output_format="csv", pages="all")
    gas_requiremnt_file = pd.read_csv("gas_req_file.csv")

    gas_req_dic = {}
    # Columns swap
    gas_requiremnt_file.columns = gas_requiremnt_file.iloc[2]

    # This area is responsible data cleaning of the csv
    gas_requiremnt_file = gas_requiremnt_file.drop(
        gas_requiremnt_file.index[2])
    masking_nums = np.arange(gas_requiremnt_file.shape[0])
    mask = masking_nums == 2
    gas_requiremnt_file = gas_requiremnt_file[mask]
    # This area is reponsible for mapping the required values of GRF values into a dictionary

    # print(gas_requiremnt_file.head(10))
    gas_req_dic["DeliveryLoadfactor"] = gas_requiremnt_file.iloc[:, 5]
    gas_req_dic["DailyDeliveryRequirement(MMBtu)"] = gas_requiremnt_file.iloc[:, 6]
    gas_req_dic["StaticBTUfactor"] = gas_requiremnt_file.iloc[:, 3]

    return gas_req_dic
