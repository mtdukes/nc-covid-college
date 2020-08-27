#NCSU COVID-19 dashboard scraper
#A simple scraper to gather data from
#North Carolina State University's COVID-19
#data dashboard, located at
#https://www.ncsu.edu/coronavirus/testing-and-tracking/
#
#Built by @mtdukes

#import libraries
import sys, csv, json, requests
#import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import argparse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#main scraper function
#takes a destination file name
#and a url to scrape as arguments
def scrape_function(url):
	#define our field layout
	header = ['id',
	'institution',
	'date_current',
	'date_captured',
	'new_cases_students',
	'new_cases_staff',
	'new_cases_total',
	'new_def_cases',
	'total_cases_students',
	'total_cases_staff',
	'total_cases_total',
	'new_tests',
	'new_positive',
	'new_positive_rate',
	'new_def_tests',
	'total_tests',
	'total_positive',
	'total_positive_rate']
	#define our known fields
	college_id = 7
	institution = 'North Carolina State University'
	date_captured = datetime.now().strftime("%Y-%m-%d %H:%M")
	file_date = datetime.now().strftime("%Y%m%d%H%M")
	new_def_cases = 1
	new_def_tests = 7
	data_row = []
	csv_file = str(college_id) + '_' + file_date + '.csv'
	data_directory = '../data/'

	#initialize and provide webdriver options
	option = webdriver.ChromeOptions()
	option.add_argument(" - incognito")
	#specify browser
	browser = webdriver.Chrome(options=option)
	#pull up the page
	browser.get(url)
	#store the source code from the rendered web page
	results = browser.page_source
	#establish a BS instance using the results from the source code
	soup = BeautifulSoup(results, "html.parser")
	try:
		#locate all the tables in the HTML
		tables = soup.find_all("table")
		#assign the tables to their appropriate variables for retrieval
		case_table = tables[0]
		total_testing = tables[1]
		weekly_testing = tables[2]
		#grab the header, which currently displays the date of new cases
		case_header = case_table.find_all('th')[1].text
		#clean up the text and extract the date, adding the year
		case_date = case_header.replace('Daily New Cases', '').strip() + datetime.now().strftime("%Y")
		#reformat the date to fit our data
		date_current = datetime.strptime(case_date, '%b. %d%Y').strftime("%Y-%m-%d")

		#process the 'positive case tracking' table
		for row in case_table.find_all('tr'):
			for cell in row.find_all('td'): 
				if(cell.text.strip().lower() == 'students'):
					new_cases = cell.next_sibling.next_sibling
					total_cases = new_cases.next_sibling.next_sibling
					new_cases_students = new_cases.string
					total_cases_students = total_cases.string
				elif(cell.text.strip().lower() == 'employees'):
					new_cases = cell.next_sibling.next_sibling
					total_cases = new_cases.next_sibling.next_sibling
					new_cases_staff = new_cases.string
					total_cases_staff = total_cases.string
				elif(cell.text.strip().lower() == 'total'):
					new_cases = cell.next_sibling.next_sibling
					total_cases = new_cases.next_sibling.next_sibling
					new_cases_total = new_cases.string
					total_cases_total = total_cases.string

		#process the 'cumulative testing' table
		for row in total_testing.find_all('tr'):
			for cell in row.find_all('td'):
				if(cell.text.strip().lower() == 'total'):
					total_tests = cell.next_sibling.next_sibling
					unparsed_results = total_tests.next_sibling.next_sibling.string.split()
					total_tests = total_tests.string
					total_positive = unparsed_results[0]
					total_positive_rate = unparsed_results[1].replace('(','').replace('%)','')

		#process the 'weekly testing' table
		for row in weekly_testing.find_all('tr'):
			for cell in row.find_all('td'):
				if(cell.text.strip().lower() == 'total'):
					new_tests = cell.next_sibling.next_sibling
					unparsed_results = new_tests.next_sibling.next_sibling.string.split()
					new_tests = new_tests.string
					new_positive = unparsed_results[0]
					new_positive_rate = unparsed_results[1].replace('(','').replace('%)','')

		data_row = [college_id,
		institution,
		date_current,
		date_captured,
		new_cases_students,
		new_cases_staff,
		new_cases_total,
		new_def_cases,
		total_cases_students,
		total_cases_staff,
		total_cases_total,
		new_tests,
		new_positive,
		new_positive_rate,
		new_def_tests,
		total_tests,
		total_positive,
		total_positive_rate]

	except:
		print('ERROR!')

	#close the browser
	browser.close()
	#open a new csv using the entered file name
	writer = csv.writer(open(data_directory + csv_file, 'w'))
	writer.writerow(header)
	print('New file created...')
	writer.writerow(data_row)
	print('Row written ...')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Download data from the NCSU college dashboard')
	parser.add_argument('path',help='Enter the url to scrape')
	args = parser.parse_args()
	
	scrape_function(args.path)
	
	print('...done')