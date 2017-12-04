from gtts import gTTS
from playsound import playsound

# Generate the preset audio files
def generate_presets1():
    language = "en"

    '''
    Start
    '''

    text = "Hello! I’m GatorWatch - I help find movies and TV shows!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/start1.mp3")
    #playsound("audio_files/start1.mp3")

    text = "If you need help about with what you can do, ask!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/start2.mp3")

    text = "I'm a virtual assistant that can help find movies and TV shows. You can ask for help any time!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/intro.mp3")
    #playsound("audio_files/intro.mp3")

    text = "You can ask for what’s showing around here today, movie suggestions, or information about a TV show or movie. You also have a calendar to store TV shows or movie events."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/commands.mp3")
    #playsound("audio_files/commands.mp3")

    text = "The calendar stores listings for TV shows and local movies and reminds you thirty minutes before they happen. You can tell me to add any TV show or local movie listing to the calendar."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/calendar.mp3")
    #playsound("audio_files/calendar.mp3")

    text = "Okay, see you later!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/bye.mp3")

    '''
    Misunderstand/error
    '''

    text = "I'm sorry, I didn't get that. Can you rephrase that?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/misunderstood.mp3")
    #playsound("audio_files/misunderstood.mp3")

    text = "I’m sorry, I cannot do that. If you need help about what you can do, ask!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_command.mp3")
    #playsound("audio_files/invalid_command.mp3")

    text = "I’m sorry, I’m currently having problems connecting to the internet."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/no_internet.mp3")
    #playsound("audio_files/no_internet.mp3")

    text = "Couldn't request results from Google Speech Recognition service."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/google_fail.mp3")

    '''
    Show movie/TV show
    '''
    text = "Ok, what movie do you want to know more about?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/find_movie.mp3")
    #playsound("audio_files/find_movie.mp3")

    text = "Okay, what else do you want to do?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/continue.mp3")
    #playsound("audio_files/continue.mp3")


    text = "Ok, what show do you want to look for?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/find_show.mp3")
    #playsound("audio_files/find_show.mp3")

    text = "Here are the Gainesville theaters and the movies they’re showing today."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/local_movies.mp3")
    #playsound("audio_files/local_movies.mp3")



    '''
    Calendar
    '''
    text = "Okay, here is your calendar."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/show_calendar.mp3")
    #playsound("audio_files/show_calendar.mp3")

    text = "Ok, are you sure you want to delete your entire calendar?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/clear_calendar_question.mp3")
    #playsound("audio_files/clear_calendar_question.mp3")

    text = "Okay, your calendar is empty."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/clear_calendar_yes.mp3")
    #playsound("audio_files/clear_calendar_yes.mp3")

    text = "Okay, your calendar will not be cleared."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/clear_calendar_no.mp3")
    #playsound("audio_files/clear_calendar_no.mp3")

    text = "Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/add_to_calendar.mp3")

def generate_presets2():
    language = "en"
    '''
    Calendar Corrections
    '''
    text = "I'm sorry, that theater is not in Gainesville. "
    text += "The Gainesville theaters are: The Hippodrome, Royal Park, and Butler Town."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_theater.mp3")

    text = "I'm sorry, that movie does not exist. Please state one on the list."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_movie_name.mp3")

    text = "That time is not available. Please state one on the list."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_movie_time.mp3")

    text = "I'm sorry, I didn't find that TV show. Please choose from one of the listings I found."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_show_name.mp3")

    text = "I'm sorry, I didn't find that there is a showing on that day. Please say another day."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_show_day.mp3")

    text = "I'm sorry, I didn't find that there is a showing at that time. Please say another time."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_show_time.mp3")

    text = "You can only add events to the calendar after viewing local movies or looking up a TV show."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/cannot_add_event.mp3")

    '''
    Restrictive prompts
    '''

    text = "Okay, what show do you want to look up?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/show_tv_question.mp3")

    text = "Okay, what do you want to search for?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/lookup_details_question.mp3")

    text = "Okay, what's the movie theater? The Hippodrome, Royal Park, or Butler Town?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/movie_theater_question.mp3")

    text = "And the movie name?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/movie_name_question.mp3")

    text = "And the time of the movie?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/movie_time_question.mp3")

    text = "Okay, what's the the name of the show that you want to add?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/show_name_question.mp3")

    text = "And the day of the show?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/show_day_question.mp3")

    text = "And the time of the show?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/show_time_question.mp3")

    '''
    Calendar deletion
    '''
    text = "I'm sorry, you cannot delete an event unless you have just viewed the calendar. View your calendar first before deleting."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/cannot_delete.mp3")

    text = "You have no events to delete!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/no_events.mp3")

    text = "Okay, what is the day of the event that you want to delete?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/event_day_question.mp3")

    text = "You have no event at on that date. Please state another date."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_event_day.mp3")

    text = "And the time of the event?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/event_time_question.mp3")

    text = "You have no event at that time. Please state another time."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_event_time.mp3")

    text = "Okay, the event has been deleted from your calendar."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/event_deleted.mp3")

    text = "Okay, the event won't be created. What else do you want to do?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/not_creating_event.mp3")

    text = "Okay, the event won't be deleted. What else do you want to do?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/not_deleting_event.mp3")


