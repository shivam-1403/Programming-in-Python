import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
html_text = response.text

soup = BeautifulSoup(html_text, "html.parser")
all_h2_tags = soup.find_all(name="h2")
movie_titles = [tag.find("strong").getText() for tag in all_h2_tags if tag.find("strong")]
movies = movie_titles[::-1]

with open(r"D:\Python Code\Programming-in-Python\044.Top_100_Movies\movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")