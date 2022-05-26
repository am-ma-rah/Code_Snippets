import shutil
import os
import glob

#path of a directory where the files are stored
src_dir = r'./data/src_dir'

#path of a directory from where we have to check if any file exists that matches files in src_dir
match_dir = r'./data/match_dir'

#path of a directory where we need to store the matched files(find files in src_dirc, matches with match_dir and store in tar_dir)
tar_dir = r'./data/tar_dir'

src_files = []
match_files = []
tar_list = []

for path,subdirs,files in os.walk(src_dir):
    for f in files:
        file_name = os.path.join(path,f)
        #Note: you can change it as per your file name requirement!
        fn = file_name.split('\\')[-1]
        src_files.append(fn)
#     print(f'Files:{len(src_files)}')
# print(src_files)

for path,subdirs,files in os.walk(match_dir):
    for f in files:
        file_name = os.path.join(path,f)
        match_files.append(file_name)
#     print(f'Files:{len(match_files)}')

for element in match_files:
    element_split = element.split('\\')[-1]
#     print(element_split)
    if element_split in src_files:
        print(f'Matched File name is: {element_split}')
#         print(f'This File match: File path is {element}')
        shutil.copyfile(element, tar_dir+"\\"+element_split.split("\\")[-1])
#         print("File transfered!")
        tar_list.append(element)
# print(f'Total File matches(remember it includes folders too): {len(tar_list)}')
