# This program creates dictionary that matches
# outcomes to weeks in which they are discussed and then
# produces .tex files for each outcome
# with snippets ordered chronologically by weeks
#
# Input: outcomes.json specifies all outcomes
# website-settings are global settings (ungrouped snippets)
# unit_settings.json helps find the order of the weeks each snippet appears in
#
#Output: compiled .tex files for each outcome with corresponding snippets

from string import Template
import os
import linecache
from user_functions import *

import json
from weekly_compile_app import UNGROUPED
outcomes = json.loads(open("outcomes.json").read())
settings = json.loads(open("website-settings.json").read())

# returns unit_settings JSON file as a dictionary
unitData = json.loads(open("unit_settings.json").read())

# Credit: Professor Politz code from outcomes-list.py
low_levels = []
for (k, v) in outcomes.items():
  for (k2, v2) in v["Children"].items():
    for k3 in v2["Children"].keys():
        # low_levels.append(k3.replace(" ", "-").lower()) 
        low_levels.append(k3.replace(" ", "-")) 

#TODO : remove todooutcome as a key (should be here until all todooutcomes are removed though)
low_levels.append("todooutcome")

#debug: shows outcomes as filenames
#for outcome in low_levels: print(outcome)

# Create a dictionary
lowLevelsDict = {}
for line in low_levels:
    # Each dictionary has the low_levels as key and empty array as value
    lowLevelsDict[line.lower()] = []

# A function that returns the week of the snippet (key for later sort)
def findWeek(element):
    return int(element[1])

#if file in lessons directory is not found within a week on the website/unit_settings.json, then it will have the
#UNGROUPED constant as a week number, so that it is sorted to the end of compiled .tex files 
#ensure that the ungrouped constant is uniqe and will not appear as a week  
UNGROUPED = 99
weekNumber = UNGROUPED

weeklyDirectory = "notes/lessons"
for filename in os.listdir(weeklyDirectory):
    #debug:
    # print(filename)
    weekly = open (weeklyDirectory+"/"+filename, "r")

   #remove .tex extension from filename
    editFilename= filename.replace(".tex","")
    #print("editFilename: "+editFilename)

    #get week number/order from unit_settings.json file, this will be the order in which files appear on the website
    for element in unitData:
        if('pdfs' in element):
            for pdf in element['pdfs']:
                if( editFilename in pdf['file']):
                

                    weekNumber= unitData.index(element)+1

                #debug
                #print(pdf['file'])
                #print(" index: "+str(unitData.index(element)+1))
    
    
    #debug
    #print(filename+" "+str(weekNumber))
    

    Lines = weekly.readlines()

    # for k in lowLevelsDict:
        # print(k + ": " + str(lowLevelsDict[k]) + "\n")

    for line in Lines: 
        if (line.startswith("\input{../")) and not ("lesson-head.tex" in line):

            snippetsFile= line.replace("\input{../activity-snippets/", "").replace("}","").replace("\n", "")
            
            #debug
            #print(snippetsFile)

            # Get the second line of each file and clean the string
            snippetsDirectory= "notes/activity-snippets/"


            # Get the line which %! app: is there (without hard coding)
            activitysnippet = open(snippetsDirectory+snippetsFile, "r")
            
            particularLine = ""

            for theline in activitysnippet:
                if("%! outcome:" in theline):
                    particularLine = theline.replace("%! outcome:", "").replace("\n", "").strip()
                    break

            # particularLine = linecache.getline(snippetsDirectory+snippetsFile, 2).replace("%! outcome:", "").replace("\n", "").strip()
            
            #debug
            # print(particularLine)
    

            # Split small outcomes with the delimiter ", " into a list
            li = list(particularLine.split(", "))
            for element in li:
                # print("element is: " + element + "\n")
                # lowercase them and replace whitespace with dashes (to make them uniform)
                test = element.replace(" ", "-").lower()

                #debug
                #print(test)

                #if application in snippet is empty or is none, do not add it to dictionary
                if(not test or "none" in test):
                    continue


                #if IncludeUngroupedSnippets is true, then include all snippets
                #(including ungrouped ones)
                if(settings['IncludeUngroupedSnippets']):
                    snippetWeek = [snippetsFile, weekNumber]

                    # add that tex filename to the dictionary
                    # print("test is: " + test)
                    lowLevelsDict[test].append(snippetWeek)

                    #debug
                    #print(snippetWeek)
            
                #if IncludeUngroupedSnippets is false, then only include those snippets who aren't 
                # ungrouped (these are set to the UNGROUPED constant value)
                elif (weekNumber != UNGROUPED):
                    snippetWeek = [snippetsFile, weekNumber]
                
                    # add that tex filename to the dictionary
                    lowLevelsDict[test].append(snippetWeek)

                    #debug
                    #print(snippetWeek)
                
                #sort each outcome by week
                lowLevelsDict[test].sort(key=findWeek)

#debug: UNCOMMENT if want to see how the dictionary looks
# print(lowLevelsDict)

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

        write_if_different("generated/notes/outcome/"+ key + ".tex", result)
