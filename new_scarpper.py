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

# Create an empty list
data_list = []


def scrape():
  # Get all the tables of the page using find_all() method
  soup = BeautifulSoup(browser.page_source, "html.parser")
  
  # Get all the <tr> tags from the table
  table_body = soup.find_all('table')
  print(len(table_body))
  
  #For loop to take out all the <td> tages
  table_rows = table_body[4].find_all('tr')
  for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    #Keep all rows in the list
    data_list.append(row)
    
    Star_names = []
  Distance =[]
  Mass = []
  Radius =[]

  print(temp_list)

  for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
 
# Call Scrape function
scrape()

# Define headers for CSV file
headers = ["Star_name", "Distance", "Mass", "Radius"]

# Create data frame
dwarf_planets = pd.DataFrame(data_list, columns=headers)

# Converts data frame into CSV
dwarf_planets.to_cvs("new_scrapped_data", index=True, index_label="id")
