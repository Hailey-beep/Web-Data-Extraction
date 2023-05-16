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
browser.get(START_URL)

# Has the program wait for the info from the website to load
time.sleep(10)

# Make a page request using the request module
page = request.get(hyperlink)

# Get all the tables of the page using find_all() method


# Create an empty list
list = []

# Get all the <tr> tags from the table

