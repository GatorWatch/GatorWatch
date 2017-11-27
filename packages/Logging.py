import datetime
import time

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
now = datetime.datetime.now()
text = str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)
text += ".txt"

start_time = time.time()
f = open(text,"w+")
curr_time = "Start Seconds: " + str(start_time) + "\r\n"
f.write(curr_time)
