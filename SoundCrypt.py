import os
import wave
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
parser.add_argument('-m', help='message', dest='message')
parser.add_argument('-o', help='outputfile', dest='outputfile')
args = parser.parse_args()

af = args.audiofile
msg = args.message
output_file = args.outputfile

arged = False

if af and msg and output_file:
    arged = True

def cls():
    os.system("clear")

def help():
    print("Extract Your Secret Message from Audio Wave File.")
    print ('''usage: Encrypt.py [-h] -f AUDIOFILE -m SECRETMSG -o OUTPUTFILE

optional arguments:
  -h, --help       show this help message and exit
  -f AUDIOFILE     Select Audio File
  -m SECRETMSG     Enter your message
  -o OUTPUTFILE    Your output file path and name''')

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
Easily hide your text message in a wave audio file.''')

def ex_msg(af, msg, output_file):
    if not arged:
        help()
    else:
        print ("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        # Hide the message in the audio
        msg += "###"
        binary_msg = ''.join(format(ord(char), '08b') for char in msg)
        data_index = 0

        for i in range(len(frame_bytes)):
            if data_index < len(binary_msg):
                frame_bytes[i] = int(format(frame_bytes[i], '08b')[:-1] + binary_msg[data_index], 2)
                data_index += 1
            if data_index == len(binary_msg):
                break

        # Write the modified frame bytes to the output file
        with wave.open(output_file, 'wb') as output_wave:
            output_wave.setparams(waveaudio.getparams())
            output_wave.writeframes(bytes(frame_bytes))

        print("Message successfully hidden in the audio file.")
        waveaudio.close()

cls()
banner()
try:
    ex_msg(af, msg, output_file)
except Exception as e:
    print ("Something went wrong!! Try again.")
    print(str(e))