# Generates an audio file given the intent and entities
# Returns a string of what the audio file says
def generate(intent, entities, num):
    output = ""
    if intent == "lookup_details" and entities is not None:
        output += scripts["lookup_details"] # Name
        output += entities[0]

    elif intent == "show_tv" and entities is not None:
        months = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June", "Jul": "July",
                  "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
        output += scripts["show_tv1"]
        output += entities[0]   # TV show name
        output += scripts["show_tv2"]
        output += entities[1]   # time
        output += scripts["show_tv3"]

        tokens = entities[2].split()
        output += months[tokens[0]]   # month
        output += " " + tokens[1]
        output += "."

    elif intent == "add_to_calendar" and entities is not None:
        output += scripts["add_to_calendar1"]
        output += entities[0]
        output += scripts["add_to_calendar2"]

    elif intent == "remove_from_calendar" and entities is not None:
        output += scripts["remove_from_calendar1"]
        output += entities[0]
        output += scripts["remove_from_calendar2"]

    elif intent == "recommend_movie" and entities is not None:
        output += scripts["recommend_movie1"]
        output += entities[0]   # Movie title
        output += scripts["recommend_movie2"]
        output += str(entities[1])   # Movie rating
        output += "."

    elif intent == "recommend_movie_genre" and entities is not None:
        output += scripts["recommend_movie_genre1"]
        output += entities[0]   # Genre
        output += scripts["recommend_movie_genre2"]
        output += entities[1]   # Movie title
        output += scripts["recommend_movie_genre3"]
        output += str(entities[2])   # Movie rating


    elif intent == "no_tv_shows" and entities is not None:
        output += scripts["no_tv_shows"]
        output += entities[0]

    elif intent == "confirm_movie" and entities is not None:
        output += scripts["confirm_movie1"]
        output += entities[0]   # Theater
        output += scripts["confirm_movie2"]
        output += entities[1]   # Movie name
        output += scripts["confirm_movie3"]
        output += entities[2]   # Time
        output += scripts["confirm_movie4"]

    elif intent == "confirm_show" and entities is not None:
        output += scripts["confirm_show1"]
        output += entities[0]   # Show name
        output += scripts["confirm_movie2"]
        output += entities[1]   # Show day
        output += scripts["confirm_movie3"]
        output += entities[2]   # Show time
        output += scripts["confirm_movie4"]

    elif intent == "confirm_deletion" and entities is not None:
        output += scripts["confirm_deletion1"]
        output += entities[0]   # Event day
        output += scripts["confirm_deletion2"]
        output += entities[1]   # Event time
        output += scripts["confirm_deletion3"]

    elif intent == "calendar_overlap" and entities is not None:
        output += scripts["calendar_overlap1"]
        output += entities[0]   # Event name
        output += scripts["calendar_overlap2"]

    language = "en"
    audio = gTTS(text=output, lang=language, slow=False)
    path = "audio_files/temp" + str(num) + ".mp3"
    audio.save(path)
    #playsound("audio_files/temp.mp3")
    return output


scripts = {}
scripts["lookup_details"] = "Okay, here's information about "
scripts["recommend_movie1"] = "Okay, here are some popular movies. "
scripts["recommend_movie2"] = " is a popular movie with a TMDB rating of "
scripts["recommend_movie_genre1"] = "Okay, here are some "
scripts["recommend_movie_genre2"] = " movies. "
scripts["recommend_movie_genre3"] = " is a popular movie with a TMDB rating of "
scripts["movie_more_info1"] = "Okay, it has a rating of "
scripts["movie_more_info2"] = ". The description is: "
scripts["show_tv1"] = "Okay, here are listings for "
scripts["show_tv2"] = ". There is a showing at "
scripts["show_tv3"] = " on "
scripts["add_to_calendar1"] = "Okay, "
scripts["add_to_calendar2"] = " has been added to your calendar."
scripts["remove_from_calendar1"] = "Okay, "
scripts["remove_from_calendar2"] = " has been removed from your calendar."
scripts["confirm_movie1"] = "Okay, so an event at the "
scripts["confirm_movie2"] = " to see "
scripts["confirm_movie3"] = " at "
scripts["confirm_movie4"] = ". Do you want to add this?"
scripts["confirm_show1"] = "Okay, so an event to see "
scripts["confirm_show2"] = " on "
scripts["confirm_show3"] = " at "
scripts["confirm_show4"] = ". Do you want to add this?"
scripts["confirm_deletion1"] = "Okay, so you want to delete the event on "
scripts["confirm_deletion2"] = " at "
scripts["confirm_deletion3"] = " . Is that correct?"
scripts["no_tv_shows"] = "I'm sorry, I couldn't find anything about "
scripts["calendar_overlap1"] = "There is already an event to watch "
scripts["calendar_overlap2"] = " at that time! I cannot save this event"
#print(scripts["movie_info"])

#generate("There is a showing on November 27 at 9:30 AM.")

# text = "There is a showing on November 27 at 9:30AM."
# audio = gTTS(text=text, lang="en", slow=False)
# audio.save("test.mp3")
#
# text = "Test"
# audio = gTTS(text=text, lang="en", slow=False)
# audio.save("test.mp3")

# playsound("test.mp3")

#generate_presets1()
#generate_presets2()
