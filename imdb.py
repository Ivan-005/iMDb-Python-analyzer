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

        """Returns dictoinary with film id as jey and Filmd name and year as values"""
        search = {}
        data = requests.get(self.url.format('SearchMovie',self.api_key) + name).json()
        # Loops through the dictionary
        for item in data['results']:
            search.setdefault(item['id'], [item['title'], item['description']])

        return search


    def top_movies(self):

        """Returns dictionary with top 250 movies all time as key value pairs"""
        top_movies = {}
        data = requests.get(self.url.format('Top250Movies',self.api_key)).json()
        # Loops through the dictionary
        for item in data['items']:
            top_movies.setdefault(item['rank'], item['title'])

        return top_movies

    def popular_movies(self):

        """Returns a dictionary with 100 most popular movies"""
        popular_movies = {}
        data = requests.get(self.url.format('MostPopularMovies', self.api_key)).json()
        # Loops through the data
        for item in data['items']:
            popular_movies.setdefault(item['rank'], [item['title'], item['year']])

        return popular_movies



    def in_theaters(self):

        """Gets all in theaters movies"""
        in_theaters = {}
        data = requests.get(self.url.format('InTheaters', self.api_key)).json()
        # Loops through the data
        for item in data['items']:
            in_theaters.setdefault(item['id'], [item['title'], item['releaseState'], item['runtimeStr'], item['plot']])

        return in_theaters

    def soon_movies(self):

        """Returns dictionary with movie id as key and title, release date and plot as values"""
        soon_movies = {}
        data = requests.get(self.url.format('ComingSoon', self.api_key)).json()
        #Loops through the data
        for item in data['items']:
            soon_movies.setdefault(item['id'],[item['title'],item['releaseState'],item['plot']])

        return soon_movies



    def box_office_now(self):

        """Returns dictionary with rank as key and title,earnings as values"""
        box_office = {}
        data = requests.get(self.url.format('BoxOffice', self.api_key)).json()
        #Loops through the data
        for item in data['items']:
            box_office.setdefault(item['rank'],[item['title'],item['weekend']])

        return box_office

    def box_office_alltime(self):

        """Returns dictionary with rank as key and title,earnings as values"""
        box_office_all = {}
        data = requests.get(self.url.format('BoxOfficeAllTime', self.api_key)).json()
        #Loops through the data
        for item in data['items']:
            box_office_all.setdefault(item['rank'],[item['title'],item['worldwideLifetimeGross']])

        return box_office_all



class TvShow(Imdb):

    def find_tvshow(self,tvshow):

        """Returns dictionary about tvshow"""
        tv_search = {}
        data = requests.get(self.url.format('SearchSeries',self.api_key) + tvshow).json()
        #Loops through the data
        for item in data['results']:
            tv_search.setdefault(item['id'], [item['title'], item['description']])

        return tv_search

    def top_tvshow(self):

        """Returns a dictionary with top 250 Tv-Shows"""
        top_tvshow = {}
        data = requests.get(self.url.format('Top250TVs', self.api_key)).json()
        #Loops through the data
        for item in data['items']:
            top_tvshow.setdefault(data['id'], [data['title'], data['year'], data['rank'], data['imDbRating']])

        return top_tvshow

    def popular_tvshows(self):

        """Returns dictionary with most popular Tv-Shows"""
        popular_shows = {}
        data = requests.get(self.url.format('MostPopularTVs', self.api_key)).json()
        #Loops through the data
        for item in data['items']:
            popular_shows.setdefault(item['id'], [item['title'], item['rank'], item['year'], item['imDbRating']]) # da popunam ovde

        return popular_shows



a = TvShow()
print(a.popular_tvshows())
