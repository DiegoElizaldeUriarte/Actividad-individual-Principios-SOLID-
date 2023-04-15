import re
import requests
import csv
from bs4 import BeautifulSoup

from movie import Movie

# Este método respeta el principio de Single Responsibility, ya que su única responsabilidad es parsear los datos de una película a partir de una etiqueta HTML y un índice.


def parse_movie(movie, index, crew, ratings, votes, links):
    movie_string = movie.get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    return {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index],
            "preference_key": index % 4 + 1}

# Este método respeta el principio de Single Responsibility, ya que su única responsabilidad es obtener los datos de las películas a partir de la URL proporcionada.


def get_movies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
               for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value')
             for b in soup.select('td.ratingColumn strong')]
    return movies, links, crew, ratings, votes

# Este método respeta el principio de Single Responsibility, ya que su única responsabilidad es llamar a los métodos necesarios para obtener y parsear los datos de las películas a partir de la URL proporcionada, y retornar una lista de objetos Movie.


def scrape_movies(url):
    movies, links, crew, ratings, votes = get_movies(url)
    return [Movie(**parse_movie(movies[i], i, crew, ratings, votes, links)) for i in range(len(movies))]

# Este método respeta el principio de Single Responsibility, ya que su única responsabilidad es guardar los datos de las películas en un archivo CSV con el nombre especificado.


def save_movies_to_csv(movies, file_path):
    fields = ["preference_key", "movie_title", "star_cast",
              "rating", "year", "place", "vote", "link"]
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie.to_dict())
