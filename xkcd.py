from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import date
import pandas as pd 
import time
import re
import csv

# first imports selenium and brings in webdriver 
# second import lauches a browser
# third import allos you to search for things with parameters
# fourth import allows you to wait for the page to load 
# fifth import allows you to specify what you are looking for 
# sixth allows you to handle a timout situation 


medium_data = open('medium_data.csv', 'w', encoding='utf-8')
writer = csv.writer(medium_data)
news_dict = {}
#create column for dictionary
news_dict['title'] = 'title'
news_dict['author_name'] = 'author_name'
news_dict['date'] = 'date'
news_dict['likes'] = 'likes'
news_dict['comments'] = 'comments'
news_dict['categories_list'] = 'categories_list'
news_dict['type'] = 'type_of_story'
#add all title column created above to the first row of the csv file
writer.writerow(news_dict.values())


SCROLL_PAUSE_TIME = 4

#driver = webdriver.Chrome()

topics = ['https://xkcd.com/archive/',
'https://what-if.xkcd.com/archive/']
driver = webdriver.Chrome('/Users/Sausa08/Downloads/chromedriver')

#/Users/Sausa08/Downloads/Developer

for url in topics:

	driver.get(url)

	last_height = driver.execute_script("return document.body.scrollHeight")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(SCROLL_PAUSE_TIME)
	new_height = driver.execute_script("return document.body.scrollHeight")

	# while True: 	
	# 	if new_height != last_height:
	# 		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 		time.sleep(SCROLL_PAUSE_TIME)
	# 		last_height = new_height
	# 		new_height = driver.execute_script("return document.body.scrollHeight")
	# 	else:
	# 		break

	#blocks = driver.find_elements_by_xpath('//section[@class = "n o p fi r c"]')
	links = driver.find_elements_by_xpath('//div[@class="archive-wrapper"]/div')
	links = [link.get_attribute('class') for link in links]
	print(len(links))
	print(links)
	#for item in blocks:
	for link in links:
		news_dict = {}

		author_name = "Randall Munroe"

		try: 
			date = driver.find_element_by_tag_name('h2').text
		except:
			date = "NA"
		try:
			title = driver.find_element_by_tag_name('h1').text
		except:
			title = "NA"
		print(title)
		
		likes = "NA"
		
		comments = "NA"
		try: 
			categories_list = driver.find_element_by_xpath('//div[@class="archive-entry"]/a').text
		except:
			categories_list = "NA"
		try:
			type_of_story = driver.find_element_by_tag_name('h3').text
		except:
			type_of_story = "NA"
		
		news_dict['title'] = title
		news_dict['author_name'] = author_name
		news_dict['date'] = date
		news_dict['likes'] = likes
		news_dict['comments'] = comments
		news_dict['categories_list'] = categories_list
		news_dict['type'] = 'type_of_story'
		writer.writerow(news_dict.values())

		driver.execute_script("window.history.go(-1)")



		





