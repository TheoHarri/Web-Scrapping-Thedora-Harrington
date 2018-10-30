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


oatmeal = open('oatmeal.csv', 'w', encoding='utf-8')
writer = csv.writer(oatmeal)
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

topics = ['http://theoatmeal.com/tag/animals', 
'http://theoatmeal.com/tag/cats',
'http://theoatmeal.com/tag/grammar',
'http://theoatmeal.com/tag/food',
'http://theoatmeal.com/tag/tech']

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

	
	links = driver.find_elements_by_xpath('//div[@class="pad2"]/ul/li/div[@class="bg_comic"]/a')
	links = [link.get_attribute('href') for link in links]
	print(len(links))
	print(links)
	#for item in blocks:
	for link in links:
		driver.get(link)
		news_dict = {}

		author_name = 'Matthew Innman'

		try: 
			date = driver.find_element_by_tag_name('head')
		except:
			date = "N/A"
		try:
			title = driver.find_element_by_xpath('//div[@class="bg_comic"]/a/alt').text
		except:
			title = "N/A"
		print(title)
		
		try: 
			likes = driver.find_element_by_xpath('//div[@class="more2016"]/').text
		except:
			likes = "N/A"
		
		try: 
			comments = driver.find_element_by_xpath('//div[@class="clear"]').text
		except: 
			comments = "N/A"
		
		try: 
			categories_list = driver.find_element_by_xpath('//div[@class="ghost"]').text
		except:
			categories_list = "na"

		type_of_story = driver.find_element_by_xpath('//div[@class="tag_nav"]').text


		
		news_dict['title'] = title
		news_dict['author_name'] = author_name
		news_dict['date'] = date
		news_dict['likes'] = likes
		news_dict['comments'] = comments
		news_dict['categories_list'] = categories_list
		news_dict['type'] = type_of_story
		writer.writerow(news_dict.values())

		driver.execute_script("window.history.go(-1)")



		





