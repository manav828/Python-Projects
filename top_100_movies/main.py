from bs4 import BeautifulSoup
import requests

responce = requests.get('https://www.imdb.com/list/ls068718974/')
web_pg = responce.text

soup = BeautifulSoup(web_pg,'html.parser')
movies = soup.find_all()
i=0

with open('top_100_movies','w') as file:
    for movie in movies:
        i +=1
        movie_name = movie.find('a').text
        file.write(f"{i}) {movie_name}\n")