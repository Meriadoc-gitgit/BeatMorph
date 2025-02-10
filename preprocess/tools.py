import pandas as pd 

import wave, struct
import os 


def extract_features(filename):
    wavefile = wave.open(filename, 'r')
    length = wavefile.getnframes()
    lr = []
    for i in range(0, length):
        wavedata = wavefile.readframes(1)
        data = struct.unpack("<h", wavedata)
        lr.append(int(data[0]))

    return lr