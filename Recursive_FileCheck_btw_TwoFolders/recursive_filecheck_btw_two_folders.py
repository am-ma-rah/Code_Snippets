import os
if __name__ == '__main__':   
    current_dir1 = ""
    path_list1 = []
    for path, subdirs, files in os.walk(current_dir1):
        for f in files:
            p = os.path.join(path, f)
            #print(p)
            p = p.split(".")[0].split("\\")[-1]
#             print(p)
            path_list1.append(p)
    print(f'Total Files in First Directory: {len(path_list1)}')
    
    current_dir2 = ""
    path_list2 = []
    for path, subdirs, files in os.walk(current_dir2):
        for f in files:
            p = os.path.join(path, f)
            p = p.split(".")[0].split("\\")[-1]
#             print(p)
            path_list2.append(p)
    print(f'Total Files in Second Directory: {len(path_list2)}')
    
    #Change accordingly
    for i in path_list1:
        if i not in path_list2:
            print(i)
#             #os.remove(i) #uncomment if you want to delete extra/not matching file

