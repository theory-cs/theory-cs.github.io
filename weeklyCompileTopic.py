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


weeklyDirectory = "notes/lessons"
for filename in os.listdir(weeklyDirectory):
    #print(filename)
    weekly = open (weeklyDirectory+"/"+filename, "r")

    #get week number/order from weekly notes file- this will be the number right before .tex(length-4)
    #convention: #.tex -> must be at the end of every lessons/ file
    weekNumber = filename[len(filename)-5]
    
    #debug
    #print(filename+" "+weekNumber)
    

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
# UNCOMMENT if want to see how the dictionary looks
#print(lowLevelsDict)

def write_if_different(filename, contents):
    old_contents = open(filename).read()
    if old_contents == contents: return
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

        write_if_different("generated/notes/app/"+ key + ".tex", result)