#Jaclyn
# pull in api from OMDb - load in api key?
    # creating API key/ jaclyn

import requests
import json
import csv

    api_key = "3da5c4d" #api key from website
    # title = input("?") #movie title parameter required 
    # should we ask for input now or later? 

    # Define the page number you want to fetch
    page_number = 1  # You can change this to fetch subsequent pages

    # Create the URL for the OMDb API
    url = f"http://www.omdbapi.com/?s=*&apikey={api_key}&page={page_number}"

    # Print the URL to check if it's correctly formatted
    print(url)

# figure out how to get all movies into csv!

    # Fetch data from the OMDb API
    request = requests.get(url)

    rqst_dictionary = json.loads(request.text)

    json.dump(rqst_dictionary, open("results.json", "w"))

    key1 = "Title" # dictionary 
    # key2 = "Year"

    for key in rqst_dictionary[key1]:
        print(key)

# example from Professor Harding's video
# csv_file = open(api_key + ".csv", "w") 
# csv_file.write("Title,api_key\n")
# write_lines = []
# for title in req_dict[key1]:
#     print(date + "," + req_dict[key1][date][key2]) #print key, value
#     # csv_file.write(date + "," + req_dict[key1][date][key2]+"\n") #print key, value
#     write_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
    
# write_lines = write_lines[::-1]
# csv_file.writelines(write_lines)
# csv_file.close()

#Xyla
def fetch_movie_data(page=1):
    params = {"apikey": api_key, "s": "movie", "r": "json", "page": page}
    response = requests.get(url, params=params)
    return response.json()
print("movie data:", fetch_movie_data())


def get_all_movie_data():
    movie_data = []
    page = 1
    while True:
        data = fetch_movie_data(page)
        if "Search" not in data:
            break  # Stop if no more results are returned
        movie_data.extend(data["Search"])
        page += 1
    return movie_data

# Fetch movie data and store in CSV
all_movies = get_all_movie_data()
movie_data = []

for movie in all_movies:
    params = {"apikey": api_key, "i": movie["imdbID"], "r": "json"}
    response = requests.get(url, params=params)
    data = response.json()

    # Extract relevant fields
    movie_info = {
        "Title": data.get("Title"),
        "Year": data.get("Year"),
        "Rated": data.get("Rated"),
        "Genre": data.get("Genre"),
        "imdbRating": data.get("imdbRating"),
        "Plot": data.get("Plot"),
    }
    movie_data.append(movie_info)


Write to CSV
with open("movies.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Year", "Rated", "Genre", "imdbRating", "Plot"])
    writer.writeheader()
    writer.writerows(movie_data)
print("Data stored in movies.csv")

""" All other steps
explore data, determine dictionaries

add to csv file

analyze data- ask for inputs

store results in .json file"""

# trying again
import requests
import json
import csv

api_key = "3da5c4d"  # API key
search_term = "movie"  # Generic search term to get multiple movies
url = "http://www.omdbapi.com/"
page_number = 1  # Start with page 1
all_movies = []  # List to store all movie data

# Fetch multiple pages until there are no more results
while True:
    params = {"s": search_term, "apikey": api_key, "page": page_number}
    response = requests.get(url, params=params)
    data = response.json()

    if "Search" in data:  # Check if movies are found
        all_movies.extend(data["Search"])  # Add movies to the list
        print(f"Fetched page {page_number}, total movies so far: {len(all_movies)}")
        page_number += 1  # Move to the next page
    else:
        print("No more results found or reached the API limit.")
        break  # Stop the loop when no more movies are found

# Save movies to a CSV file
csv_filename = "movies.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Year", "Type", "IMDb ID"])  # CSV Header
    for movie in all_movies:
        writer.writerow([movie["Title"], movie["Year"], movie["Type"], movie["imdbID"]])

print(f"Saved {len(all_movies)} movies to '{csv_filename}' successfully!")

# this only saved 6387 movies and then reached API limit, not sure what movies it saved (there should be over 600,000)
