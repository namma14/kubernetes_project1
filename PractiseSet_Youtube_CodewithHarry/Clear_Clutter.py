#writing a prog to clear a folder
import os
import shutil

def creatfolderifnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder) #makedirs() is used to create folders

def move(foldername,files):
    for dt in files:
        os.replace(f"Library_Project/{dt}", f"Library_Project/Newfolder/{foldername}/{dt}")

file = os.listdir('Library_Project') # to dislpay all folder available in python folder
print("The content in file is ",file)

creatfolderifnotexist('Library_Project/Newfolder/Images')
creatfolderifnotexist('Library_Project/Newfolder/Docs')
creatfolderifnotexist('Library_Project/Newfolder/Music')

imgext = ['.png','.jpg','.jpeg']
imageextn = [ext for ext in file if os.path.splitext(ext)[1].lower() in imgext]
# print(imageextn)
docext = ['.pdf','.txt','.py','.pyc']
docextn = [ext for ext in file if os.path.splitext(ext)[1].lower() in docext]
# print(docextn)

musicext = ['.mp4','.mp3']
musicextn = [ext for ext in file if os.path.splitext(ext)[1].lower() in musicext]
# print(musicextn)

# for dt in musicextn:
    # os.replace(f"Library_Project/{dt}", f"Library_Project/Newfolder/Music/{dt}")

move("Images",imageextn)
move("Docs",docextn)
move("Music",musicextn)
   
