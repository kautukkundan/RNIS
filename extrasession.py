import urllib
import json
#import pprint
from sys import argv

#print argv[1]

url = "http://samples.openweathermap.org/data/2.5/weather?q="+argv[1]+"&appid=b6907d289e10d714a6e88b30761fae22"

req = urllib.urlopen(url)

res = req.read()


parsed = json.loads(res)

#print type(parsed)
#pprint.pprint(parsed)

print parsed['main'][argv[2]]