import wave, struct

filename = "/Users/vuhoangthuyduong/Documents/music-genre-classification/data/genres_original/classical/classical.00000.wav"

wavefile = wave.open(filename, 'r')

length = wavefile.getnframes()
lr = []
for i in range(0, length):
    wavedata = wavefile.readframes(1)
    data = struct.unpack("<h", wavedata)
    print(int(data[0]))
    lr.append(int(data[0]))


