# This program creates dictionary that matches
# applications to weeks in which they are discussed and then
# produces .tex files for each application
# with snippets ordered chronologically by weeks
#
# Input: applications.json specifies all applications

from string import Template
import os
import linecache

import json
apps = json.loads(open("applications.json").read())


# Credit: Professor Politz code from outcomes-list.py
applications = []
for (k, v) in apps.items():
  for (k2, v2) in v["Children"].items():
      applications.append(k2.replace(" ", "-").lower())
# For debugging: shows applications as filenames
#for app in applications: print(app)

#TODO : remove todoapp as a key (should be here until all todoapps are removed though)
applications.append("todoapp")

# Create a dictionary with applications as key, each have 
# value an array of pairs (snippet filename, week it appears)
appsDict = {}
for app in applications:
    # Initialize the value of each item in the dictionary to be empty array
    appsDict[app] = []

# A function that returns the week of the snippet (key for later sort)
def findWeek(element):
    return int(element[1])


weeklyDirectory = "notes/lessons"
for filename in os.listdir(weeklyDirectory):
    #print(filename)
    weekly = open (weeklyDirectory+"/"+filename, "r")

    #get week number/order from weekly notes file- this will be the number right before .tex(length-4)
    weekNumber = filename[len(filename)-5]
    print(filename+" "+weekNumber)
    

    Lines = weekly.readlines()

    for line in Lines: 
        if (line.startswith("\input{../")) and not ("lesson-head.tex" in line):
            
            snippetsFile= line.replace("\input{../activity-snippets/", "").replace("}","").replace("\n", "")
            #print(snippetsFile)

            # Get the second line of each file and clean the string
            
            snippetsDirectory= "notes/activity-snippets/"
            particularLine = linecache.getline(snippetsDirectory+snippetsFile, 1).replace("%! app:", "").replace("\n", "").strip()
            #print(particularLine)
    

            # Split small outcomes with the delimiter ", " into a list
            li = list(particularLine.split(", "))
            for element in li:
                # lowercase them and replace whitespace with dashes (to make them uniform)
                test = element.replace(" ", "-").lower()
                #print(test)

                #if application in snippet is empty or is none, do not add it to dictionary
                if(not test or "none" in test):
                    continue

                snippetWeek = [snippetsFile, weekNumber]
                #print(snippetWeek)
                # add that tex filename to the dictionary
                appsDict[test].append(snippetWeek)

                #sort each outcome by week
                appsDict[test].sort(key=findWeek)
# UNCOMMENT if want to see how the dictionary looks
print(appsDict)


#Iterate through the dict
for key in appsDict:
    # Only run if the key has elements
    if(len(appsDict[key]) > 0):
        # Create each tex file
        result = "\input{../../resources/lesson-head.tex}\n"

        for list in appsDict[key]:
            tex = list[0]
            
            result += "\section*{"+tex.replace("-"," ").replace(".tex","").capitalize()+"}\n"
            result += "\input{../activity-snippets/" + tex + "}\n"
            result += "\\vfill\n"

        result += "\end{document}"

        resultFile = open("generated/notes/app/"+ key + ".tex", "w")
        resultFile.write(result)

        resultFile.close()