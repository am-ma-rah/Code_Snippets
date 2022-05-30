import os

root = 'data/'    #path to the directory where we have to find emoty folders
empty_folders = []
folders = list(os.walk(root))[1:]
print(folders)

for folder in folders:
#     folder example: ('FOLDER/3', [], ['file'])
    if not folder[2]:
#         print(f'Empty folder found !')
        empty_folders.append(folder[0])
        os.rmdir(folder[0])   # Delete those folders that are empty
