from userFunctions import *
from zipfile import ZipFile
import re
from os.path import basename

#function which creates zip file with all images and tex file 
def zip_file(filename, view): 
    path = ""; newPath=  ""; texFile=""; zipObj= ""; newTexFile = "";
    if(view == "chronological"):
        path= "generated/notes/lessons-flat/"+filename+".tex"
        newPath= "generated/notes/lessons-flat/new-"+filename+".tex"
        zipObj = ZipFile("generated/notes/lessons-flat/"+filename+".zip", 'w')
        newTexFile = open(newPath, "w")
    elif(view == "outcome"):
        path= "generated/notes/topic-flat/"+filename+".tex"
        newPath= "generated/notes/topic-flat/new-"+filename+".tex"
        zipObj = ZipFile("generated/notes/topic-flat/"+filename+".zip", 'w')
        newTexFile = open(newPath, "w")
    elif(view == "application"):
        path= "generated/notes/app-flat/"+filename+".tex"
        newPath= "generated/notes/app-flat/new-"+filename+".tex"
        zipObj = ZipFile("generated/notes/app-flat/"+filename+".zip", 'w')
        newTexFile = open(newPath, "w")
    elif(view == "assignments"):
        path= "generated/notes/assignments-flat/"+filename+".tex"
        newPath= "generated/notes/assignments-flat/new-"+filename+".tex"
        zipObj = ZipFile("generated/notes/assignments-flat/"+filename+".zip", 'w')
        newTexFile = open(newPath, "w")

    try: 
            texFile = open(path, "r+")
    except IOError as e:
            print(e)
            return

    #image list 
    imageList = [] 

    texString = texFile.readlines()
    
    newTexString = ""
    
    newTexFile.write(newTexString)

    for line in texString:
        if ("\includegraphics" in line):
            replaced = line.replace("../","").replace("resources/images/","")
            #DEBUG
            #print(replaced)
            newTexString += replaced 
        else : 
            newTexString += line
        
        if ("\includegraphics" in line):
            imageFile = re.findall(r'\{.*?\}', line)
            for element in imageFile :
                if "/images" in element:
                    element = element.replace("{","").replace("}","").replace("../","")
                    imageList.append(element) 

    newTexFile.write(newTexString)
    imageList = list(set(imageList))

    #DEBUG
    #nlines=texString.count('\n')
    #print(nlines)
    #print(filename)
    #print(imageList)

    if(len(imageList)!=0):
        zipObj.write(newPath,basename(newPath))
        for element in imageList:
            zipObj.write(element, basename(element)) 
        
        
        if(view == "chronological"):
            return "../notes/lessons-flat/"+filename+".zip"
        elif(view == "outcome"):
            return "../notes/topic-flat/"+filename+".zip"
        elif(view == "application"):
            return "../notes/app-flat/"+filename+".zip"
        elif(view == "assignments"):
            return "../notes/assignments-flat/"+filename+".zip"
    else: 
        if(view == "chronological"):
            return "../notes/lessons-flat/"+filename+".tex"
        elif(view == "outcome"):
            return "../notes/topic-flat/"+filename+".tex"
        elif(view == "application"):
            return "../notes/app-flat/"+filename+".tex"
        elif(view == "assignments"):
            return "../notes/assignments-flat/"+filename+".tex"
