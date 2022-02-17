import os

def get_files_folders_paths(path):
    allFoldersPath = list()
    allFilesPath = list()
    for root,dirs,files in os.walk(path):
        for d in dirs:
            #print(d)
            allFoldersPath.append((os.path.join(root,d)))
        for name in files:
            #print(name)
            allFilesPath.append(os.path.join(root,name))
    return allFoldersPath , allFilesPath

path = ''              #Enter the directory path to raed files and folders from
listOfPaths = get_files_folders_paths(path)
listOfPaths
# listOfPaths[0]
# listOfPaths[1]

