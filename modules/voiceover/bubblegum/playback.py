import pyaudio
import numpy as np
from utils import stretch, speedx, pitchshift

p = pyaudio.PyAudio()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

def callback(in_data, frame_count, time_info, flag):
    # using Numpy to convert to array for processing
    # audio_data = np.fromstring(in_data, dtype=np.float32)
    return in_data, pyaudio.paContinue

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                input=True,
                stream_callback=callback)


stream.start_stream()

while stream.is_active():
    data = stream.read(CHUNK)
    data = np.fromstring(data, dtype=np.int16)
    data *= 2
    pitched = pitchshift(data, -5)
    sound = (pitched.astype(np.int16).tostring())
    stream.write(sound)
    # time.sleep(600) # play the stream for 10 minutes
    # stream.stop_stream()
    # print("Stream is stopped")

stream.close()
p.terminate()