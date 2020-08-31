from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import requests
import csv

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
browser = webdriver.Chrome(executable_path = "/Users/user/Desktop/nopolitics/coronavirus_counts/chromedriver", chrome_options=option)
browser.get("https://www.nccu.edu/coronavirus/confirmed-cases-covid-19-nccu")


results = browser.page_source
soup = BeautifulSoup(results, "html.parser")
table = soup.find("tbody")

#check that this order remains the same on the site
output = [["students", "employees", "subcontractors"]]

for cell in table.find_all('td'):
    text = cell.text.strip()
    output.append(text)
print(output)

# import datetime
# current_date = datetime.datetime.now()
# filename = "nccucases"+str(current_date.strftime("%Y-%m-%d%H:%M"))

# outfile = open(filename + ".csv", "w")
# writer = csv.writer(outfile)
# writer.writerows(output)
browser.close()

