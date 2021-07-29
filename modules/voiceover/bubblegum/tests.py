import pyaudio
import numpy as np
from utils import stretch, speedx, pitchshift

# http://people.csail.mit.edu/hubert/pyaudio/
# special thanks to http://zulko.github.io/blog/2014/03/29/soundstretching-and-pitch-shifting-in-python/

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# work with one huge chunk
CHUNK = 204800

audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("* recording")

def playAudio(audio, samplingRate, channels):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=samplingRate,
                    output=True)
    sound = (audio.astype(np.int16).tostring())
    stream.write(sound)

    stream.stop_stream()
    stream.close()
    p.terminate()
    return

data = stream.read(CHUNK)
data = np.fromstring(data, dtype=np.int16)

# make two times louder
data *= 2

print ("* done recording")

# stop recording
"""
stream.stop_stream()
stream.close()
audio.terminate()
"""

# tests

playAudio(data, RATE, CHANNELS)

# this is how the pitch should change, positive integers increase the frequency, negative integers decrease it.

pitched = pitchshift(data, -5)
playAudio(pitched, RATE, CHANNELS)

pitched = pitchshift(data, 5)
playAudio(pitched, RATE, CHANNELS)