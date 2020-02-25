from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
# import datetime
import time
import os

# Specify the path where chromedriver is installed
chrome_path = r"C:\Users\Siddhant Mahurkar\Desktop\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get("http://www.cgatnew.gov.in/catweb/Delhi/services/judgement_status.php")

# driver.find_element_by_xpath('/html/body/fieldset[2]/table/tbody/tr[3]/td[1]/input').send_keys("2020-02-03")


def get_data(date, month, year):

	""" For Selecting the 
		Month Required """

	is_future_month = False
	is_future_year = False

	driver.find_element_by_xpath('/html/body/fieldset[2]/table/tbody/tr[3]/td[1]/input').click()
	current_date = (driver.find_element_by_xpath('//*[@id="ds_calclass"]/table/tbody/tr[2]/td')).text

	cur_date = current_date.split()
	cur_month = cur_date[0]
	cur_year = int(cur_date[1])

	date_dict = {

		'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9, 
        'October' : 10,
        'November' : 11,
        'December' : 12
	}

	cur_month = date_dict[cur_month]
	month_diff = cur_month - (date_dict[month])

	year_diff = cur_year - int(year)

	print(month_diff)

	if(month_diff<0):
		is_future_month = True
		month_diff = -1 * (month_diff)

	for i in range(month_diff):
		if(is_future_month):
			driver.find_element_by_xpath('//*[@id="ds_calclass"]/table/tbody/tr[1]/td[4]').click()
		else:
			driver.find_element_by_xpath('//*[@id="ds_calclass"]/table/tbody/tr[1]/td[2]').click()

	""" For Selecting the 
	    Required Year """

	if(year_diff<0):
		is_future_year = True
		year_diff = -1 * (year_diff)

	for j in range(year_diff):
		if(is_future_year):
			driver.find_element_by_xpath('//*[@id="ds_calclass"]/table/tbody/tr[1]/td[5]').click()
		else:
			driver.find_element_by_xpath('//*[@id="ds_calclass"]/table/tbody/tr[1]/td[1]').click()

	""" For Selecting the
		Required Date """

	columns = driver.find_elements_by_tag_name("td")
	for k in range(len(columns)):
		print(columns[k].text)
		# if (columns[k].text == date ):
			# driver.find_element_by_link_text(date).click()
			# break

	# driver.find_element_by_xpath('//td[text()]="2"')


# //*[@id="ds_calclass"]/table/tbody/tr[5]/td[4]

date = '13'
month = 'January'
year = '2017'

# get_data(date, month, year)