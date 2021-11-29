# Just a quick script to knock the rust off of web scraping

# Import libraries
import requests
from bs4 import BeautifulSoup
import sqlite3 

# Establish where I'm picking data up from
page = requests.get('https://w1.weather.gov/data/obhistory/KOSU.html')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Start parsing out the data
find_code = soup.prettify() #show the html

find_tags = list(soup.children) #create a list of all of the html elements

find_basic_entries = [type(item) for item in list(soup.children)] # create a list of the class types in this code


show_html = list(soup.children)[2]
show_html2 = list(show_html.children)[3]
show_html3 = list(show_html2.children)

show_code = soup.find('td').get_text()

body_search = soup.find(class_="th")

for tag in soup.find('table').find_all():
	tag.extract()
	print(tag)






# Print the results in a visible way so I can make sure everything is outputting appropriately
print (show_code)