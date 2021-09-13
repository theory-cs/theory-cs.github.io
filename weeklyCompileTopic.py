# This program creates dictionary that matches
# topics to weeks in which they are discussed and then
# produces .tex files for each topic
# with snippets ordered chronologically by weeks
#
# Input: outcomes.json specifies all topics

from string import Template
import os
import linecache

import json
outcomes = json.loads(open("outcomes.json").read())

# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())

# Credit: Professor Politz code from outcomes-list.py
low_levels = []
for (k, v) in outcomes.items():
  for (k2, v2) in v["Children"].items():
    for k3 in v2["Children"].keys():
      low_levels.append(k3.replace(" ", "-").lower()) 

#TODO : remove todooutcome as a key (should be here until all todooutcomes are removed though)
low_levels.append("todooutcome")

#debug: shows outcomes as filenames
#for outcome in low_levels: print(outcome)

# Create a dictionary
lowLevelsDict = {}
for line in low_levels:
    # Each dictionary has the low_levels as key and empty array as value
    lowLevelsDict[line] = []

# A function that returns the week of the snippet (key for later sort)
def findWeek(element):
    return int(element[1])

#if file in lessons directory is not found within a week on the website/unit-settings.json, then it will have 99 as a week number, 
#so that it is sorted to the end of compiled .tex files 
weekNumber = 99

weeklyDirectory = "notes/lessons"
for filename in os.listdir(weeklyDirectory):
    #debug:
    # print(filename)
    weekly = open (weeklyDirectory+"/"+filename, "r")

   #remove .tex extension from filename
    editFilename= filename.replace(".tex","")
    #print("editFilename: "+editFilename)

    #get week number/order from unit-settings.json file, this will be the order in which files appear on the website
    for element in unitData:
        for pdf in element['pdfs']:
            if( editFilename in pdf['file']):
                

                weekNumber= unitData.index(element)+1

                #debug
                #print(pdf['file'])
                #print(" index: "+str(unitData.index(element)+1))
    
    
    #debug
    #print(filename+" "+str(weekNumber))
    

    Lines = weekly.readlines()

    for line in Lines: 
        if (line.startswith("\input{../")) and not ("lesson-head.tex" in line):

            snippetsFile= line.replace("\input{../activity-snippets/", "").replace("}","").replace("\n", "")
            
            #debug
            #print(snippetsFile)

            # Get the second line of each file and clean the string
            snippetsDirectory= "notes/activity-snippets/"
            particularLine = linecache.getline(snippetsDirectory+snippetsFile, 2).replace("%! outcome:", "").replace("\n", "").strip()
            
            #debug
            #print(particularLine)
    

            # Split small outcomes with the delimiter ", " into a list
            li = list(particularLine.split(", "))
            for element in li:
                # lowercase them and replace whitespace with dashes (to make them uniform)
                test = element.replace(" ", "-").lower()
                
                #debug
                #print(test)

                #if application in snippet is empty or is none, do not add it to dictionary
                if(not test or "none" in test):
                    continue

                snippetWeek = [snippetsFile, weekNumber]
                
                #debug
                #print(snippetWeek)
                
                # add that tex filename to the dictionary
                lowLevelsDict[test].append(snippetWeek)

                #sort each outcome by week
                lowLevelsDict[test].sort(key=findWeek)

#debug: UNCOMMENT if want to see how the dictionary looks
#print(lowLevelsDict)

def write_if_different(filename, contents):
    try:
        old_contents = open(filename).read()
        if old_contents == contents: return
    except FileNotFoundError:
        pass # If the file doesn't exist, continue so we can create it!
    result_file = open(filename, "w")
    result_file.write(contents)
    result_file.close()


#Iterate through the dict
for key in lowLevelsDict:
    # Only run if the key has elements
    if(len(lowLevelsDict[key]) > 0):
        # Create each tex file
        result = "\input{../../resources/lesson-head.tex}\n"

        for list in lowLevelsDict[key]:
            tex = list[0]
            
            result += "\section*{"+tex.replace("-"," ").replace(".tex","").capitalize()+"}\n"
            result += "\input{../activity-snippets/" + tex + "}\n"
            result += "\\vfill\n"

        result += "\end{document}"

        write_if_different("generated/notes/topic/"+ key + ".tex", result)