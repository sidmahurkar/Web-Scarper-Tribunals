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
driver.get("http://atfp.gov.in/judgements.asp")


def get_data_by_date(day, month, year):

	Sr_no, Case_no, Date_of_order, Appellant_name, pdf_link = [], [], [], [], []
	check = 0

	select_day = Select(driver.find_element_by_xpath('//*[@id="DDDate"]'))
	select_day.select_by_visible_text(day)

	select_month = Select(driver.find_element_by_xpath('//*[@id="DDMONTH"]'))
	select_month.select_by_visible_text(month)

	select_year = Select(driver.find_element_by_xpath('//*[@id="DDYEAR"]'))
	select_year.select_by_visible_text(year)

	driver.find_element_by_xpath('//*[@id="FrmJudgement"]/div/div[3]/button').click()

	# to check if there are no records present
	first_row_data = (driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[1]/section/div/div/table/tbody/tr[1]/td')).text

	if (first_row_data == 'There are no records at present'):
		print("Sorry!! There Are No Records At Present")
		print("\n")
		print("Try Entering Different Date")
		check+=1

	else:

		ar = driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[1]/section/div/div/table').get_attribute(('innerHTML'))
		table = BeautifulSoup(ar, "lxml")

		# to ectract all the pdf links present in the respective columns
		for links in table.find_all('a'):

			link = links["href"]
			pdf_link.append("http://atfp.gov.in" + str(link))

		row_count = len(pdf_link)

		# to get the remaining data from the table
		for i in range(1,row_count+1):

			# extract sr.no
			t_data_srno = driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[1]/section/div/div/table/tbody/tr[' + str(i) + ']/td[1]')
			Sr_no.append(t_data_srno.text)

			# extract case_no
			t_data_case_no = driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[1]/section/div/div/table/tbody/tr[' + str(i) + ']/td[2]')
			Case_no.append(t_data_case_no.text)

			# extract date of order
			t_data_doo = driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[1]/section/div/div/table/tbody/tr[' + str(i) + ']/td[3]')
			Date_of_order.append(t_data_doo.text)

			# extract appelant name
			t_data_aname = driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[1]/section/div/div/table/tbody/tr[' + str(i) + ']/td[4]')
			Appellant_name.append(t_data_aname.text)


	return Sr_no, Case_no, Date_of_order, Appellant_name, pdf_link, check

day = '06'
month = 'February'
year = '2018'

Sr_no, Case_no, Date_of_order, Appellant_name, pdf_link, check = get_data_by_date(day, month, year)

if (check==0):
	print("Sr. No.: ", Sr_no)
	print("\n")
	print("Case_no: ", Case_no)
	print("\n")
	print("Date of Order:", Date_of_order)
	print("\n")
	print("Appellant / Respondent Name: ", Appellant_name)
	print("\n")
	print("PDF Links: ", pdf_link)



