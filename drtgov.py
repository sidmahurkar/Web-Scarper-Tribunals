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
driver.get("https://drt.gov.in/front/drat_orderparty.php")

def get_data(drat, order, from_day, from_month, from_year, to_day, to_month, to_year):

	sr_no, diary_no, case_no, order_date, applicant, respondent, judge_name, pdf_link = [],[],[],[],[],[],[],[]

	month_dict = {

		'January' : '01',
        'February' : '02',
        'March' : '03',
        'April' : '04',
        'May' : '05',
        'June' : '06',
        'July' : '07',
        'August' : '08',
        'September' : '09', 
        'October' : '10',
        'November' : '11',
        'December' : '12'
	}

	from_month = month_dict[from_month]
	to_month = month_dict[to_month]

	fromd = from_day + '/' + from_month + '/' + from_year
	tod = to_day + '/' + to_month + '/' + to_year

	select_drat = Select(driver.find_element_by_xpath('/html/body/div[1]/div/form/div[2]/div[1]/select'))
	select_drat.select_by_visible_text(drat)

	select_order = Select(driver.find_element_by_xpath('/html/body/div[1]/div/form/div[2]/div[2]/select'))
	select_order.select_by_visible_text(order)

	driver.execute_script("document.getElementsByName('from_date1')[0].value= '{}' ".format(fromd))
	driver.execute_script("document.getElementsByName('to_date1')[0].value= '{}' ".format(tod))

	driver.find_element_by_xpath('//*[@id="submit1"]').click()

	row_count = len(driver.find_elements_by_xpath('//*[@id="myTable"]/tbody/tr'))
	print(row_count)

	ar = driver.find_element_by_xpath('//*[@id="myTable"]').get_attribute(('innerHTML'))
	table = BeautifulSoup(ar, "lxml")

	for links in table.find_all('a'):

		link = links["href"]
		pdf_link.append("https://drt.gov.in/" + link[2:])

	x = len(pdf_link)
	print(x)

	for i in range(1,row_count+1):

		y = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[1]')).text
		sr_no.append(y)

		z = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[2]')).text
		diary_no.append(z)

		w = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[3]')).text
		case_no.append(w)

		q = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[4]')).text
		order_date.append(q)

		x = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[5]')).text
		applicant.append(x)

		f = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[6]')).text
		respondent.append(f)

		e = (driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[' + str(i) + ']/td[7]')).text
		judge_name.append(e)

	dictionary = [ {"Sl. No." : val[0], 
					"Diary No." : val[1], 
					"Case No." : val[2], 
					"Date of Order" : val[3],
					"Applicant" : val[4],
					"Respondent" : val[5],
					"Judge Name" : val[6],
					"DRAT Daily Orders" : val[7] } for val in zip(sr_no, diary_no, case_no, order_date, applicant, respondent, judge_name, pdf_link) ]

	return dictionary

# options are: (allahabad, chennai, delhi, kolkata, mumbai)
drat = "DEBT RECOVERY APPELLATE TRIBUNAL - ALLAHABAD"

# options are: (daily order, final  order)
order = "Daily Order"

from_day = "08"
from_month = "February"
from_year = "2020"

to_day = "28"
to_month = "February"
to_year = "2020"

data = get_data(drat, order, from_day, from_month, from_year, to_day, to_month, to_year)

if(len(data) == 0):
	print("No Records Found")
else:
	print(data)