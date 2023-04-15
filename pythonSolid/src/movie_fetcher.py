from movie_scraper import scrape_movies, save_movies_to_csv

# Este método respeta el principio de Single Responsibility, ya que su única responsabilidad es llamar a los métodos necesarios para descargar los datos de las películas, guardarlos en un archivo CSV y finalizar la ejecución.


def main():
    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    movies = scrape_movies(url)
    save_movies_to_csv(movies, "movie_results.csv")


if __name__ == '__main__':
    main()
