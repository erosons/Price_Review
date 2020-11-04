from glob import glob
import os
from datetime import datetime, timedelta
from get_latest_WNF import GetLatestFile
from ActiveWNF_filepath import NewPath
import pandas as pd
import numpy as np


latest_con_gasReq=GetLatestFile().get_gasreq_con()

df=pd.read_excel(latest_con_gasReq)
print(df.head(10))
