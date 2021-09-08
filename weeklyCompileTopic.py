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


# Create a dictionary
lowLevelsDict = {}
for line in low_levels:
    # Each dictionary has the low_levels as key and empty array as value
    lowLevelsDict[line] = []

# A function that returns the week of the snippet (key for later sort)
def findWeek(element):
    return int(element[1])

# TO DO: CHANGE testWeek TO lessons
weeklyDirectory = "notes/testWeek"
for filename in os.listdir(weeklyDirectory):
    #print(filename)
    weekly = open (weeklyDirectory+"/"+filename, "r")

    #get week number/order from week notes file
    weekNumber = linecache.getline(weeklyDirectory+"/"+filename, 1).replace("%", "").replace("\n", "")
    

    Lines = weekly.readlines()

    for line in Lines: 
        if (line.startswith("\input{../")) and not ("lesson-head.tex" in line):
            #TODO change testDir to activity-snippets
            snippetsFile= line.replace("\input{../testDir/", "").replace("}","").replace("\n", "")
            #print(snippetsFile)

            # Get the second line of each file and clean the string
            snippetsDirectory= "notes/testDir/"
            particularLine = linecache.getline(snippetsDirectory+snippetsFile, 2).replace("%! outcome: ", "").replace("\n", "")
            #print(particularLine)
    

            # Split small outcomes with the delimiter ", " into a list
            li = list(particularLine.split(", "))
            for element in li:
                # lowercase them and replace whitespace with dashes (to make them uniform)
                test = element.replace(" ", "-").lower()
                #print(test)
                snippetWeek = [snippetsFile, weekNumber]
                # add that tex filename to the dictionary
                lowLevelsDict[test].append(snippetWeek)

                #sort each outcome by week
                lowLevelsDict[test].sort(key=findWeek)
# UNCOMMENT if want to see how the dictionary looks
print(lowLevelsDict)


#Iterate through the dict
for key in lowLevelsDict:
    # Only run if the key has elements
    if(len(lowLevelsDict[key]) > 0):
        # Create each tex file
        result = "\input{../../resources/lesson-head.tex}\n"

        for list in lowLevelsDict[key]:
            tex = list[0]
            # TO DO: CHANGE testDir TO activity-snippets
            result += "\section*{"+tex.replace("-"," ").replace(".tex","").capitalize()+"}\n"
            result += "\input{../testDir/" + tex + "}\n"
            result += "\\vfill\n"

        result += "\end{document}"

        resultFile = open("generated/notes/app/"+ key + ".tex", "w")
        resultFile.write(result)

        resultFile.close()