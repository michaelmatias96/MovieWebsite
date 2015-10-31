import media

__author__ = 'michaelmatias'


class TvShow(media.Video):
    def __init__(self, title, duration, season, episode, tv_station):
        media.Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        pass