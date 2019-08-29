import os
import shutil

# folder with the images. replace the directory with your own
downloads = '/Users/ahmedyusuf/Downloads/'

# destination folder for the images
destination = f'{downloads}images/'
#print(destination)

# iterate over the files in the folder
for f in os.listdir(downloads):
    #print(f)
    
    # only if the file is jpg or png
    if f.endswith('.jpg') or f.endswith('.png'):
        print(f)
        shutil.move(downloads + f, destination) # move the images to the destination folder
    else:
        print('no image files')
        break
