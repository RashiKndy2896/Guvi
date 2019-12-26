import os

target_folder = r'C:\Users\rashi\Documents\movefiles\dest'+'\\'
src_folder = r'C:\Users\rashi\Documents\movefiles\src'+'\\'

def move_files(sourcefolder,targetfolder):
    for path,dir, files in os.walk(sourcefolder):
        if files:
           for file in files:
               if not os.path.isfile(targetfolder + file):
                    os.rename(path + '\\' + file, targetfolder + file)
    print("all files moved")

move_files(src_folder,target_folder)   

  
