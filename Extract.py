# SoundCrypt Ver 1.0
# Powered by Securegarv
# Hide your secret text in wave audio file.
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True
def cls():
  os.system("clear")
def help():
  print("\033[92mExtract Your Secret Message from Audio Wave File.\033[0m")
  print ('''usage: Xwave.py [-h] [-f AUDIOFILE]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File''')

def banner():
    print ('''

   _____                       _  _____                  _
  / ____|                     | |/ ____|                | |
 | (___   ___  _   _ _ __   __| | |     _ __ _   _ _ __ | |_
  \___ \ / _ \| | | | '_ \ / _` | |    | '__| | | | '_ \| __|
  ____) | (_) | |_| | | | | (_| | |____| |  | |_| | |_) | |_
 |_____/ \___/ \__,_|_| |_|\__,_|\_____|_|   \__, | .__/ \__|
                                              __/ | |
                                             |___/|_|
v1.0
\033[93mEasily hide your text message in wave audio file.\033[0m''')

def ex_msg(af):
    if not arged:
      help()
    else:
        print ("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print("Your Secret Message is: \033[1;91m"+msg+"\033[0m")
        waveaudio.close()
cls()
banner()
try:
  ex_msg(af)
except:
  print ("Something went wrong!! try again")
  quit('')