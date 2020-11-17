from glob import glob
import os
from datetime import datetime, timedelta
from get_latest_WNF import GetLatestFile
import pandas as pd
import numpy as np


def con_gas_reqt():
    latest_con_gasReq=GetLatestFile().get_gasreq_con()

    df=pd.read_excel(latest_con_gasReq)
    #print(df.head(10))
    Con_gas_req_dic = {}
    # Columns swap
    df.columns = df.iloc[4]
    #print(df)
    #get the first part of the table
    df1=df.iloc[:3,5:]
    #print(df1)
    # Used the shape of the dataframe to create a number to be used for index in masking the table
    df.shape
    mask=np.arange(df.shape[0])
    mask_num=mask==5
    # created a new table with the mask 
    df2=df[mask_num]
    #print(df2)
    # Filling the map the dictioning to the tables above
    Con_gas_req_dic["BTU Average"] = df1.iloc[1,0]
    Con_gas_req_dic["Normalization Adjustment"] = df1.iloc[1,0]
    Con_gas_req_dic["Cold Weather Design Adjustment"] = df1.iloc[2,0]
    Con_gas_req_dic["Allowance Factor"] = df2.iloc[0,5]
    Con_gas_req_dic["Normalized & Adjusted (CW Adj) MMBtu/Day"] = df2.iloc[0,6]
    
    return Con_gas_req_dic