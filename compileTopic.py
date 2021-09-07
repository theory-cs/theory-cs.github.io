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


# TO DO: CHANGE testDir TO activity-snippets
directory = "notes/testDir"
for filename in os.listdir(directory):
    

    # Get the second line of each file and clean the string
    particularLine = linecache.getline(directory + "/" + filename, 2).replace("%! small-outcomes: ", "").replace("\n", "")
    # print(particularLine)
    

    # Split small outcomes with the delimiter ", " into a list
    li = list(particularLine.split(", "))
    for element in li:
        # lowercase them and replace whitespace with dashes (to make them uniform)
        test = element.replace(" ", "-").lower()
        # add that tex filename to the dictionary
        lowLevelsDict[test].append(filename)

# UNCOMMENT if want to see how the dictionary looks
# print(lowLevelsDict)


# Iterate through the dict
for key in lowLevelsDict:
    # Only run if the key has elements
    if(len(lowLevelsDict[key]) > 0):
        # Create each tex file
        result = "\input{../../resources/lesson-head.tex}"

        result += "\n"

        for tex in lowLevelsDict[key]:
            # TO DO: CHANGE testDir TO activity-snippets
            result += "\section*{"+tex.replace("-"," ").replace(".tex","").capitalize()+"}\n"
            result += "\input{../testDir/" + tex + "}"
            result += "\n"
            result += "\\vfill"
            result += "\n"

        result += "\end{document}"

        resultFile = open("notes/topic/"+ key + ".tex", "w")
        resultFile.write(result)

        resultFile.close()