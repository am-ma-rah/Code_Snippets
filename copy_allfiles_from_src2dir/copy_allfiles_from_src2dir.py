# importing required packages
from pathlib import Path
import shutil
 
# defining source and destination paths
src = 'source'
trg = 'destination'
 
files=os.listdir(src)
 
# iterating over all the files in the source directory
for fname in files:
     
    # copying the files to the destination directory
    shutil.copy2(os.path.join(src,fname), trg)