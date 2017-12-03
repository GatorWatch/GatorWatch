# -*- coding: utf-8 -*-
#!/usr/bin/python3

from packages import GuideScraper
from packages import LocalMoviesScraper
from packages import tmdbutils
from packages import nlu
import speech_recognition as sr
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QAction, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
import sys
from playsound import playsound
import time
from packages import GenerateAudio
import random
from packages import Logging

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
        self.setWordWrap(True)
        self.setSizePolicy

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
        self.tableWidget = QtWidgets.QTableWidget(self.infoScrollContents)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("background-color: rgb(107, 122, 143);")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setRowCount(500)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.infoLayout.addWidget(self.tableWidget)            
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
        self.currRow = 0
        #variable to know which table header to print 0=tmdb_movies, 1=local_movies, 2= tv show, 3 =calender
        self.tableMode= 0
        self.speechApp()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GatorWatch"))
        self.speakBtn.setText(_translate("Form", "Speak"))

    def buttonClick(self):
        self.speechApp()

    def rerun(self):
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

        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            self.msgLayout.addWidget(MyWidget("GatorWatch: Couldn't request results from Google Speech Recognition service. {0}\n".format(e)))
            Logging.write("System", "GatorWatch: Couldn't request results from Google Speech Recognition service.")
            playsound("packages/audio_files/google_fail.mp3")
            userInput = None

    def speechApp(self):
        global previousIntent
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
                    print("Sorry, could you rephrase that?")
                    self.msgLayout.addWidget(MyWidget("GatorWatch: I'm sorry, I don't understand. Can you repeat that?\n"))

                # Display list of popular movies
                elif (intent == "recommend_movie"):
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 0):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Title"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Rating Average"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Summary"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Genres"))
                            self.currRow+=1
                            self.tableMode = 0
                    else:    
                        if (self.tableMode != 0):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Title"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Rating Average"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Summary"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Genres"))
                            self.currRow+=1
                            self.tableMode = 0

                    # Attempt to extract genres from the user input
                    # If we find genres, do a search with that list
                    # Otherwise return the default popular list
                    genreStringList = tmdbutils.getGenreStringList()
                    userGenres = []

                    for item in entities:
                        if (item["entity"] == "genre" and item["value"].title() in genreStringList):
                            userGenres.append(item["value"].title())

                    # If no genres specified, do default search
                    #playsound(popular_movies)
                    if not userGenres:
                        popularMovies = tmdbutils.getPopularMovies()

                        # Pick a random movie to say
                        random.seed()
                        number = random.randint(0, len(popularMovies))
                        output = GenerateAudio.generate(intent=intent, entities=[popularMovies[number].title])
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")

                        itemLength = len(popularMovies)
                        if (itemLength+self.currRow < 499):
                            for movieItem in popularMovies:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for movieItem in popularMovies:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1

                    else:
                        popularMoviesWithGenres = tmdbutils.getPopularMoviesWithGenre(userGenres)
                        itemLength = len(popularMoviesWithGenres)
                        if (itemLength+self.currRow < 499):
                            for movieItem in popularMoviesWithGenres:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for movieItem in popularMoviesWithGenres:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1

                elif (intent == "lookup_details"):
                    movieToLookup = None
                    
                    if (len(entities) != 0):
                        if (entities[0]["entity"] == "movie"):
                            movieToLookup = entities[0]["value"]

                    while (movieToLookup is None or movieToLookup == ""):
                        print("What movie do you want to look up")
                        movieToLookup = self.rerun()

                    movieToLookup = tmdbutils.searchForMovie(movieToLookup)
                    print(movieToLookup[0].title)

                # Command: Search show [show name]
                elif (intent == "show_tv"):
                    userTvShow = None
                    
                    if (len(entities) != 0):
                        if (entities[0]["entity"] == "tv_show"):
                            userTvShow = entities[0]["value"]

                    while (userTvShow is None or userTvShow == ""):
                        print("What show do you want to search for?")
                        userTvShow = self.rerun()

                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 2):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Name"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Episode Name"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Episode #"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Description"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Channel"))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem("Date"))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 2
                    else:    
                        if (self.tableMode != 2):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Name"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Episode Name"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Episode #"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Description"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Channel"))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem("Date"))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 2
                    listings = GuideScraper.searchTVGuide(userTvShow)
                    itemLength = len(listings)
                    if listings is None or len(listings) == 0:
                        print("Couldn't find anything")
                    
                    else:
                        output = GenerateAudio.generate(intent=intent, entities=[listings[0].name, listings[0].time])
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        playsound("audio_files/temp.mp3")
                        if(itemLength+self.currRow < 499):
                            for listing in listings:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(listing.name))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(listing.episode_name))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(listing.episode))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(listing.description))
                                self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(listing.channel))
                                self.tableWidget.setItem(self.currRow,5, QTableWidgetItem(listing.date))
                                self.tableWidget.setItem(self.currRow,6, QTableWidgetItem(listing.time))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for listing in listings:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(listing.name))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(listing.episode_name))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(listing.episode))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(listing.description))
                                self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(listing.channel))
                                self.tableWidget.setItem(self.currRow,5, QTableWidgetItem(listing.date))
                                self.tableWidget.setItem(self.currRow,6, QTableWidgetItem(listing.time))
                                self.currRow+=1
                # Command: Search local movies
                elif (intent == "show_local"):

                    Logging.write("System", "Here are the Gainesville theaters and the movies they’re showing today.")
                    playsound("packages/audio_files/local_movies.mp3")
                    self.msgLayout.addWidget(MyWidget("Here are the Gainesville theaters and the movies they’re showing today."))
                    theaters = LocalMoviesScraper.searchLocalMovies()
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 1):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Theater"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Address"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Movie Name"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Duration"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 1
                    else:    
                        if (self.tableMode != 1):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Theater"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Address"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Movie Name"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Duration"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 1
                    if(self.currRow+90 <= 499):
                        for theater in theaters:
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(theater.name))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(theater.address))
                            for movie in theater.movies:
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movie.name))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(movie.duration))
                                for time in movie.times:
                                    self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(time))
                                    self.currRow+=1
                                self.currRow+=1
                            self.currRow+=1
                    else:
                        self.tableWidget.clear()
                        self.currRow= 0
                        for theater in theaters:
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(theater.name))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(theater.address))
                            for movie in theater.movies:
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movie.name))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(movie.duration))
                                for time in movie.times:
                                    self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(time))
                                    self.currRow+=1
                                self.currRow+=1
                            self.currRow+=1
                
                elif intent == "view_calendar":
                    print("view calendar")

                elif intent == "add_to_calendar":
                    if previousIntent == "show_local":
                        print("Ask for theater")
                        print("Ask for movie")
                        print("Ask for time")
                        # Verify if listing exists
                        print("Confirm")
                        if intent == "affirm":
                            print("Add to calendar")
                        else:
                            print("Do you want to change the theater, movie name, time, or cancel the event?")
                    elif previousIntent == "show_tv":
                        print("TV name")
                        print("Time")
                        # Verify if listing exists
                        print("Confirm")
                        if intent == "affirm":
                            print("OK")
                        else:
                            print("Do you want to change the show name, time, or cancel the event?")

                elif intent == "remove_from_calendar":
                    if previousIntent == "view_calendar":
                        print("Ask for name")
                        print("Ask for time")
                        # Verify if listing exists
                        print("Confirm")
                        if intent == "affirm":
                            print("Remove from calendar")
                        else:
                            print("Cancel the deletion?")

                    else:
                        print("Cannot do that")

                elif intent == "show_instructions":
                    print("play instr")
`
                previousIntent = intent
            
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                self.msgLayout.addWidget(MyWidget("GatorWatch: I'm sorry, I didn't get that. Can say that again?\n"))
                Logging.write("System", "I'm sorry, I didn't get that. Can say that again?")
                playsound("packages/audio_files/misunderstood.mp3")

            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                self.msgLayout.addWidget(MyWidget("GatorWatch: Couldn't request results from Google Speech Recognition service. {0}\n".format(e)))
                Logging.write("System", "GatorWatch: Couldn't request results from Google Speech Recognition service.")
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

    Logging.write("System", "Hello! I’m GatorWatch - I help you find movies and TV shows!")
    playsound("packages/audio_files/start1.mp3")

    Logging.write("System", "If you need help about with what you can do, ask!")
    playsound("packages/audio_files/start2.mp3")

    previousIntent = None

    ex = App()
    try:
        ex.show()
        sys.exit(app.exec_())
    finally:
        Logging.end()
