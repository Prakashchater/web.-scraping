from bs4 import BeautifulSoup
import requests

url = "https://stacker.com/stories/1587/100-best-movies-all-time"

response = requests.get(url)
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h2")
movie_list = [movie.getText() for movie in all_movies]
movies = movie_list[102:2:-1]
# print(movies)

# for i in range(len(movie_list)-2,2,-1):
#     print(movie_list[i])


with open("movies.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
