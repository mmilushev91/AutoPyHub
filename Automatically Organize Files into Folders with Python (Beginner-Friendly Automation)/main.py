import os
import shutil

#create folder path
folder_path = "./Files"

#create list of file names
files = os.listdir(folder_path)

#loop through files
for file in files:
    #split file name into name and extension
    name, extension = os.path.splitext(file)

    #create file type folder
    extension_folder = extension.replace(".", "").upper()

    #create new folder path
    new_folder = os.path.join(folder_path, extension_folder)

    #create new type folder if not exits
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(new_folder, file)

    shutil.move(old_path, new_path)
