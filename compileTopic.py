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


lowLevelsDict = {}
for line in low_levels:
    lowLevelsDict[line] = []


# TO DO: CHANGE testDir TO activity-snippets
directory = "notes/testDir"
for filename in os.listdir(directory):
    
    particularLine = linecache.getline(directory + "/" + filename, 2).replace("%! small-outcomes: ", "").replace("\n", "")
    # print(particularLine)
    
    li = list(particularLine.split(", "))
    for element in li:
        test = element.replace(" ", "-").lower()
        lowLevelsDict[test].append(filename)


for line in lowLevelsDict:
    if(len(lowLevelsDict[line]) > 0):
        result = "\input{../../resources/lesson-head.tex}"

        result += "\n"

        for tex in lowLevelsDict[line]:
            # TO DO: CHANGE testDir TO activity-snippets
            result += "\input{../testDir/" + tex + "}"
            result += "\n"
            result += "\\vfill"
            result += "\n"

        result += "\end{document}"




        resultFile = open("notes/topic/"+ line + ".tex", "w")
        resultFile.write(result)

        resultFile.close()