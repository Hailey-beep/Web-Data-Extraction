#Import BeautifulSoup from bs4, time, and pandas
rom selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# Create URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
#browser.get(START_URL)

# Has the program wait for the info from the website to load
time.sleep(10)

# Make a page request using the request module
page = requests.get(START_URL)
print(page)

# Get all the tables of the page using find_all() method
soup = BeautifulSoup(browser.page_source, "html.parser")

# Create an empty list
list = []

# Get all the <tr> tags from the table
def scrape():
  
  table_body = 

  table_data = table_body.
 
#
scrape()

# Define headers for CSV file
header = ["Star_name", "Distance", "Mass", "Radius"]

#
dwarf_planets = pd.DataFrame(list)

# Converts data frame into CSV
dwarf_planets.to_cvs("new_scrapped_data", index=True, index_label="id")
