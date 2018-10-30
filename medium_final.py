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
#add all title column created above to the first row of the csv file
writer.writerow(news_dict.values())


SCROLL_PAUSE_TIME = 4

#driver = webdriver.Chrome()

topics = ['https://medium.com/topic/art',
 'https://medium.com/topic/books',
 'https://medium.com/topic/comics',
 'https://medium.com/topic/culture',
 'https://medium.com/topic/film',
 'https://medium.com/topic/food',
 'https://medium.com/topic/gaming',
 'https://medium.com/topic/humor',
 'https://medium.com/topic/internet-culture',
 'https://medium.com/topic/fiction',
 'https://medium.com/topic/medium-magazine',
 'https://medium.com/topic/music',
 'https://medium.com/topic/photography',
 'https://medium.com/topic/poetry',
 'https://medium.com/topic/social-media',
 'https://medium.com/topic/sports',
 'https://medium.com/topic/style',
 'https://medium.com/topic/true-crime',
 'https://medium.com/topic/tv',
 'https://medium.com/topic/writing',
 'https://medium.com/topic/business',
 'https://medium.com/topic/design',
 'https://medium.com/topic/economy',
 'https://medium.com/topic/startups',
 'https://medium.com/topic/freelancing',
 'https://medium.com/topic/leadership',
 'https://medium.com/topic/marketing',
 'https://medium.com/topic/productivity',
 'https://medium.com/topic/work',
 'https://medium.com/topic/artificial-intelligence',
 'https://medium.com/topic/blockchain',
 'https://medium.com/topic/cryptocurrency',
 'https://medium.com/topic/cybersecurity',
 'https://medium.com/topic/data-science',
 'https://medium.com/topic/gadgets',
 'https://medium.com/topic/javascript',
 'https://medium.com/topic/machine-learning',
 'https://medium.com/topic/math',
 'https://medium.com/topic/neuroscience',
 'https://medium.com/topic/programming',
 'https://medium.com/topic/science',
 'https://medium.com/topic/self-driving-cars',
 'https://medium.com/topic/software-engineering',
 'https://medium.com/topic/space',
 'https://medium.com/topic/technology',
 'https://medium.com/topic/visual-design',
 'https://medium.com/topic/addiction',
 'https://medium.com/topic/creativity',
 'https://medium.com/topic/disability',
 'https://medium.com/topic/family',
 'https://medium.com/topic/health',
 'https://medium.com/topic/mental-health',
 'https://medium.com/topic/parenting',
 'https://medium.com/topic/personal-finance',
 'https://medium.com/topic/pets',
 'https://medium.com/topic/psychedelics',
 'https://medium.com/topic/psychology',
 'https://medium.com/topic/relationships',
 'https://medium.com/topic/self',
 'https://medium.com/topic/sexuality',
 'https://medium.com/topic/spirituality',
 'https://medium.com/topic/travel',
 'https://medium.com/topic/wellness',
 'https://medium.com/topic/basic-income',
 'https://medium.com/topic/cities',
 'https://medium.com/topic/education',
 'https://medium.com/topic/environment',
 'https://medium.com/topic/equality',
 'https://medium.com/topic/future',
 'https://medium.com/topic/gun-control',
 'https://medium.com/topic/history',
 'https://medium.com/topic/justice',
 'https://medium.com/topic/language',
 'https://medium.com/topic/lgbtqia',
 'https://medium.com/topic/media',
 'https://medium.com/topic/masculinity',
 'https://medium.com/topic/philosophy',
 'https://medium.com/topic/politics',
 'https://medium.com/topic/race',
 'https://medium.com/topic/religion',
 'https://medium.com/topic/san-francisco',
 'https://medium.com/topic/transportation',
 'https://medium.com/topic/women',
 'https://medium.com/topic/world']
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
	links = driver.find_elements_by_xpath('//div[@class="ea ee"]/h3/a')
	links = [link.get_attribute('href') for link in links]
	print(len(links))
	print(links)
	#for item in blocks:
	for link in links:
		driver.get(link)
		news_dict = {}

		try: 
			author_name = driver.find_element_by_xpath('//div[@class="u-lineHeightTightest"]//a[@dir="auto"]').text
		except: 
			try: 
				author_name = driver.find_element_by_xpath('//div[@class="u-flexEnd u-marginBottom4"]/a[@ds-link ds-link--styleSubtle postMetaInline postMetaInline--author]').text 
			except:
				author_name = "na"

		try: 
			date = driver.find_element_by_xpath('//div[@class="ui-caption postMetaInline js-testPostMetaInlineSupplemental"]/time').get_attribute('datetime')
		except:
			try: 
				date = driver.find_element_by_xpath('//span[@class="u-noWrap"]/time').text
			except:
				date = "na"
		try:
			title = driver.find_element_by_tag_name('h1').text
		except:
			try: 
				title = driver.find_element_by_tag_name('h3').text
			except:
				try: 
					title = driver.find_element_by_xpath('//html/head/title').text
				except:
					title = "na"
		print(title)
		#('//div[@class="section-inner sectionLayout--insetColumn"]/h1[@class="graf graf--h3 graf--leading graf--title"]').text
		#except: 
			#title = driver.find_element_by_xpath('//div[@class="section-inner sectionLayout--insetColumn"]/h1[@class="graf graf--h3 graf-after--figure graf--trailing graf--title"]').text
		try: 
			likes = driver.find_element_by_xpath('//span[@class="u-textAlignCenter u-relative u-background js-actionMultirecommendCount u-marginLeft10"]/button').text
		except:
			likes = "na"
		try: 
			comments = driver.find_element_by_xpath('//button[@data-action="show-recommends"]').text
		except: 
			comments = "na"
		try: 
			categories_list = driver.find_element_by_xpath('//div[@class="u-paddingBottom10"]/ul[@class="tags tags--postTags tags--borderless"]/li/a').text
		except:
			categories_list = "na"
		
		news_dict['title'] = title
		news_dict['author_name'] = author_name
		news_dict['date'] = date
		news_dict['likes'] = likes
		news_dict['comments'] = comments
		news_dict['categories_list'] = categories_list
		writer.writerow(news_dict.values())

		driver.execute_script("window.history.go(-1)")



		





