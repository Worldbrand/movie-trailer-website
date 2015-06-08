class Movie():
    """Contains all relevant information for each movie object.
    
    Takes in several arguments and applies them as 
    self-contained variables when initialized.
    
    Args:
        movie_title (str): The name of the movie.
        movie_plot (str):  A summary of the movie's plot.
        poster_image (str): A URL to a poster image of the movie.
        trailer_youtube (str): A URL to the trailer of the movie on youtube.
        movie_cast (str): The lead actors and actresses' names.
        movie_rating (str): The movie's rating on IMDb.
        movie_year (str): The year of the movie's release.
    
    """
    def __init__(self, movie_title, movie_plot, poster_image, trailer_youtube,
                 movie_cast, movie_rating, movie_year):
        self.title = movie_title
        self.plot = movie_plot
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.cast = movie_cast
        self.rating = movie_rating
        self.year = movie_year