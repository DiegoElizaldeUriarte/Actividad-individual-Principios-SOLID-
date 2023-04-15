class Movie:
    # Este método respeta el principio de Single Responsibility, ya que su única responsabilidad es asignar los valores de los parámetros a las propiedades correspondientes del objeto Movie.
    def __init__(self, movie_title, year, place, star_cast, rating, vote, link, preference_key):
        self.movie_title = movie_title
        self.year = year
        self.place = place
        self.star_cast = star_cast
        self.rating = rating
        self.vote = vote
        self.link = link
        self.preference_key = preference_key

    # Este método respeta el principio de Open/Closed, ya que la clase Movie está abierta a la extensión pero cerrada a la modificación.
    def to_dict(self):
        return {"movie_title": self.movie_title,
                "year": self.year,
                "place": self.place,
                "star_cast": self.star_cast,
                "rating": self.rating,
                "vote": self.vote,
                "link": self.link,
                "preference_key": self.preference_key}
