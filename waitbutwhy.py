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


waitbutwhy = open('waitbutwhy.csv', 'w', encoding='utf-8')
writer = csv.writer(waitbutwhy)
news_dict = {}
#create column for dictionary
news_dict['title'] = 'title'
news_dict['author_name'] = 'author_name'
news_dict['date'] = 'date'
news_dict['likes'] = 'likes'
news_dict['comments'] = 'comments'
news_dict['categories_list'] = 'categories_list'
news_dict['type_of_story'] = type_of_story
#add all title column created above to the first row of the csv file
writer.writerow(news_dict.values())


SCROLL_PAUSE_TIME = 4

#driver = webdriver.Chrome()

topics = ['https://waitbutwhy.com/archive',
'https://waitbutwhy.com/archive/page/2']
driver = webdriver.Chrome('/Users/Sausa08/Downloads/chromedriver')


for url in topics:

	driver.get(url)

	last_height = driver.execute_script("return document.body.scrollHeight")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(SCROLL_PAUSE_TIME)
	new_height = driver.execute_script("return document.body.scrollHeight")


	links = driver.find_elements_by_xpath('//div[@class="older-postlist"]/ul/li/a')
	links = [link.get_attribute('href') for link in links]
	print(len(links))
	print(links)
	#for item in blocks:
	for link in links:
		driver.get(link)
		news_dict = {}

		author_name = "Tim Urban"

		try: 
			date = driver.find_element_by_xpath('//span[@class="date"]/i').text
		except:
			date = "NA"
		
		try:
			title = driver.find_element_by_tag_name('h1').text
		except:
			try: 
				title = driver.find_element_by_xpath('//header[@class="entry-header"]/h1').text
			
			except:
					title = "na"
		print(title)
		
		try: 
			likes = driver.find_element_by_xpath('//div/span[@class="_5n6h _2pih"]').text
		except:
			likes = "na"
		try: 
			comments = driver.find_element_by_xpath('//li[@class="nav-tab nav-tab--primary tab-conversation active"]/a/span[@class="comment-count"]').text
		except: 
			comments = "na"
		try: 
			categories_list = driver.find_element_by_xpath('html/meta[@property="article:tag"]').text
		except:
			categories_list = "na"
		type_of_story = Blog
		
		news_dict['title'] = title
		news_dict['author_name'] = author_name
		news_dict['date'] = date
		news_dict['likes'] = likes
		news_dict['comments'] = comments
		news_dict['categories_list'] = categories_list
		news_dict['type_of_story'] = type_of_story
		writer.writerow(news_dict.values())

		driver.execute_script("window.history.go(-1)")



		





