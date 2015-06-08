#This python file contains the class Movie
#In the interest of keeping class definitions in their own files, the class is not included in entertainment_center.py
class Movie():
    def __init__(self, movie_title, movie_plot, poster_image, trailer_youtube, movie_cast, movie_rating, movie_year):
        self.title = movie_title
        self.plot = movie_plot
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.cast = movie_cast
        self.rating = movie_rating
        self.year = movie_year