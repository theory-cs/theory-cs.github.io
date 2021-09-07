from string import Template
import os
import linecache

import json
apps = json.loads(open("appTemplate.json").read())


# Credit: Professor Politz code from outcomes-list.py
applications = []
for (k, v) in apps.items():
  for (k2, v2) in v["Children"].items():
      applications.append(k2.replace(" ", "-").lower())

#shows applications as filenames
#for app in applications: print(app)

# Create a dictionary
appsDict = {}
for line in applications:
    # Each dictionary has the low_levels as key and empty array as value
    appsDict[line] = []


# TO DO: CHANGE testDir TO activity-snippets
directory = "notes/testDir"
for filename in os.listdir(directory):
    #print(filename)

    # Get the second line of each file and clean the string
    particularLine = linecache.getline(directory + "/" + filename, 1).replace("%! app: ", "").replace("\n", "")
    #print(particularLine)
    

    # Split small outcomes with the delimiter ", " into a list
    li = list(particularLine.split(", "))
    for element in li:
        # lowercase them and replace whitespace with dashes (to make them uniform)
        test = element.replace(" ", "-").lower()
        #print(test)
        # add that tex filename to the dictionary
        appsDict[test].append(filename)

# UNCOMMENT if want to see how the dictionary looks
#print(appsDict)

# Iterate through the dict
for key in appsDict:
    # Only run if the key has elements
    if(len(appsDict[key]) > 0):
        # Create each tex file
        result = "\input{../../resources/lesson-head.tex}\n"

        for tex in appsDict[key]:
            # TO DO: CHANGE testDir TO activity-snippets
            result += "\section*{"+tex.replace("-"," ").replace(".tex","").capitalize()+"}\n"
            result += "\input{../testDir/" + tex + "}\n"
            result += "\\vfill\n"

        result += "\end{document}"

        resultFile = open("notes/lessons/"+ key + ".tex", "w")
        resultFile.write(result)

        resultFile.close()