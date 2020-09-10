import requests
import json
import time


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

    def find_movie(self):

        """Returns dictoinary with film id as key and movie name and year as values"""
        name = input("Enter the movie name: ")
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

    def find_tvshow(self):

        """Returns dictionary about tvshow"""
        tvshow = input("Enter the Tv-Show name: ")
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
            popular_shows.setdefault(item['id'], [item['title'], item['rank'], item['year'], item['imDbRating']])

        return popular_shows


class Engine():
    """Engine fot the script"""

    def __init__(self):
        """Constructs and initializes all necessary objects"""
        self.imdb = Imdb()
        self.movie = Movie()
        self.tvshow = TvShow()
        self.func = {
        '1': self.movie.find_movie,
        '2': self.movie.top_movies,
        '3': self.movie.popular_movies,
        '4': self.movie.in_theaters,
        '5': self.movie.soon_movies,
        '6': self.movie.box_office_now,
        '7': self.movie.box_office_alltime,
        '8': self.tvshow.find_tvshow,
        '9': self.tvshow.top_tvshow,
        '10': self.tvshow.popular_tvshows
        }

    

    def menu(self):
        print("""
        ---ALL FUNCTIONS RETURN DICTIONARY FORMAT---

        0. Quit the program

        Analyzing movies functions:

            1. find_movie (Finds movie and returns id, title and description)
            2. top_movies (Returns top 250 movies)
            3. popular_movies (Returns most 100 popular movies)
            4. in_theaters (Returns all in theaters movies)
            5. soon_movies (Returns all upcoming movies)
            6. box_office_now (Returns Box office now)
            7. box_office_alltime (Returns Box office for all time)

        Analyzing Tv-Shows functions:

            8. find_tvshow (Finds Tv-Show and returns id, title and description)
            9. top_tvshow (Returns top 250 Tv-Show)
            10. popular_tvshows (Returns most 100 popular Tv-Show)

        Press Control + C (Ctrl + C) to exit the program
        """)



    def run(self):
        """Function for running the whole script"""

        while True:
            #Mainloop for the program
            self.menu()
            decision = input("Please enter the number of your choice: ")
            action = self.func.get(decision)
            if action:
                print(action())
            else:
                print("Invalid choice.")



if __name__ == '__main__':
    Engine().run()
