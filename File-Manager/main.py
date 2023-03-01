#import reuired modules
import os
import shutil

#input of the file path location
path = input("Enter your path for sorting: ")

#for the files in the directory
files = os.listdir(path)

for i in files:
    filename , extension = os.path.splitext(i)
    extension_1 = extension[1:] #slicing of the file extension i.e removing of the dot(.)
    folder_path = path +"\\"+extension_1

    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i) #move file from one to another path 
        print("succesfully moving to exisiting folder ") #print statment for understanding the process is done or not 
    else:
        #if the folder is not present then create folder and move files
        os.makedirs(folder_path) #for this makedirs function of os is used
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i)  #move file from one to another path 
        print("succesfully moving to the new folder ")  #print statment for understanding the process is done or not 