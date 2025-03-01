# creating API key/ jaclyn

import requests
import json

api_key = "3da5c4d" #api key from website
# title = input("?") #movie title parameter required 
# # should we ask for input now or later?

# url = "http://www.omdbapi.com/?apikey=" + api_key + "&t=" + title 
# print(url)
# request = requests.get(url)
# print(request.text)

# rqst_dict = json.loads(request.text)
# print(rqst_dict.keys)

# Define the page number you want to fetch
page_number = 1  # You can change this to fetch subsequent pages

# Create the URL for the OMDb API
url = f"http://www.omdbapi.com/?s=*&apikey={api_key}&page={page_number}"

# Print the URL to check if it's correctly formatted
print(url)

import requests

# Define the search term and API key
search_term = "Action"  # You can replace with any genre, actor, or keyword
page_number = 1

# Construct the URL
url = f"http://www.omdbapi.com/?s={search_term}&apikey={api_key}&page={page_number}"

# Make the request
response = requests.get(url)

# Get the data
data = response.json()

# Check if the response is valid
if data.get('Response') == 'True':
    print(data)  # Print the data if valid
else:
    print(f"Error: {data.get('Error')}")
