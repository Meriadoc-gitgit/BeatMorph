import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import os
import argparse
from preprocess import extract_features  # Ensure extract_features is correctly implemented

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract data from wav files')
    parser.add_argument('--data_path', type=str, help='Input directory')
    parser.add_argument('--output_dir', type=str, help='Output directory')
    args = parser.parse_args()

    data_path = args.data_path
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, _ in os.walk(data_path):
        for d in dirs:
            genre_dir = os.path.join(output_dir, d)  # Ensure genre subdirectory exists
            os.makedirs(genre_dir, exist_ok=True)

            path = os.path.join(root, d)
            for _, _, files in os.walk(path):
                for file in files:
                    if file.endswith('.wav'):
                        filename = os.path.join(path, file)
                        print(f"Extracting features from {filename}")
                        
                        # Extract features
                        features = extract_features(filename)
                        if features is None or not isinstance(features, (list, np.ndarray)):
                            print(f"Skipping {filename}: Invalid features extracted")
                            continue
                        
                        features = np.array(features)

                        # Plot features
                        plt.figure(figsize=(10, 4))
                        plt.plot(features)
                        plt.title(f"Features for {file}")
                        plt.xlabel("Feature Index")
                        plt.ylabel("Value")

                        # Construct output file path
                        out_file = os.path.join(genre_dir, f"{os.path.splitext(file)[0]}.png")

                        print(f"Saving plot to {out_file}")
                        plt.savefig(out_file)
                        plt.close()  # Close the plot to free memory
