
import os
from moviepy.editor import *
from pathlib import Path
if __name__ == '__main__':
    dir_path = r""              # Path of videos to extract the audios from.
    target_path = r""           # Path of target directory where extracted audios will be stored.
    count = 0
    for path, subfol, files in os.walk(dir_path):
        c = 0
        for file in files:
            v_file = os.path.join(path,file)
            a_file_name = file.split(".")[0] + '.wav'
            save_path = os.path.join(target_path, a_file_name)
            exists = os.path.isfile(save_path)
            if exists:
                c = c+1
                print(c)
                pass
            else:
                try:
                    audio_clip = VideoFileClip(v_file,verbose=False)
                    audio_clip.audio.write_audiofile(save_path,verbose=False)
                    count+=1
                    print(count)
                except (IndexError,OSError,KeyError,AttributeError):
                    print('here',v_file)
                    os.remove(v_file)
                    temp = v_file.replace('train','train_audio').replace('.mp4', '.wav')
                    if os.path.exists(temp):
                        os.remove(temp)
                    else:
                        print("The audio does not exist")

