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
driver.get("http://sat.gov.in/scripts/search.asp")


def get_data(year, month):

	date, appeal_no, ma_ra_no, title, pdf_link = [],[],[],[],[]

	select_year = Select(driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/p/font/select[1]'))
	select_year.select_by_visible_text(year)

	select_month = Select(driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/p/font/select[2]'))
	select_month.select_by_visible_text(month)

	driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/p/font/input').click()

	a = []
	ar = driver.find_element_by_xpath('//*[@id="form1"]/table').get_attribute(('innerHTML'))
	table = BeautifulSoup(ar, "lxml")
	# for tr in table.find_all('tr'):
	# 	a.append(tr)

	for links in table.find_all('a'):


		link = links["href"]
		link = link[2:]

		pdf_link.append("http://sat.gov.in" + str(link))
		title.append(links.text)

	row_count = len(title)
	# t_data = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[4]/td[1]')
	# t_data = t_data.text

	# for i in range(4,(((row_count+1)*2)+2),2):

	for i in range(4,(4 + (row_count)*2)+1,2):


		t_data_date = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[' + str(i) + ']/td[1]')
		date.append(t_data_date.text)

		t_data_appeal = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[' + str(i) + ']/td[2]')
		appeal_no.append(t_data_appeal.text)

		t_data_mara = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[' + str(i) + ']/td[3]')
		ma_ra_no.append(t_data_mara.text)


	return date, appeal_no, ma_ra_no, title, pdf_link 
# //*[@id="form1"]/table/tbody/tr[4]
# //*[@id="form1"]/table/tbody/tr[100]/td[2]
# //*[@id="form1"]/table/tbody/tr[120]/td[2]
# //*[@id="form1"]/table/tbody/tr[122]/td[2]
# //*[@id="form1"]/table/tbody/tr[78]/td[2]

date, appeal_no, ma_ra_no, title, pdf_link = get_data('2018', 'March')

print(date)
# print(len(date))
print("\n")
print(appeal_no)
# print(len(appeal_no))
print("\n")
print(ma_ra_no)
# print(len(ma_ra_no))
print("\n")
print(title)
# print(len(title))
print("\n")
print(pdf_link)
print(len(pdf_link))
	