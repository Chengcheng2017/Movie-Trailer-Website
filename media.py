import webbrowser


class Movie:
    """This provides documentation about the class "Movie"
    that stores movie related information.

    Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
    """
    """ This class provides a way to store movie related information """
    # Initializing and creating space in memory
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
