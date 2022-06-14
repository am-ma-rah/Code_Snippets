import os

tar_dir = r'\data' 
file_names = os.listdir(tar_dir)
for file_name in file_names:
    with open('filenames_list.txt', 'a') as f:
        f.write(file_name+"\n")
