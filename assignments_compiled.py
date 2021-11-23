
import os
from os import listdir
from os.path import isfile, join
import linecache
import collections

#path of assignments directory
assignmentsPath = "notes/assignments/"

#string with content of all assignments files
assnString = ""

hwDict= []

#open each file in the notes/assignments directory
for entry in os.scandir(assignmentsPath):
    if(".tex" in entry.name):
        file = open(entry, 'r').read()
        
        #DEBUG
        #print(entry.name)
        if(entry.name != "assignments-compiled.tex"):
            hwDict.append(entry.name)

        #sort hw (this will make it hw 1, hw2 ...)
        hwDict = sorted(hwDict)

        #print(hwName)
        
        
#DEBUG
#print(hwDict)
count = 1; #count of hws 

for filename in hwDict:
    #string manipulation on the filename to make the title for each HW name 
    #hwName = filename.replace("-"," ").replace(".tex","").replace("hw","hw ").title()
    
    #open hw file
    filepath = assignmentsPath+filename
    file = open(filepath).read()
   

    #remove the begin document from all hws after hw1 
    if(count != 1):
        file = file.replace("\\begin{document}","").replace("\\input{../../resources/assignment-head.tex}","")
        
    #replace all end documents, add hw file contents to compiled string
    assnString+= file.replace("\\end{document}", "")

    assnString += "\\newpage"

    count += 1

#end compiled PDF 
assnString += "\n\n\end{document}"

#open a tex file in notes/assignments directory and write compiled string to it
assnFile = open("notes/assignments/assignments-compiled.tex", "w").write(assnString)
