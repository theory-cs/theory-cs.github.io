from userFunctions import *
from zipfile import ZipFile
import re
from os.path import basename

#function which creates zip file with all images and tex file 
def zip_file(filename):
    path= "generated/notes/lessons-flat/"+filename+".tex"
    texFile = open(path, "r+")
    zipObj = ZipFile("generated/notes/lessons-flat/"+filename+".zip", 'w')
    zipObj.write("generated/notes/lessons-flat/Week2.tex")


    #image list 
    imageList = [] 
   

    #DEBUG
    print(filename)
    print(imageList)

  

zip_file("Week2")