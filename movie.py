import config
import webbrowser
import media

__author__ = 'michaelmatias'


class Movie(media.Video):
    """This class provides a way to store movie related information"""
    valid_ratings = config.VALID_RATINGS

    def __init__(self, title, duration, storyline,
                 trailer_youtube_url, poster_image_url):
        media.Video.__init__(self, title, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)