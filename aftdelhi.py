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
driver.get("http://aftdelhi.nic.in/index.php?option=com_casetracking&view=judgement&layout=date&Itemid=35")

def get_data(from_date, from_month, from_year, to_date, to_month, to_year):


	item_no, case_no, case_title, judgement_date, head_notes, connected_cases, pdf_link = [], [], [], [], [], [], []


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

	fromd = from_date + '-' + from_month + '-' + from_year
	tod = to_date + '-' + to_month + '-' + to_year

	
	driver.execute_script("document.getElementsByName('search_date')[0].value= '{}' ".format(fromd))
	driver.execute_script("document.getElementsByName('search_date_to')[0].value= '{}' ".format(tod))

	driver.find_element_by_xpath('//*[@id="ja-content"]/form/table/tbody/tr[1]/td[5]/input').click()

	ar = driver.find_element_by_xpath('//*[@id="ja-content"]/table').get_attribute(('innerHTML'))
	table = BeautifulSoup(ar, "lxml")

	for links in table.find_all('a'):

		link = links["href"]
		pdf_link.append("http://aftdelhi.nic.in/" + link)

	row_count = len(pdf_link)

	for i in range(1,row_count+1):

		y = (driver.find_element_by_xpath('//*[@id="ja-content"]/table/tbody/tr[' + str(i) + ']/td[1]')).text
		item_no.append(y)

		z = (driver.find_element_by_xpath('//*[@id="ja-content"]/table/tbody/tr[' + str(i) + ']/td[2]')).text
		case_no.append(z)

		w = (driver.find_element_by_xpath('//*[@id="ja-content"]/table/tbody/tr[' + str(i) + ']/td[3]')).text
		case_title.append(w)

		q = (driver.find_element_by_xpath('//*[@id="ja-content"]/table/tbody/tr[' + str(i) + ']/td[4]')).text
		judgement_date.append(q)

		x = (driver.find_element_by_xpath('//*[@id="ja-content"]/table/tbody/tr[' + str(i) + ']/td[5]')).text
		head_notes.append(x)

		f = (driver.find_element_by_xpath('//*[@id="ja-content"]/table/tbody/tr[' + str(i) + ']/td[6]')).text
		connected_cases.append(f)

	dictionary = [ {"Item No." : val[0], 
					"Case No." : val[1], 
					"Case Title	" : val[2], 
					"Judgement Date" : val[3],
					"Head Notes" : val[4],
					"Connected Cases" : val[5],
					"PDF Links" : val[6] } for val in zip(item_no, case_no, case_title, judgement_date, head_notes, connected_cases, pdf_link) ]

	return dictionary

from_date = '01'
from_month = 'January'
from_year = '2020'

to_date = '08'
to_month = 'March'
to_year = '2020'

dictionary = get_data(from_date, from_month, from_year, to_date, to_month, to_year)
print(dictionary)