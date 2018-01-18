# TO RUN THIS APP 

# first obtain API key from openweather website 

# in terminal type

# python weather-app.py <city-name> <query>

# <query> can be one of these [temp, temp_min, temp_max, humidity]
 


import urllib			#imports urllib module
import json 			#imports json module
from sys import argv 	#imports argv from sys


#uncomment the below line to see argv output
#print argv


API_key = "INSERT_YOUR_API_KEY"			#openweather api key

location = argv[1]		#fetches <city-name> from terminal


url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+API_key	#generates request API Url


req = urllib.urlopen(url) 	#sends request to the set url

data = req.read() 			#reads the data in the req body


# #uncomment the below line to see data output and data type of received data
# #print data
# #print type(data)


parsedData = json.loads(data)


# #uncomment the below line to see data output and data type of parsed JSON data
# #print data
# #print type(parsedData)

obtained = parsedData['main'][argv[2]]

print ('current {} condition of {} area is {}'.format(argv[2], argv[1], obtained))
