#import os builtin module
import os

#new names list
new_names = ["text1.txt", "text2.txt", "text3.txt", "text4.txt", "text5.txt"]
new_names_len = len(new_names)

#assign directory
folder_path = "./Files"

#create a list of files in the folder
files_list = os.listdir(folder_path)
files_list_len = len(files_list)

#loop through files list
for idx in range(files_list_len):

    #check if idx is equal to new names list length and if so raise an exception
    if idx == new_names_len:
        raise Exception("No new name available for file")

    #current file name
    file_name = files_list[idx]

    #new file name
    new_name = new_names[idx]

    #create old and new file paths
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, new_name)

    #rename file
    os.rename(old_path, new_path)
