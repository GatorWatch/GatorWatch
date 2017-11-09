from gtts import gTTS
from playsound import playsound

def speak(text, option = None):
    # Speak a predetermined response
    if option is not None:
        if option == "welcome":
            playsound("audio_files/welcome.mp3")
        elif option == "intro":
            playsound("audio_files/intro.mp3")
        elif option == "commands":
            playsound("audio_files/commands.mp3")
        elif option == "misunderstood":
            playsound("audio_files/misunderstood.mp3")
        elif option == "invalid_command":
            playsound("audio_files/invalid_command.mp3")
        elif option == "no_internet":
            playsound("audio_files/no_internet.mp3")

    # Create a given custom response
    else:
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save("audio_files/audio.mp3")
        playsound("audio_files/audio.mp3")
