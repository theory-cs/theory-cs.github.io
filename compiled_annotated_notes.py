from string import Template
import json
from user_functions import *
import collections
from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache

files = "generated/notes/lessons"

# key is week and value is activity snippets

bigPDF = ""


weekFiles = []
for entry in os.scandir(files):
    if((".tex" in entry.name) and ("new-" not in entry.name)):
        file = open(entry, 'r').readlines()
        if (len(file) > 0) and ("Week" in entry.name):
            weekFiles.append(entry.name)
    
    weekFiles = sorted(weekFiles)
    
print(weekFiles)
# count = 1
# for thefiles in weekFiles:
#     filename = "generated/notes/lessons/" + thefiles
#     file = open("generated/notes/lessons/" + thefiles, 'r').read()
    
    
#     #remove the begin document from all files after the first
#     if(count != 1):
#         file = file.replace("\\begin{document}","").replace("\input{../../resources/lesson-head.tex}","").replace("\\documentclass[12pt, oneside]{article}","")
        
#     #replace all end documents, add hw file contents to compiled string
#     bigPDF+= file.replace("\\end{document}", "")

#     bigPDF += "\\newpage"

    
#     count +=1


# bigPDF += "\n\\end{document}"

# # print(bigPDF)

# write_if_different("notes/lessons/complete-week.tex", bigPDF)