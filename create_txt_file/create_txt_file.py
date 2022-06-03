
import os
tar_dir = r'data_folder/class0'

file_paths = [x[0] for x in os.walk(tar_dir)]
for f in file_paths[1:]: #[1:] will help us to get rid of 1st item in list which is a folder path
    file_name = f.split('\\')[-1]  #split according to your required filename
    label=f.split('\\')[-2]   #split according to your required label
    if label=='class0':  #check 'if else' condition according to your requirement
        label = '0'
    else:
        label= '1'
    line = "train/{}.wav {}".format(file_name,label) #set output according to what you want to write in txt file
#     print(line)

    with open('labels_file.txt', 'a') as f: #labels.txt is the name of .txt file we are creating
        f.write(line)
        f.write('\n')
