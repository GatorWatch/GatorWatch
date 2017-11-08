#!/usr/bin/python3

from packages import GuideScraper
from packages import LocalMoviesScraper
from packages import tmdbutils
from packages import nlu
from tkinter import *
import speech_recognition as sr
import re

def speechApp(*args):
    try:
        '''
        print("Say something!")
        T.insert(INSERT, "Say something!\n")
        '''

        with m as source: audio = r.listen(source)

        '''
        print("Got it! Now to recognize it...")
        T.insert(INSERT, "Got it! Now to recognize it...\n")
        '''

        try:
            # recognize speech using Google Speech Recognition
            userInput = r.recognize_google(audio)

            print("You said {}".format(userInput))
            T.insert(INSERT, "You said {}\n".format(userInput))

            # Get the intent from a model
            interpretation = nlu.getInterpretation(userInput)
            intent = interpretation["intent"]["name"]

            # Display list of popular moies
            if (intent == "recommend_movie"):
                # Attempt to extract genres from the user input
                # If we find genres, do a search with that list
                # Otherwise return the default popular list
                entities = nlu.getEntities(interpretation)
                userGenres = []

                # Build the list of genres to include in our search
                for item in entities:
                    if (item["entitiy"] == "genre"):
                        userGenres.append(item["value"])

                # If no genres specified, do default search
                if not userGenres:
                    popularMovies = tmdbutils.getPopularMovies()
                    # Do stuff with popularMovies 
                else:
                    popularMoviesWithGenres = tmdbutils.getPopularMoviesWithGenre(userGenres)
                    # Do stuff with popularMoviesWithGenres


            # Attempt to extract the movie or show name using rasa
            # This is kind of hard right now without any training data
            # elif (intent == "lookup_details"):
            #     entities = nlu.getEntities(interpretation)
            #     movieToLookup = entities[0]["value"]

            # Command: Search show [show name]
            elif (intent == "show_tv"):
                listings = GuideScraper.searchTVGuide(userInput)
                for listing in listings:
                    T.insert(INSERT, "Name: " + listing.name + "\n")
                    T.insert(INSERT, "Episode Name: " + listing.episode_name + "\n")
                    T.insert(INSERT, "Episode: " + listing.episode + "\n")
                    T.insert(INSERT, "Description: " + listing.description + "\n")
                    T.insert(INSERT, "Channel: " + listing.channel + "\n")
                    T.insert(INSERT, "Time: " + listing.time + "\n")
                    T.insert(INSERT, "-----------------\n")

            # Command: Search local movies
            elif (intent == "show_local"):
                theaters = LocalMoviesScraper.searchLocalMovies()
                for theater in theaters:
                    T.insert(INSERT, "Theater: " + theater.name + "\n")
                    T.insert(INSERT, "Address: " + theater.address + "\n")
                    for movie in theater.movies:
                        T.insert(INSERT, "Movie Name: " + movie.name + "\n")
                        T.insert(INSERT, "Duration: " + movie.duration + "\n")
                        for time in movie.times:
                            T.insert(INSERT, "Time: " + time + "\n")
                        T.insert(INSERT, "---------------\n")

            input("Waiting...")
        
        except sr.UnknownError:
            print("Oops! Didn't catch that")
            T.insert(INSERT, "GatorWatch: I'm sorry, I don't understand. Can you repeat that?\n")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            T.insert(INSERT, "GatorWatch: Couldn't request results from Google Speech Recognition service. {0}\n".format(e))
        T.pack()
        root.after(200, speechApp)
    except KeyboardInterrupt:
        pass

r = sr.Recognizer() 
m = sr.Microphone()
root = Tk()
T = Text(root, height=50, width=150)
T.pack()

print("A moment of silence, please...")
# T.insert(INSERT, "A moment of silence, please...\n")
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
# T.insert(INSERT, "Set minimum energy threshold to {}\n".format(r.energy_threshold))

button = Button(T, text="Speak", command=speechApp)
T.window_create(INSERT, window=button)
#speechApp()
root.mainloop()