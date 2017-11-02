import tmdbsimple as tmdb
import config

tmdb.API_KEY = config.API_KEY

# Build the dictionary of genres so it is easier to get the ID later
genre = tmdb.Genres()
response = genre.list()
genreIdMap = {}
genreStringMap = {}
for item in response["genres"]: 
    genreIdMap[item["id"]] = item["name"]
    genreStringMap[item["name"]] = item["id"]

class Movie:
    title = None
    id = None
    voteAverage = None
    genres = []
    overview = None
    posterURL = "image.tmdb.org/t/p/w300"

    def __init__(self, title, id, voteAverage, genres, overview, posterURL):
        self.title = title
        self.id = id
        self.voteAverage = voteAverage
        self.overview = overview
        self.posterURL += posterURL

# @description
#  Gets the genre ID associated with a string
# @param
#  genreString: the name of a genre 
# @return
#   An int id associated with that genre in tmdb
# @error
#   KeyError if the string is not in the map
def getGenreId(genreString):
    return genreStringMap[genreString]

# @description
#   Gets the genre string associated with an ID
# @param
#   genreId: the id of a genre
# @return
#   A string that describes the genre
# @error
#   KeyError if the id is not in the mao
def getGenreString(genreId):
    return genreIdMap[genreId]

# @description
#   Gets a list of popular movies as defined by tmdb
# @param 
#   pageNum (optional): the page of results to display, defaults to 1
# @return
#   A list of 20 or less movie objects in descending popularity
#   By default it will return the top 20 from page 1
# @error
#   HttpError if the pageNum exceeds the actual number of results 
def getPopularMovies(pageNum=1):
    tmdbmovie = tmdb.Movies()
    response = tmdbmovie.popular(page=pageNum)
    popularMovieList = []

    for item in response["results"]:
        popularMovieList.append(Movie(item["title"], item["id"], item["vote_average"], item["genre_ids"], item["overview"], str(item["poster_path"])))

    return popularMovieList

# @description
#   Gets a list of popular movies that contains the specified genres
# @param
#   genreList (required): a list of genre strings or IDs that has to be included in the search
#   pageNum (optional): the page of results to display, defaults to 1
# @return
#   A list of 20 or less movie objects in descending popularity with the given genres
# @error
#   KeyError if the genre dotmdbdiscoveres not exist or the argument is not an array
#   HttpError if the pageNum exceeds the actual number of results
def getPopularMoviesByGenre(genreList=[], pageNum=1):
    tmdbdiscover = tmdb.Discover()
    genreQuery = ""

    for genre in genreList:
        # If the genre is a string, find the associated ID
        if (isinstance(genre, str)):
            genreId = getGenreId(genre)
            genreQuery += str(genreId) + ","
        else:
            genreQuery += str(genre) + ","

    if (genreQuery != ""):
        genreQuery = genreQuery[:-1]

    response = tmdbdiscover.movie(with_genres=genreQuery, page=pageNum)
    popularMovieListWithGenre = []

    for item in response["results"]:
        popularMovieListWithGenre.append(Movie(item["title"], item["id"], item["vote_average"], item["genre_ids"], item["overview"], str(item["poster_path"])))
    
    return popularMovieListWithGenre

# @description
#   Gets a list of movie objects given some query
# @param
#   movie (required): a string query to search
# @return
#   A list of movies that matches that given search terms
# @error
#   None
def searchForMovie(movie):
    tmdbsearch = tmdb.Search()
    response = tmdbsearch.movie(query=movie)
    movieList =[]

    # Grab all the IDs that match our search term
    for item in response["results"]:
        movieList.append(Movie(item["title"], item["id"],item["vote_average"], item["genre_ids"], item["overview"], str(item["poster_path"])))

    return movieList

# @description
#   Gets a list of similar movies given some id
# @param
#   movieId (required): The id associated with a movie
# @return
#   A list of movies tmdb recognizes as similar to the movie passed
# @error
#   HttpError if the movieId does not exist
def getSimilarMoviesById(movieId):
    tmdbsim = tmdb.Movies(movieId)
    response = tmdbsim.similar_movies()
    similarMovieList = []

    for item in response["results"]:
        similarMovieList.append(Movie(item["title"], item["id"],item["vote_average"], item["genre_ids"], item["overview"], str(item["poster_path"])))

    return similarMovieList