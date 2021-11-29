# read_config.py
# The purpose of this script is to read the config file and all appropriate variables that will be used by the weather app. 
# This script will be called by any applications within the weather app framework to simplify
# how variables are called

## ==> Using double pound signs (##) to denote when I am disabling a section of code

# => Import Step
## import configparser
import json



# => LET'S TRY TO READ A .INI FILE


##config = configparser.ConfigParser()

##config_file = config.read('.\config\config.ini')

##code_test = str(config_file['location_variables']['location'])
##code_test = config.sections()



# => LET'S TRY TO READ A JSON FILE

def func1(): 
	with open(cfile, 'r') as config_file:
		data = json.load(config_file)
	file_URL = json.dumps(data["location"])
	db_file = json.dumps(data["db_file"])
	code_test = json.dumps(data["location"])
	print("Successfully imported read_config.py")
	
if __name__ == '__main__':
	func1()

#cfile = 'config.json'

#with open(cfile, 'r') as config_file:
#	data = json.load(config_file)
	
#obj = json.loads(data)

#file_URL = json.dumps(data["location"])
#db_file = json.dumps(data["db_file"])

#code_test = json.dumps(data["location"])

# => PRINT THE TEST RESULTS
#print("Current URL:", file_URL)
#print("Reading / Writing to DB: ",db_file)