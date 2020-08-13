import requests
import json


class Imdb():

    def __init__(self):
        self.url = url = "https://imdb-api.com/en/API/{}/{}/{}"
        with open('credentials.json') as file:
            self.api_key = json.load(file)['api_key']



class Movie(Imdb):

    def find_movie(self,name):
        json_data = requests.get(url.format('SearchMovie',self.api_key,name)).text
        return json_data

    def top_movies(self):
        pass

    def popular_movies(self):
        pass

    def in_theaters(self):
        pass

    def soon_movies(self):
        pass

    def box_office_now(self):
        pass

    def box_office_alltime(self):
        pass



class TvShow(Imdb):

    def find_tvshow(self,tvshow):
        pass

    def top_tvshow(self):
        pass

    def popular_tvshows(self):
        pass
