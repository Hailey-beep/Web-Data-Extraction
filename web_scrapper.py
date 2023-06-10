#Import BeautifulSoup from bs4, time, and pandas
from bs4 import BeautifulSoup as soup
import time
import pandas as pd

#Initialise the webdriver to open website
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(URL)

#Make a 10 millisecond delay for the url to load
time.sleep(10)

#Create an empty list for scraped data
scraped_data = []

#Create function to scrape data from the url about the stars
def scrape():
    ##The 

    #Fins <table>
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    #
    table_body = bright_star_table.find('tbody')

    #
    table_rows = table_body.find_all('tr')
    
    #Get all data from <td>
    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        
        print(table_cols)

        for col_data in table_cols:
            #Removes Extra white spaces using strip() method
            data = col_data.text.strip()
            print(data)

            #adds data from each row to list
            temp_list.append(data)

        #Append leisted data to star data list
        scraped_data.append(temp_list)

    #

    stars_data = []

    if i in range(0,len(scraped_data)):
        
        star_names = scraped_data[i,1]
        distance = scraped_data[i,3]
        mass = scraped_data[i,5]
        radius = scraped_data[i,6]
        lum = scraped_data[i,7]

        required_data = [star_names, distance, mass, radius, lum]
        stars_data.apprend(required_data)

# Call the function to scrape data
scrape()

# Define Header for data
headers = ['star_name','distance', 'mass', 'radius', 'luminosity']

# Define a data frame using pandas
star_df_1 = pd = pd.DataFrame(stars_data, columns=headers)

#convert the data frame into CSV
star_df_1.tocsv('scraped_data.cv', index=True, index_label="id")
