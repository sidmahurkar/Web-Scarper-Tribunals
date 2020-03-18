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
driver.get("http://www.tdsat.gov.in/Delhi/services/judgment.php")

def get_data(from_date, from_month, from_year, to_date, to_month, to_year):

	sr_no, case_no, member_name, party_detail, order_date, pdf_link = [], [], [], [], [], []
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


	fromd = from_date + '/' + from_month + '/' + from_year
	tod = to_date + '/' + to_month + '/' + to_year

	driver.execute_script("document.getElementsByName('from_date1')[0].value= '{}' ".format(fromd))
	driver.execute_script("document.getElementsByName('to_date1')[0].value= '{}' ".format(tod))

	driver.find_element_by_xpath('//*[@id="submit1"]').click()

	row_count = len(driver.find_elements_by_xpath('/html/body/form[3]/fieldset/div/table/tbody/tr'))
	# print(row_count)

	ar = driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table').get_attribute(('innerHTML'))
	table = BeautifulSoup(ar, "lxml")

	for links in table.find_all('a'):

		link = links["href"]
		pdf_link.append("http://www.tdsat.gov.in/" + link)

	x = len(pdf_link)
	# print(x)

	for i in range(2,row_count+1):

		y = (driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table/tbody/tr[' + str(i) + ']/td[1]')).text
		sr_no.append(y)

		z = (driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table/tbody/tr[' + str(i) + ']/td[2]')).text
		case_no.append(z)

		w = (driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table/tbody/tr[' + str(i) + ']/td[3]')).text
		member_name.append(w)

		q = (driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table/tbody/tr[' + str(i) + ']/td[4]')).text
		party_detail.append(q)

		x = (driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table/tbody/tr[' + str(i) + ']/td[5]')).text
		order_date.append(x)

	dictionary = [ {"Serial No." : val[0], 
					"Case No." : val[1], 
					"Member Name" : val[2], 
					"Party Detail" : val[3],
					"Order Date" : val[4],
					"Download" : val[5] } for val in zip(sr_no, case_no, member_name, party_detail, order_date, pdf_link) ]

	return dictionary


from_date = '01'
from_month = 'April'
from_year = '2019'

to_date = '01'
to_month = 'March'
to_year = '2020'

data = get_data(from_date, from_month, from_year, to_date, to_month, to_year)

if(len(data) == 0):
	print("No Records Found")
else:
	print(data)