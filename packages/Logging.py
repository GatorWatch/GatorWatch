import datetime
import time
import os

def write(speaker, utterance):
    global text
    global f
    #f = open(text, "w+")
    curr_time = time.time()
    delta = float(curr_time) - float(start_time)
    delta = str(delta)
    text = speaker + ": " + utterance + " - " + delta + "\r\n"
    f.write(text)
    #f.close()

def end(negations, misunderstands, timeouts):
    global text
    global f
    #f = open(text, "w+")
    end_time = time.time()
    text = "End Seconds: " + str(end_time) + "\r\n"
    f.write(text)

    delta = float(end_time) - float(start_time)
    delta = str(delta)
    line = "Elapsed time: " + delta + "\r\n"
    f.write(line)

    line = "Negations: " + str(negations) + "\r\n"
    f.write(line)

    line = "Misunderstands: " + str(misunderstands) + "\r\n"
    f.write(line)

    line = "Timeouts: " + str(timeouts) + "\r\n"
    f.write(line)
    f.close()

# Create a text file which will hold dialogue
arr = os.listdir()
now = datetime.datetime.now()
text = str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)
text += ".log"
i = 0

# Check to see if the file already exists - create a new file if so
while text in arr:
    text = str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "_" + str(i)
    text += ".log"
    i += 1

start_time = time.time()
f = open(text,"w+")
curr_time = "Start Seconds: " + str(start_time) + "\r\n"
f.write(curr_time)
#f.close()
