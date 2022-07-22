from string import Template
import os
import linecache
from user_functions import *

#TODO: use header file ... 
with open('resources/lesson-head.tex') as f:
    lines = f.readlines()

with open('resources/discrete-math-packages.tex') as f:
    package = f.read()

for line in lines:
    if("\input" in line):
        idx = lines.index(line)
        lines.pop(idx)
        lines.insert(idx, package)

opening = ""
for line in lines:
    opening += line

bigPDF = opening


directoryFolder = "notes/activity-snippets"

definition_array = []
for filename in os.listdir(directoryFolder):
    # print(filename)
    if("definition" in filename):
        # print(filename)
        definition_array.append(filename)

definition_array = sorted(definition_array)

websiteData = json.loads(open("website-settings.json").read())

full_definition = websiteData['Compiled Activity Snippets']

if(full_definition == "True"):
    for filename in definition_array:
        weekly = open (directoryFolder+"/"+filename, "r")
            
        lines = weekly.readlines()

        strNew = ""
        for line in reversed(lines):
            if(line.startswith("%!") or line.startswith("\n")):
                lines.remove(line)
            
        strNew += opening

        for line in lines:
            strNew += line
            bigPDF += line

        bigPDF += "\n"

        strNew += "\n\end{document}"
        # print(strNew)
        
        write_if_different("generated/notes/activity-snippets-flat/" + filename, strNew)

    bigPDF += "\n\end{document}"
    write_if_different("generated/notes/activity-snippets-flat/full-definition.tex", bigPDF)