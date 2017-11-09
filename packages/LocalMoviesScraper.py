from bs4 import BeautifulSoup
import requests

class MovieListing:
    name = ""
    duration = ""
    times = []

    def __init__(self, name, rating, duration, times):
        self.name = name
        self.rating = rating
        self.duration = duration    # Contains more than movie length at the moment
        self.times = times          # Show times

    def DisplayData(self):
        print("Movie name:", self.name)
        print("Movie rating:", self.rating)
        print("Movie duration:", self.duration)
        for time in self.times:
            print("Time:", time)

class Theater:
    name = ""
    address = ""
    movies = []

    def __init__(self, name, address, movies):
        self.name = name
        self.address = address
        self.movies = movies

    def DisplayData(self):
        print("Theater name:", self.name)
        print("Theater address:", self.address)

        for movie in self.movies:
            movie.DisplayData()

# Find movies in the area - return an array of Theaters
def GetMovies():
    r = requests.get("https://www.moviefone.com/showtimes/gainesville-fl/32601/theaters/")
    soup = BeautifulSoup(r.text, "html.parser")

    results = soup.find("body", {"class": "showtimes-closest-page"})
    results = results.find("div", {"id": "mf-theater-showtimes-list"})

    results = results.findAll("div", {"class": "theater"})

    theaters = []

    for theater in results:
        theater_name = theater.find("a", {"class": "theater-name"}).text
        address = theater.find("p", {"class": "address"}).find("a").text

        movies = theater.findAll("div", {"class": "movie-data-wrap"})

        # print(theater_name)
        # print(address)

        movie_list = []

        for movie in movies:
            title = movie.find("div", {"class": "movietitle"}).text

            duration = movie.find("div", {"class": "movierating-runtime"}).text
            duration = duration.strip()
            duration = duration[:20]
            duration = duration.strip()
            info = duration.split("|")
            try:
                rating = info[0]
                rating = rating.strip()
            except:
                rating = "Unavailable"

            try:
                duration = info[1]
                duration = duration.strip()
            except:
                duration = "Unknown"

            showtimes = movie.find("div", {"class": "showtimes-list"}).findAll("span", {"class": "showtime-display"})
            times = []
            for time in showtimes:
                times.append(time.text)

            MovieObj = MovieListing(title,rating,duration,times)
            movie_list.append(MovieObj)

            '''
            print(title)
            print(duration)
            for child in showtimes:
                print(child.text)
            print("---------")
            '''

        TheaterObj = Theater(theater_name, address, movie_list)
        theaters.append(TheaterObj)

    '''
    for theater in theaters:
        print(theater.name)
    '''

    return theaters


def searchLocalMovies():
    theaters = GetMovies()
    '''
    for theater in theaters:
        theater.DisplayData()
        print("-------")
    '''
    return theaters

theaters = searchLocalMovies()
for theater in theaters:
    theater.DisplayData()