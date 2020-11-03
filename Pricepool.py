from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_latest_poolprice import get_latest_file_poolfile
from pathlib import Path
import os
from Iam import iam
import pandas as pd
import time



browser = webdriver.Chrome()

browser.get("https://ceschoice.herokuapp.com/")


Username_box = browser.find_element_by_id("user_email")
Username_box.send_keys(iam().get("username"))
passwordbox = browser.find_element_by_id("user_password")
passwordbox.send_keys(iam().get("password"))
passwordbox.submit()
#continue_link = browser.find_element_by_link_text('reports/price_pool_report').click()

#Execute Report dropdown click

browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[8]/a").click()

#Execute the Price pool click
browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[8]/ul/li[2]/a").click()

time.sleep(5)

#Execute the All Utilities click
#browser.find_element_by_xpath("//*[@id='utility_id']").click()
browser.find_element_by_id("utility_id").click()

# Excute the CA-Pacific Gas & Electric click
browser.find_element_by_xpath("//*[@id='utility_id']/option[2]").click()

time.sleep(5)

# Execute the Export All Price Pools 
try:
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'export_button')))
finally:
    browser.find_element_by_xpath("//*[@id='export_button']").click()

# accepts the Dialogue box pop up
Alert(browser).accept()

#The program wait for the download to execute
time.sleep(45)

#Execute Operations dropdown click
browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[7]/a").click()

# This clicks the file export , however waits for the AJAX to load it
try:
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'navbar-collapse')))
finally:
    browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[7]/ul/li[10]/a").click()

time.sleep(20)

options=webdriver.ChromeOptions()
preferences={"download.default_directory":Path(r'C:\Users\c_seromonsei\Desktop\downloads'),"safebrowsing.enabled":"false"}
options.add_experimental_option("prefs",preferences)
browser.get('https://ceschoice.herokuapp.com/export_files')

browser.find_element_by_xpath("//*[@class='container']/table/tbody/tr[1]/td[1]/a").click()


time.sleep(10)

browser.close()


#Getting and writing a fresh data to path

df=pd.read_csv(get_latest_file_poolfile())
df["Utility-Pool01"]=df["Utility"]+ df["Pool"]
df["Utility-Pool"]=df["Utility"]+ df["Pool"].str.lstrip("0")
mypath = os.path.join(r"H:\Corp\Dept\Choice\Analytics\Samson","pricepool.csv")
df.to_csv(path_or_buf=mypath,encoding="utf-8", sep=",")