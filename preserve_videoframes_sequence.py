
import os
from natsort import natsorted    #used to preserve the frame sequence 
import glob
from PIL import Image

def get_vids(path2vids):
    listOfCats = os.listdir(path2vids)
    vidpaths = []
    for catg in listOfCats:
        path2catg = os.path.join(path2vids, catg)
        listOfSubCats = os.listdir(path2catg)
        path2subCats= [os.path.join(path2catg,los) for los in listOfSubCats]
        vidpaths.extend(path2subCats)
    return vidpaths, listOfCats 

path2vids = r""

vidpaths, listOfCats  = get_vids(path2vids) 
print(f'Total Videos = {len(vidpaths)}\nCategories = {len(listOfCats)}\nCategory Names = {listOfCats}')

print('_'*40)


cat_dict = {}
ind = 0
for l in listOfCats:
    cat_dict[l] = ind
    ind += 1
print(f'Labels Dict :{cat_dict}')


#To preserve the frame sequence we use !pip install natsort
timesteps = 16      #to select specific frames
c = 0
for path in vidpaths:
    c = c+1
    path2imgs = glob.glob(path +"/*.jpg")
    path2imgs = natsorted(path2imgs)
    print(path2imgs[:])
    path2imgs = path2imgs[:timesteps]
    
    frames = []
    for p2i in path2imgs:
        frame = Image.open(p2i)
        frames.append(frame)
#     print(f'No. of frames in Video {c} = {len(frames)}')
#     print(frames)
