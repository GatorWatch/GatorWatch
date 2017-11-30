import datetime
import time
import os

def write(speaker, utterance):
    text = speaker + ": " + utterance + "\r\n"
    f.write(text)

def end():
    end_time = time.time()
    text = "End Seconds: " + str(end_time) + "\r\n"
    f.write(text)

    delta = float(end_time) - float(start_time)
    delta = str(delta)
    line = "Elapsed time: " + delta
    f.write(line)
    f.close()

# Create a text file which will hold dialogue
arr = os.listdir()
now = datetime.datetime.now()
text = str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)
text += ".txt"
i = 0

# Check to see if the file already exists - create a new file if so
while text in arr:
    text = str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "_" + str(i)
    text += ".txt"
    i += 1

start_time = time.time()
f = open(text,"w+")
curr_time = "Start Seconds: " + str(start_time) + "\r\n"
f.write(curr_time)
