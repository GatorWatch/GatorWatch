#!/usr/bin/python3

from tkinter import *
import speech_recognition as sr


def speechApp():
    try:
        print("Say something!")
        T.insert(INSERT, "Say something!\n")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        T.insert(INSERT, "Got it! Now to recognize it...\n")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                T.insert(INSERT, u"You said {}\n".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
                T.insert(INSERT, "You said {}\n".format(value))
        except sr.UnknownValueError:
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