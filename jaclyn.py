# creating API key/ jaclyn

import requests
import json

api_key = "3da5c4d" #api key from website
title = input("?") #movie title parameter required 
# should we ask for input now or later?

url = "http://www.omdbapi.com/?apikey=" + api_key + "&t=" + title 
print(url)
request = requests.get(url)
print(request.text)

# rqst_dict = json.loads(request.text)
# print(rqst_dict.keys)