import os

rec = "sox -t alsa default recording.wav silence 1 0.1 2% 1 0.5 2%"

decode = "multimon-ng -t wav -a DTMF recording.wav > out.txt"

while True:
    #listen for audio
    os.system(rec)
    
    #decode the audio from audio file
    os.system(decode)

    #store full result in a variable
    results = open("out.txt").read()
    results = results.split()

    try:
        print((results[results.index("DTMF:") + 1]).center(50, "*"))        #For debugging
    except:
        pass