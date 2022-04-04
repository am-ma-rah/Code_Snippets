# importing required packages
from pathlib import Path
import shutil
import os

# We have 3 folders -->  folder1 = contain some files from source directory  , folder2 = source directory , folder3 = destination directory
fileslist = 'E:\Frameworks\deepfake\df_data\Train\Fake_jpg'
files_list = os.listdir(fileslist)

# defining source and destination
src = ''
trg = ''

match_files = []
for path, subdir, files in os.walk(src):
    for f in files:
        v = f.split('.')[0]
#         print(v)
        if v in files_list:
            v = v + ".mp4"
            vid_file = os.path.join(path, v)
            match_files.append(vid_file)
            #print(vid_file)

#   copying the files to the destination directory
for vid_file in match_files:
    shutil.copyfile(vid_file, trg+"\\"+vid_file.split("\\")[-1])
    print("Done")