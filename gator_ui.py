# -*- coding: utf-8 -*-
#!/usr/bin/python3

from packages import GuideScraper
from packages import LocalMoviesScraper
from packages import tmdbutils
from packages import nlu
import speech_recognition as sr
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
import sys
from playsound import playsound
import time
from packages import GenerateAudio
import random
from packages import Logging
from packages import CalendarSystem
import datetime
import os

class ShowListing:
    name = ""
    episode_name = ""
    episode = ""
    description = ""
    channel = ""
    date = ""
    time = ""

    def __init__(self, name, episode_name, episode, description, channel, date, time):
        self.name = name
        self.episode_name = episode_name
        self.episode = episode
        self.description = description
        self.channel = channel
        self.date = date
        self.time = time



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
class Bubble(QtWidgets.QLabel):
    def __init__(self,text):
        super(Bubble,self).__init__(text)
        self.setContentsMargins(5,5,5,5)

    def paintEvent(self, e):

        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing,True)
        p.drawRoundedRect(0,0,self.width()-1,self.height()-1,5,5)

        super(Bubble,self).paintEvent(e)        

class MyWidget(QtWidgets.QWidget):

    def __init__(self,text,left=True):
        super(MyWidget,self).__init__()

        hbox = QtWidgets.QHBoxLayout()

        label = Bubble(text)

        if not left:
            hbox.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred))

        hbox.addWidget(label)

        if left:
            hbox.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred))            

        hbox.setContentsMargins(0,0,0,0)

        self.setLayout(hbox)
        self.setContentsMargins(0,0,0,0)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1233, 869)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(220, 199, 170);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.infoScrollLayout = QtWidgets.QVBoxLayout()
        self.infoScrollLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.infoScrollLayout.setObjectName("infoScrollLayout")
        self.infoScrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoScrollArea.sizePolicy().hasHeightForWidth())
        self.infoScrollArea.setSizePolicy(sizePolicy)
        self.infoScrollArea.setMinimumSize(QtCore.QSize(600, 845))
        self.infoScrollArea.setAutoFillBackground(True)
        self.infoScrollArea.setStyleSheet("background-color: rgb(107, 122, 143);")
        self.infoScrollArea.setWidgetResizable(True)
        self.infoScrollArea.setObjectName("infoScrollArea")
        self.infoScrollContents = QtWidgets.QWidget()
        self.infoScrollContents.setGeometry(QtCore.QRect(0, 0, 598, 843))
        self.infoScrollContents.setObjectName("infoScrollContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.infoScrollContents)    
        self.verticalLayout_3.setObjectName("verticalLayout_3")            
        self.infoLayout = QtWidgets.QVBoxLayout()            
        self.infoLayout.setObjectName("infoLayout")            
        self.verticalLayout_3.addLayout(self.infoLayout)
        self.infoScrollArea.setWidget(self.infoScrollContents)
        self.infoScrollLayout.addWidget(self.infoScrollArea)
        self.gridLayout.addLayout(self.infoScrollLayout, 0, 1, 1, 1)
        self.msgScrollLayout = QtWidgets.QVBoxLayout()
        self.msgScrollLayout.setObjectName("msgScrollLayout")
        self.msgScrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgScrollArea.sizePolicy().hasHeightForWidth())
        self.msgScrollArea.setSizePolicy(sizePolicy)
        self.msgScrollArea.setMinimumSize(QtCore.QSize(600, 845))
        self.msgScrollArea.setAutoFillBackground(True)
        self.msgScrollArea.setStyleSheet("background-color: rgb(247, 136, 47);")
        self.msgScrollArea.setWidgetResizable(True)
        self.msgScrollArea.setObjectName("msgScrollArea")
        self.msgScrollContents = QtWidgets.QWidget()
        self.msgScrollContents.setGeometry(QtCore.QRect(0, 0, 598, 843))
        self.msgScrollContents.setObjectName("msgScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.msgScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.msgLayout = QtWidgets.QVBoxLayout()
        self.msgLayout.setObjectName("msgLayout")
        self.verticalLayout_2.addLayout(self.msgLayout)
        self.speakBtn = QtWidgets.QPushButton(self.msgScrollContents)
        self.speakBtn.setObjectName("speakBtn")
        self.verticalLayout_2.addWidget(self.speakBtn)
        self.msgScrollArea.setWidget(self.msgScrollContents)
        self.msgScrollLayout.addWidget(self.msgScrollArea)
        self.gridLayout.addLayout(self.msgScrollLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.speakBtn.clicked.connect(self.buttonClick)
        self.speechApp()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GatorWatch"))
        self.speakBtn.setText(_translate("Form", "Speak"))

    def buttonClick(self):
        self.speechApp()

    def rerun(self):
        global timeouts
        try:
            # with m as source: audio = r.listen(source)
            # userInput = r.recognize_google(audio)
            userInput = input("Input: ")
            return userInput

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            self.msgLayout.addWidget(MyWidget("GatorWatch: I'm sorry, I didn't get that. Can say that again?\n"))  
            Logging.write("System", "I'm sorry, I didn't get that. Can say that again?")
            playsound("packages/audio_files/misunderstood.mp3")
            userInput = None
            timeouts += 1
            return userInput

        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            self.msgLayout.addWidget(MyWidget("GatorWatch: Couldn't request results from Google Speech Recognition service. {0}\n".format(e)))
            Logging.write("System", "GatorWatch: Couldn't request results from Google Speech Recognition service.")
            playsound("packages/audio_files/google_fail.mp3")
            userInput = None
            return userInput

    def speechApp(self):
        global previousIntent
        global theaters
        global listings
        global start
        global negations
        global misunderstands
        global timeouts

        if start:
            Logging.write("System", "Hello! I’m GatorWatch - I help you find movies and TV shows!")
            self.msgLayout.addWidget(MyWidget("Hello! I’m GatorWatch - I help you find movies and TV shows!"))
            playsound("packages/audio_files/start1.mp3")

            Logging.write("System", "If you need help about with what you can do, ask!")
            self.msgLayout.addWidget(MyWidget("If you need help about with what you can do, ask!"))
            playsound("packages/audio_files/start2.mp3")

            start = False
            return

        try:
            print("Say something!")
            self.msgLayout.addWidget(MyWidget("Say something!\n"))
            
            # with m as source: audio = r.listen(source)

            try:
                # recognize speech using Google Speech Recognition
                # userInput = r.recognize_google(audio)
                userInput = input("Input: ")
                Logging.write("User", userInput)

                print("You said {}".format(userInput))
                self.msgLayout.addWidget(MyWidget(format(userInput), left=False))

                # Get the intent from a model
                interpretation = nlu.getInterpretation(userInput)
                print(interpretation)
                intent = interpretation["intent"]["name"]
                confidence = interpretation["intent"]["confidence"]
                entities = interpretation["entities"]
                print("The intent was " + str(intent))

                if (previousIntent is None):
                    previousIntent = intent

                # TODO: Find a way to handle low confidence intents
                if (confidence < 0.0):
                    Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                    self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                    playsound("packages/audio_files/misunderstood.mp3")

                # Display list of popular movies
                elif (intent == "recommend_movie"):
                    # Attempt to extract genres from the user input
                    # If we find genres, do a search with that list
                    # Otherwise return the default popular list
                    genreStringList = tmdbutils.getGenreStringList()
                    userGenres = []

                    for item in entities:
                        if (item["entity"] == "genre" and item["value"].title() in genreStringList):
                            userGenres.append(item["value"].title())

                    # If no genres specified, do default search
                    if not userGenres:
                        popularMovies = tmdbutils.getPopularMovies()

                        # Pick a random movie to say
                        random.seed()
                        number = random.randint(0, len(popularMovies))
                        output = GenerateAudio.generate(intent=intent, entities=[popularMovies[number].title, popularMovies[number].voteAverage])
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        os.remove("audio_files/temp.mp3")

                        for movieItem in popularMovies:
                            self.infoLayout.addWidget(MyWidget("Title: " + movieItem.title + " " + str(movieItem.voteAverage) + "\n"))

                    # Search for movies of the genre
                    else:
                        popularMoviesWithGenres = tmdbutils.getPopularMoviesWithGenre(userGenres)

                        # Pick a random movie to say
                        random.seed()
                        number = random.randint(0, len(popularMoviesWithGenres))
                        output = GenerateAudio.generate(intent=intent, entities=[popularMoviesWithGenres[number].title, userGenres, popularMoviesWithGenres[number].voteAverage])
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        os.remove("audio_files/temp.mp3")

                        for movieItem in popularMoviesWithGenres:
                            self.infoLayout.addWidget(MyWidget("Title: " + movieItem.title + " " + str(movieItem.voteAverage) + "\n"))

                elif (intent == "lookup_details"):
                    movieToLookup = None
                    
                    if (len(entities) != 0):
                        if (entities[0]["entity"] == "movie"):
                            movieToLookup = entities[0]["value"]

                    if movieToLookup is None or movieToLookup == "":
                        Logging.write("System", "Okay, what movie do you want to know more about?")
                        self.msgLayout.addWidget(MyWidget("Okay, what movie do you want to know more about?"))
                        playsound("packages/audio_files/find_movie.mp3")

                        while (movieToLookup is None or movieToLookup == ""):
                            movieToLookup = self.rerun()

                        Logging.write("User", movieToLookup)
                        self.msgLayout.addWidget(MyWidget(format(movieToLookup), left=False))
                        # Print what user says

                    output = GenerateAudio.generate(intent, entities=[movieToLookup])
                    movieToLookup = tmdbutils.searchForMovie(movieToLookup)
                    # print output to UI
                    # print movieToLookup on right side
                    Logging.write("System", output)
                    self.msgLayout.addWidget(MyWidget(output))
                    playsound("audio_files/temp.mp3")
                    os.remove("audio_files/temp.mp3")

                    # Display movies on the info screen

                # Command: Search show [show name]
                elif (intent == "show_tv"):
                    userTvShow = None
                    
                    if (len(entities) != 0):
                        if (entities[0]["entity"] == "tv_show"):
                            userTvShow = entities[0]["value"]

                    if userTvShow is None or userTvShow == "":
                        Logging.write("System", "Okay, what show do you want to look up?")
                        self.msgLayout.addWidget(MyWidget("Okay, what show do you want to look up?"))
                        playsound("packages/audio_files/show_tv_question.mp3")

                        while (userTvShow is None or userTvShow == ""):
                            userTvShow = self.rerun()

                        Logging.write("User", userTvShow)
                        self.msgLayout.addWidget(MyWidget(format(userTvShow), left=False))
                        # Print what user says

                    listings = GuideScraper.searchTVGuide(userTvShow)
                    if listings is None or len(listings) == 0:
                        # Couldn't find any TV shows
                        output = GenerateAudio.generate("no_tv_shows", entities=[userTvShow])

                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        os.remove("audio_files/temp.mp3")
                    
                    else:
                        # Found TV shows
                        output = GenerateAudio.generate(intent=intent, entities=[listings[0].name, listings[0].time])

                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        os.remove("audio_files/temp.mp3")

                        # Print listings to the table on info screen

                        for listing in listings:
                            self.infoLayout.addWidget(MyWidget("Name: " + listing.name + "\n"))
                            self.infoLayout.addWidget(MyWidget("Episode Name: " + listing.episode_name + "\n"))
                            self.infoLayout.addWidget(MyWidget("Episode: " + listing.episode + "\n"))
                            self.infoLayout.addWidget(MyWidget("Description: " + listing.description + "\n"))
                            self.infoLayout.addWidget(MyWidget("Channel: " + listing.channel + "\n"))
                            self.infoLayout.addWidget(MyWidget("Date: " + listing.date + "\n"))
                            self.infoLayout.addWidget(MyWidget("Time: " + listing.time + "\n"))
                            self.infoLayout.addWidget(MyWidget("-----------------\n"))

                # Command: Search local movies
                elif (intent == "show_local"):

                    theaters = LocalMoviesScraper.searchLocalMovies()
                    Logging.write("System", "Here are the Gainesville theaters and the movies they’re showing today.")
                    self.msgLayout.addWidget(MyWidget("Here are the Gainesville theaters and the movies they’re showing today."))
                    playsound("packages/audio_files/local_movies.mp3")

                    # Display theaters and associated movies on info screen

                    for theater in theaters:
                        self.infoLayout.addWidget(MyWidget("Theater: " + theater.name + "\n"))
                        self.infoLayout.addWidget(MyWidget("Address: " + theater.address + "\n"))
                        for movie in theater.movies:
                            self.infoLayout.addWidget(MyWidget("Movie Name: " + movie.name + "\n"))
                            self.infoLayout.addWidget(MyWidget("Duration: " + movie.duration + "\n"))
                            for item in movie.times:
                                self.infoLayout.addWidget(MyWidget("Time: " + item + "\n"))
                            self.infoLayout.addWidget(MyWidget("---------------\n"))
                
                elif intent == "view_calendar":
                    events = CalendarSystem.getCalendar()
                    Logging.write("System", "Okay, here is your calendar.")
                    playsound("packages/audio_files/show_calendar.mp3")

                    # Show calendar events on right side

                elif intent == "add_to_calendar":
                    if previousIntent == "show_local":
                        #print("Ask for theater")
                        Logging.write("System", "Okay, what's the movie theater? The Hippodrome, Royal Park, or Butler Town?")
                        self.msgLayout.addWidget(MyWidget("Okay, what's the movie theater? The Hippodrome, Royal Park, or Butler Town?"))
                        playsound("packages/audio_files/movie_theater_question.mp3")

                        theater_name = None
                        while True:
                            theater_name = None
                            # Get input and verify

                            while theater_name is None:
                                # print("What movie do you want to look up")
                                theater_name = self.rerun()

                            Logging.write("User", theater_name)
                            self.msgLayout.addWidget(MyWidget(format(theater_name), left=False))

                            # Need to verify if theater is one of the three - if it isn't, keep asking the user
                            # if theater_name.lower() != "hippodrome" and theater_name.lower() != "royal park" and theater_name.lower() != "butler town":
                            if "hippodrome" not in theater_name.lower() and "royal park" not in theater_name.lower() and "butler town" not in theater_name.lower():
                                Logging.write("System", "I'm sorry, that theater is not in Gainesville. The Gainesville theaters are: The Hippodrome, Royal Park, and Butler Town.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, that theater is not in Gainesville. The Gainesville theaters are: The Hippodrome, Royal Park, and Butler Town."))
                                playsound("packages/audio_files/invalid_theater.mp3")
                                misunderstands += 1

                            else:
                                break

                        # Ask for movie name
                        movie_name = None
                        Logging.write("System", "And the movie name?")
                        self.msgLayout.addWidget(MyWidget("And the movie name?"))
                        playsound("packages/audio_files/movie_name_question.mp3")

                        while True:
                            movie_name = None
                            while movie_name is None:
                                movie_name = self.rerun()

                            movie_exists = False

                            Logging.write("User", movie_name)
                            self.msgLayout.addWidget(MyWidget(format(movie_name), left=False))

                            # Need to verify if movie name exists
                            for theater in theaters:
                                if theater_name.lower() == theater.name.lower():
                                    for movie in theater.movies:
                                        tokens = movie_name.lower().split()

                                        for token in tokens:
                                            if token in movie.name.lower():
                                                #print("Movie exists")
                                                movie_exists = True
                                                break

                            if movie_exists:
                                break

                            else:
                                Logging.write("System", "I'm sorry, that movie does not exist. Please state one on the list.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, that movie does not exist. Please state one on the list."))
                                playsound("packages/audio_files/invalid_movie_name.mp3")
                                misunderstands += 1

                        # Ask for time

                        movie_time = None
                        Logging.write("System", "And the time of the movie?")
                        self.msgLayout.addWidget(MyWidget("And the time of the movie?"))
                        playsound("packages/audio_files/movie_time_question.mp3")

                        while True:
                            movie_time = None
                            while movie_time is None:
                                movie_time = self.rerun()

                            Logging.write("User", movie_time)
                            self.msgLayout.addWidget(MyWidget(format(movie_time), left=False))

                            movie_time_exists = False

                            # Verify if listing exists
                            for theater in theaters:
                                if theater_name.lower() == theater.name.lower():
                                    for movie in theater.movies:
                                        # Might need to tokenize movie_name

                                        tokens = movie_name.lower().split()

                                        for token in tokens:
                                            if token in movie.name.lower():
                                                #print("Movie exists")
                                                for start_time in movie.times:
                                                    if movie_time == start_time:
                                                        movie_time_exists = True
                                                        break

                            if movie_time_exists:
                                break

                            else:
                                #print("Err")
                                Logging.write("User", "That time is not available. Please state one on the list.")
                                self.msgLayout.addWidget(MyWidget("That time is not available. Please state one on the list."))
                                playsound("packages/audio_files/invalid_movie_time.mp3")
                                misunderstands += 1
                                # Movie time does not exist

                        #print("Confirm")
                        output = GenerateAudio.generate("confirm_movie", entities=[theater_name, movie_name, movie_time])
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        os.remove("audio_files/temp.mp3")

                        confidence = 0

                        while confidence < 0:
                            userInput = None
                            while userInput is None:
                                userInput = self.rerun()

                            # Need to find intent
                            interpretation = nlu.getInterpretation(userInput)
                            intent = interpretation["intent"]["name"]

                            # Incorporate confidence here

                            confidence = interpretation["intent"]["confidence"]
                            if (confidence < 0.0):
                                # print("Sorry, could you rephrase that?")
                                Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                                playsound("packages/audio_files/misunderstood.mp3")
                                confidence = 0
                                misunderstands += 1



                        if intent == "affirm":
                            # Add to calendar
                            # Calculate current date
                            months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
                            now = datetime.datetime.now()
                            month = now.month
                            day = now.day
                            date = ""

                            month = months[month]
                            day = str(day)

                            date += month + " " + day

                            listing = ShowListing(movie_name, "", "", "", theater_name, date, movie_time)
                            saved = CalendarSystem.saveCalendar(listing)

                            if saved == "True":
                                Logging.write("System","Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event.")
                                self.msgLayout.addWidget(MyWidget("Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event."))
                                playsound("packages/audio_files/add_to_calendar.mp3")

                            else:
                                output = GenerateAudio.generate("calendar_overlap", entities=[saved])
                                Logging.write("System", output)
                                self.msgLayout.addWidget(MyWidget(output))
                                playsound("audio_files/temp.mp3")
                                os.remove("audio_files/temp.mp3")

                        else:
                            intent = "show_local"
                            Logging.write("System", "Okay, not creating the event. What else do you want to do?")
                            self.msgLayout.addWidget(MyWidget("Okay, not creating the event. What else do you want to do?"))
                            playsound("packages/audio_files/not_creating_event.mp3")


                            #print("Do you want to change the theater, movie name, time, or cancel the event?")


                    elif previousIntent == "show_tv":
                        Logging.write("System", "Okay, what's the the name of the show that you want to add?")
                        self.msgLayout.addWidget(MyWidget("Okay, what's the the name of the show that you want to add?"))
                        playsound("packages/audio_files/show_name_question.mp3")

                        show_name = None
                        while True:
                            show_name = None
                            # Get input and verify
                            show_name_exists = False
                            while show_name is None:
                                # print("What show do you want to look up")
                                show_name = self.rerun()

                            Logging.write("User", show_name)
                            self.msgLayout.addWidget(MyWidget(format(show_name), left=False))

                            for listing in listings:
                                tokens = show_name.lower().split()
                                for token in tokens:
                                    if token in listing.name.lower():
                                        show_name_exists = True
                                        break

                            if show_name_exists:
                                break

                            else:
                                # show does not exist
                                Logging.write("System", "I'm sorry, I didn't find that TV show. Please choose from one of the listings I found.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't find that TV show. Please choose from one of the listings I found."))
                                playsound("packages/audio_files/invalid_show_name.mp3")
                                misunderstands += 1

                        Logging.write("System", "And the day of the show?")
                        self.msgLayout.addWidget(MyWidget("And the day of the show?"))
                        playsound("packages/audio_files/show_day_question.mp3")

                        show_day = None
                        while True:
                            show_day = None
                            show_day_exists = False
                            while show_day is None:
                                show_day = self.rerun()

                            Logging.write("User", show_day)
                            self.msgLayout.addWidget(MyWidget(format(show_day), left=False))

                            for listing in listings:
                                tokens = show_name.lower().split()
                                for token in tokens:
                                    if token in listing.name.lower():
                                        if show_day == listing.day:
                                            show_day_exists = True
                                            break

                            if show_day_exists:
                                break

                            else:
                                Logging.write("System", "I'm sorry, I didn't find that there is a showing on that day. Please say another day.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't find that there is a showing on that day. Please say another day."))
                                playsound("packages/audio_files/invalid_show_day.mp3")
                                misunderstands += 1

                        Logging.write("System", "And the time of the show?")
                        self.msgLayout.addWidget(MyWidget("And the time of the show?"))
                        playsound("packages/audio_files/show_time_question.mp3")

                        show_time = None
                        while True:
                            show_time = None
                            show_time_exists = False
                            while show_time is None:
                                show_time = self.rerun()

                            Logging.write("User", show_time)
                            self.msgLayout.addWidget(MyWidget(format(show_time), left=False))

                            event = None
                            for listing in listings:
                                tokens = show_name.lower().split()
                                for token in tokens:
                                    if token in listing.name.lower():
                                        if show_day == listing.day:
                                            if show_time == listing.time:
                                                show_time_exists = True
                                                event = listing
                                                break

                            if show_time_exists:
                                break

                            else:
                                Logging.write("System", "I'm sorry, I didn't find that there is a showing at that time. Please say another time.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't find that there is a showing at that time. Please say another time."))
                                playsound("packages/audio_files/invalid_show_time.mp3")
                                misunderstands += 1

                        #print("Confirm")
                        output = GenerateAudio.generate("confirm_show", entities=[show_name, show_day, show_time])
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        os.remove("audio_files/temp.mp3")

                        confidence = 0

                        while confidence < 0:
                            userInput = None
                            while userInput is None:
                                userInput = self.rerun()

                            # Need to find intent
                            interpretation = nlu.getInterpretation(userInput)
                            intent = interpretation["intent"]["name"]

                            # Incorporate confidence here

                            confidence = interpretation["intent"]["confidence"]
                            if (confidence < 0.0):
                                # print("Sorry, could you rephrase that?")
                                Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                                playsound("packages/audio_files/misunderstood.mp3")
                                confidence = 0
                                misunderstands += 1


                        if intent == "affirm":
                            saved = CalendarSystem.saveCalendar(event)

                            if saved == "True":
                                Logging.write("System","Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event.")
                                self.msgLayout.addWidget(MyWidget("Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event."))
                                playsound("packages/audio_files/add_to_calendar.mp3")

                            else:
                                output = GenerateAudio.generate("calendar_overlap", entities=[saved])
                                Logging.write("System", output)
                                self.msgLayout.addWidget(MyWidget(output))
                                playsound("audio_files/temp.mp3")
                                os.remove("audio_files/temp.mp3")

                        else:
                            negations += 1
                            intent = "show_tv"
                            Logging.write("System", "Okay, not creating the event. What else do you want to do?")
                            self.msgLayout.addWidget(MyWidget("Okay, not creating the event. What else do you want to do?"))
                            playsound("packages/audio_files/not_creating_event.mp3")

                    else:
                        #print("Cannot do that")
                        Logging.write("System", "You can only add events to the calendar after viewing local movies or looking up a TV show.")
                        self.msgLayout.addWidget(MyWidget("You can only add events to the calendar after viewing local movies or looking up a TV show."))
                        playsound("packages/audio_files/cannot_add_event.mp3")

                elif intent == "remove_from_calendar":
                    if previousIntent == "view_calendar":
                        events = CalendarSystem.getCalendar()
                        if len(events) == 0:
                            Logging.write("System", "You have no events to delete!")
                            self.msgLayout.addWidget(MyWidget("You have no events to delete!"))
                            playsound("packages/audio_files/no_events.mp3")

                        else:
                            #print("Ask for day")
                            Logging.write("System", "Okay, what is the day of the event that you want to delete?")
                            self.msgLayout.addWidget(MyWidget("Okay, what is the day of the event that you want to delete?"))
                            playsound("packages/audio_files/event_day_question.mp3")

                            event_day = None
                            while True:
                                event_day = None
                                event_day_exists = False

                                while event_day is None:
                                    event_day = self.rerun()

                                Logging.write("User", event_day)
                                self.msgLayout.addWidget(MyWidget(format(event_day), left=False))

                                if event_day_exists:
                                    break
                                else:
                                    Logging.write("System", "You have no event at on that date. Please state another date.")
                                    self.msgLayout.addWidget(MyWidget("You have no event on that date. Please state another date."))
                                    playsound("packages/audio_files/invalid_event_day.mp3")
                                    misunderstands += 1


                            #print("Ask for time")
                            Logging.write("System", "And the time of the event?")
                            self.msgLayout.addWidget(MyWidget("And the time of the event?"))
                            playsound("packages/audio_files/event_time_question.mp3")

                            event_time = None
                            while True:
                                event_time = None
                                event_time_exists = False

                                while event_time is None:
                                    # print("What movie do you want to look up")
                                    event_time = self.rerun()

                                Logging.write("User", event_time)
                                self.msgLayout.addWidget(MyWidget(format(event_time), left=False))

                                if event_time_exists:
                                    break

                                else:
                                    Logging.write("System", "You have no event at that time. Please state another time.")
                                    self.msgLayout.addWidget(MyWidget("You have no event at that time. Please state another time."))
                                    playsound("packages/audio_files/invalid_event_time.mp3")
                                    misunderstands += 1

                            output = GenerateAudio.generate("confirm_deletion", entities=[event_day, event_time])
                            Logging.write("System", output)
                            self.msgLayout.addWidget(MyWidget(output))
                            playsound("audio_files/temp.mp3")
                            os.remove("audio_files/temp.mp3")

                            confidence = 0

                            while confidence < 0:
                                userInput = None
                                while userInput is None:
                                    userInput = self.rerun()

                                # Need to find intent
                                interpretation = nlu.getInterpretation(userInput)
                                intent = interpretation["intent"]["name"]

                                confidence = interpretation["intent"]["confidence"]
                                if (confidence < 0.0):
                                    # print("Sorry, could you rephrase that?")
                                    Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                                    self.msgLayout.addWidget(
                                        MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                                    playsound("packages/audio_files/misunderstood.mp3")
                                    confidence = 0
                                    misunderstands += 1


                            if intent == "affirm":
                                CalendarSystem.deleteEvent(event_day, event_time)
                                Logging.write("System", "Okay, the event has been deleted from your calendar.")
                                self.msgLayout.addWidget(MyWidget("Okay, the event has been deleted from your calendar."))
                                playsound("packages/audio_files/event_deleted.mp3")

                            else:
                                negations += 1
                                intent = "view_calendar"
                                Logging.write("System", "Okay, the event won't be deleted. What else do you want to do?")
                                self.msgLayout.addWidget(MyWidget("Okay, the event won't be deleted. What else do you want to do?"))
                                playsound("packages/audio_files/not_deleting_event.mp3")

                    # Cannot delete event unless the user has just viewed local movies or TV listings
                    else:
                        Logging.write("System", "I'm sorry, you cannot delete an event unless you have just viewed the calendar. View your calendar first before deleting.")
                        self.msgLayout.addWidget(MyWidget("I'm sorry, you cannot delete an event unless you have just viewed the calendar. View your calendar first before deleting."))
                        playsound("packages/audio_files/cannot_delete.mp3")

                elif intent == "show_instructions":
                    Logging.write("System", "You can ask for what’s showing around here today, movie suggestions, or information about a TV show or movie. You also have a calendar to store TV shows or movie events.")
                    self.msgLayout.addWidget(MyWidget("You can ask for what’s showing around here today, movie suggestions, or information about a TV show or movie. You also have a calendar to store TV shows or movie events."))
                    playsound("packages/audio_files/commands.mp3")

                elif intent == "calendar_question":
                    Logging.write("System", "The calendar stores listings for TV shows and local movies and reminds you thirty minutes before they happen. You can tell me to add any TV show or local movie listing to the calendar.")
                    self.msgLayout.addWidget(MyWidget("The calendar stores listings for TV shows and local movies and reminds you thirty minutes before they happen. You can tell me to add any TV show or local movie listing to the calendar."))
                    playsound("packages/audio_files/calendar.mp3")

                elif intent == "bye":
                    Logging.write("System", "Okay, see you later!")
                    self.msgLayout.addWidget(MyWidget("Okay, see you later!"))
                    playsound("packages/audio_files/calendar.mp3")
                    sys.exit()

                previousIntent = intent
            
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can say that again?\n"))
                Logging.write("System", "I'm sorry, I didn't get that. Can say that again?")
                playsound("packages/audio_files/misunderstood.mp3")
                timeouts += 1

            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                self.msgLayout.addWidget(MyWidget("Couldn't request results from Google Speech Recognition service. {0}\n".format(e)))
                Logging.write("System", "Couldn't request results from Google Speech Recognition service.")
                playsound("packages/audio_files/google_fail.mp3")
            
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    r = sr.Recognizer() 
    m = sr.Microphone()
    print("A moment of silence, please...")
    # with m as source: r.adjust_for_ambient_noise(source)
    # print("Set minimum energy threshold to {}".format(r.energy_threshold))

    theaters = []
    listings = []
    previousIntent = None
    start = True

    negations = 0
    misunderstands = 0
    timeouts = 0

    try:
        os.remove("audio_files/temp.mp3")
    except:
        print("No file to remove")

    ex = App()
    try:
        ex.show()
        sys.exit(app.exec_())
    finally:
        Logging.end()
