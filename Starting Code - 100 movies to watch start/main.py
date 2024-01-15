import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_page_data = response.text
soup = BeautifulSoup(web_page_data, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]

# slicing from the back
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:

    for movie in movies:
        file.write(f"{movie}\n")
