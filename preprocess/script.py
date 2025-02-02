import pandas as pd 

import wave, struct
import os 


def create_dataset(filepath, filetype):
    """
    filepath -> insert link to the `data` directory
    """
    data = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.endswith(filetype):
                data.append([os.path.join(root, file), root.split('/')[-1]])
                print(f'Extracting {file} from {root.split("/")[-1]}')
    df = pd.DataFrame(data, columns=['filename', 'label'])
    return df


def extract_features(filename):
    wavefile = wave.open(filename, 'r')
    length = wavefile.getnframes()
    lr = []
    for i in range(0, length):
        wavedata = wavefile.readframes(1)
        data = struct.unpack("<h", wavedata)
        lr.append(int(data[0]))
    return lr


if __name__ == '__main__':
    filepath = '/Users/vuhoangthuyduong/Documents/music-genre-classification/data'
    df = create_dataset(filepath, '.wav')
    df['features'] = df['filename'].apply(extract_features)
    df.to_csv('dataset.csv', index=False)