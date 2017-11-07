#!/usr/bin/python3

from packages import GuideScraper
from packages import LocalMoviesScraper
from packages import tmdbutils
from packages import nlu
from tkinter import *
import speech_recognition as sr
import re

def speechApp():
    try:
        print("Say something!")
        T.insert(INSERT, "Say something!\n")

        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        T.insert(INSERT, "Got it! Now to recognize it...\n")

        try:
            # recognize speech using Google Speech Recognition
            userInput = r.recognize_google(audio)

            # Get the intent from a model
            intent = nlu.determineIntent(userInput)

            # This shows the top 20 popular movies
            if (intent == "recommend_movie"):
                popularMovies = tmdbutils.getPopularMovies()
                
            # Command: Search show [show name]
            elif (intent == "show_tv"):
                GuideScraper.searchTVGuide(userInput)

            # Command: Search local movies
            elif (intent == "show_local"):
                LocalMoviesScraper.searchLocalMovies()

            
            print("You said {}".format(userInput))
            T.insert(INSERT, "You said {}\n".format(userInput))

            input("Waiting...")
        
        except sr.UnknownError:
            print("Oops! Didn't catch that")
            T.insert(INSERT, "Oops! Didn't catch that\n")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            T.insert(INSERT, "Uh oh! Couldn't request results from Google Speech Recognition service; {0}\n".format(e))
        T.pack()
        root.after(200, speechApp)
    except KeyboardInterrupt:
        pass

r = sr.Recognizer() 
m = sr.Microphone()
root = Tk()
T = Text(root, height=50, width=150)
print("A moment of silence, please...")
T.insert(INSERT, "A moment of silence, please...\n")
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
T.insert(INSERT, "Set minimum energy threshold to {}\n".format(r.energy_threshold))

speechApp()
root.mainloop()