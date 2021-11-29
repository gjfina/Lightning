# Just a quick script to knock the rust off of web scraping

# Import libraries
import requests
from bs4 import BeautifulSoup
import sqlite3 
from datetime import date
import re
import json
import sqlite3
import sys,os

# Import config details
## => This section ultimately needs to be moved to a configuration file, but I got
## ==> of troubleshooting and moved on to developing the feature to output to SQL Lite. 
## ==> Eventually I need to find a way for this code to leverage the variables from the
## ==> config file for scalability / portability. 


cfile = 'config.json' 
with open(cfile, 'r') as config_file:
	data = json.load(config_file)
file_URL = json.dumps(data["location"])
db_file = json.dumps(data["db_file"])
code_test = json.dumps(data["location"])
print("Successfully imported read_config.py")



### dev notes -> '/data/' and 'weather_data.db' should be values read from the config file
parent_path = os.path.realpath('..')
full_path = str(parent_path + '/data/' + 'weather_data.db')
print("DB Location: ", full_path)

# Establish where I'm picking data up from
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.1554&lon=-83.0878#.YZ7lB9nMLBE')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Start parsing out the data to test output 

find_seven_day = soup.find(id="seven-day-forecast")

trim_down_sevens = find_seven_day.find_all(class_="tombstone-container")

tonight = trim_down_sevens[0]

present_tonight = tonight.prettify()

# Test parsing - Create extract names

# => This section is all about pulling the data from within the individual classes,
# ==> but it pulls from the variable "tonight" in the previous section only
time_period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()



# => This section finds the image tag and grabs the long description from this field
pull_img = tonight.find("img")
long_desc = pull_img['title']

# Create tags for the various time periods
time_per_tags = find_seven_day.select(".tombstone-container .period-name")
full_time_per = [pt.get_text() for pt in time_per_tags]
full_time_per


# Parse a new section of the site based on inspecting, not a tutorial
# => The above sections were mostly pulled verbatim (except for variables) from a tutorial
# ==> This section is my attempt to use the same logic but point to a different container
# ===> which actually contains Barometric pressure (my ultimate goal!)

find_cur_conditions = soup.find(id="seven-day-forecast")
trim_down_conditions = find_cur_conditions.find_all('td')
#humidity = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[1]))
#wind_speed = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[3]))
#barometer = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[5]))
#dewpoint = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[7]))
#visibility = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[9]))
#wind_chill = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[11]))
#last_updated = re.sub(r'[<td>|</td>]',"",str(trim_down_conditions[13]))

# Test the code! change code_test to whatever variable you want to see
code_test = find_cur_conditions
print(code_test)