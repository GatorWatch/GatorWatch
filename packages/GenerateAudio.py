from gtts import gTTS
from playsound import playsound

# Generate the preset audio files
def generate_presets():
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

    text = "You can ask for what’s showing around here, movie suggestions, or information about a TV show or movie. You also have a calendar to store TV shows or movie events."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/commands.mp3")
    #playsound("audio_files/commands.mp3")

    text = "The calendar stores listings for TV shows and movies and reminds you thirty minutes before they happen. You can tell me to add any TV show or movie listing to the calendar."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/calendar.mp3")
    #playsound("audio_files/calendar.mp3")

    '''
    Misunderstand/error
    '''

    text = "I’m sorry, I didn’t get that. Can you say that again?"
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

# Generates an audio file given the intent and entities
# Returns a string of what the audio file says
def generate(intent, entities):
    output = ""
    if intent == "lookup_details" and entities is not None:
        output += scripts["lookup_details"] # Name
        output += entities[0]

    elif intent == "show_tv" and entities is not None:
        output += scripts["show_tv1"]
        output += entities[0]   # TV show name
        output += scripts["show_tv2"]
        output += entities[1]   # time
        output += scripts["show_tv3"]

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
        output += entities[0]
        output += scripts["recommend_movie2"]

    language = "en"
    audio = gTTS(text=output, lang=language, slow=False)
    audio.save("audio_files/temp.mp3")
    #playsound("audio_files/temp.mp3")
    return output


scripts = {}
scripts["lookup_details"] = "Okay, here's information about "
scripts["recommend_movie1"] = "Okay, here are some popular movies. "
scripts["recommend_movie2"] = " is a popular one. Do you want to know more about it?"
scripts["movie_more_info1"] = "Okay, it has a rating of "
scripts["movie_more_info2"] = ". The description is: "
scripts["show_tv1"] = "Okay, here are listings for "
scripts["show_tv2"] = ". There is a showing at "
scripts["show_tv3"] = ". Do you want to add it to your calendar?"
scripts["add_to_calendar1"] = "Okay, "
scripts["add_to_calendar2"] = " has been added to your calendar."
scripts["remove_from_calendar1"] = "Okay, "
scripts["remove_from_calendar2"] = " has been removed from your calendar."
#print(scripts["movie_info"])

#generate("There is a showing on November 27 at 9:30 AM.")
#generate_presets()