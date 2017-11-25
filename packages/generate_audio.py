import gtts as gTTS
from playsound import playsound

def generate():
    text = "Hello! I’m GatorWatch! If you need help about what you can do, ask!"
    language = "en"

    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/start.mp3")
    playsound("audio_files/start.mp3")

    text = "I am a virtual assistant that can help you find movies and TV shows. If you need help about what you can do, ask!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/intro.mp3")
    playsound("audio_files/intro.mp3")

    text = "You can say: \“What’s showing around here?\”, \“Suggest me a movie\”, or \“Tell me about a show\”."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/commands.mp3")
    playsound("audio_files/commands.mp3")

    text = "I’m sorry, I didn’t get that. Can you say that again?"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/misunderstood.mp3")
    playsound("audio_files/misunderstood.mp3")

    text = "I’m sorry, I cannot do that. If you need help about what you can do, ask!"
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/invalid_command.mp3")
    playsound("audio_files/invalid_command.mp3")

    text = "I’m sorry, I’m currently having problems connecting to the internet."
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("audio_files/no_internet.mp3")
    playsound("audio_files/no_internet.mp3")
