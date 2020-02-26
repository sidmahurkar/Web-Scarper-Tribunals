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

def get_data(from_date, from_month, from_year, to_date, to_month, to_year):

	sr_no, second_column, third_column, fourth_column, date, pdf_link = [], [], [], [], [], []
	count = 0

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


	input_field_from = driver.find_element_by_xpath('/html/body/fieldset[3]/table/tbody/tr/td[1]/input')
	input_field_from.send_keys(from_year + '-' + from_month + '-' + from_date)

	input_field_to = driver.find_element_by_xpath('/html/body/fieldset[3]/table/tbody/tr/td[2]/input')
	input_field_to.send_keys(to_year + '-' + to_month + '-' + to_date)

	driver.find_element_by_xpath('/html/body/fieldset[3]/table/tbody/tr/td[3]/input').click()

	ar = driver.find_element_by_xpath('/html/body/table[6]').get_attribute(('innerHTML'))
	table = BeautifulSoup(ar, "lxml")

	a = []
	for links in table.find_all('a'):

		link = links["href"]
		a.append("http://cgatnew.gov.in" + link)

	row_count = len(a)
	# print(row_count)

	for i in range(1,row_count+3):

		x = (driver.find_element_by_xpath('/html/body/table[6]/tbody/tr[' + str(i) + ']/td[1]')).text
		if (x == 'FINAL ORDER'):
			fin_order_index = i
		elif (x == 'ORAL ORDER'):
			or_order_index = i
		sr_no.append(x)

	for i in range(1,row_count+3):
		if (i == fin_order_index):
			second_column.append('FINAL ORDER')
			third_column.append('FINAL ORDER')
			fourth_column.append('FINAL ORDER')
			date.append('FINAL ORDER')
			pdf_link.append('FINAL ORDER')
			pass
		elif (i == or_order_index):
			second_column.append('ORAL ORDER')
			third_column.append('ORAL ORDER')
			fourth_column.append('ORAL ORDER')
			date.append('ORAL ORDER')
			pdf_link.append('ORAL ORDER')
			pass

		else:
			y = (driver.find_element_by_xpath('/html/body/table[6]/tbody/tr[' + str(i) + ']/td[2]')).text
			# print(y)
			second_column.append(y)

			z = (driver.find_element_by_xpath('/html/body/table[6]/tbody/tr[' + str(i) + ']/td[3]')).text
			third_column.append(z)

			w = (driver.find_element_by_xpath('/html/body/table[6]/tbody/tr[' + str(i) + ']/td[4]')).text
			fourth_column.append(w)

			q = (driver.find_element_by_xpath('/html/body/table[6]/tbody/tr[' + str(i) + ']/td[5]')).text
			date.append(q)

			pdf_link.append(a[count])
			count+=1


			# Making a Array of Dictionaries of all the lists obtained.
			dictionary = [ {"Sr. No" : val[0], 
							"Sec. Column" : val[1], 
							"Third Column" : val[2], 
							"Fourth Column" : val[3],
							"Date" : val[4],
							"PDF Link" : val[5] } for val in zip(sr_no, second_column, third_column, fourth_column, date, pdf_link) ]

	# print(len(second_column))

	return dictionary


# http://cgatnew.gov.in/catweb/madrasnew/order_files/final/2019/December/263310022512019_1.pdf

# If the date in two digits only. ( for ex => for)
from_date = '01'
from_month = 'February'
from_year = '2020'

to_date = '08'
to_month = 'February'
to_year = '2020'

dictionary = get_data(from_date, from_month, from_year, to_date, to_month, to_year)

print(dictionary)


