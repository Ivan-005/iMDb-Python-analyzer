import requests
import json


class Imdb():
    """Creating Imdb class for initializing url and api key"""

    def __init__(self):
        """Constructor for Imdb class"""
        # Initializing url and API key
        self.url = url = "https://imdb-api.com/en/API/{}/{}/"
        with open('credentials.json') as file:
            self.api_key = json.load(file)['api_key']



class Movie(Imdb):
    """Class for analyzing movies"""

    def find_movie(self,name):
        data = requests.get(self.url.format('SearchMovie',self.api_key) + name).json()
        return data

    def top_movies(self):

        """Returns dictionary with top 250 movies all time as key value pairs"""
        movies = {}
        data = requests.get(self.url.format('Top250Movies',self.api_key)).json()
        # Loops through the json data in dictionary format
        for item in data['items']:
            movies.setdefault(item['rank'], item['title'])
        return movies

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


a = Movie()
a.top_movies()
