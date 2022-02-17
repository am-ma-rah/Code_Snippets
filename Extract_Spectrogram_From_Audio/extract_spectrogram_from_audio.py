
import numpy as np
import pandas as pd 
import os 
import glob
import soundfile as sf
import scipy.io.wavfile
import scipy.signal as signal
import matplotlib.pyplot as plt
import pathlib
import shutil
import random
import librosa

dir_path = r""      # Path of a directory to load audio files in order to extract spectrograms
target_dir = r""    # Path of a directory where we have to store the spectrograms extracted from audio 

pathlib.Path(f'{target_dir}').mkdir(parents=True, exist_ok=True)
c = 0
for filename in os.listdir(f'{dir_path}'):
#     print(filename)
    audio_path = f'{dir_path}/{filename}'
    print(audio_path)
    a_file_name = filename.split(".")[0] + '.png' 
#     print(a_file_name)
    save_path = f'{target_dir}/{a_file_name}'
#     print(save_path)
    exists = os.path.isfile(save_path)
#     print(exists)
    if exists:
        c = c+1
        print(c)
        pass
    else:
        try:
            y, sr = librosa.load(audio_path, mono=True)
            plt.specgram(y,Fs=sr);
            plt.axis('off');
            plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0);
            plt.savefig(f'{save_path}')
            plt.clf()
        except(RuntimeError):
            print(here)
        

