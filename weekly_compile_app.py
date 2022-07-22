# This program creates dictionary that matches
# applications to weeks in which they are discussed and then
# produces .tex files for each application
# with snippets ordered chronologically by weeks
#
# Input: applications.json specifies all applications
# website-settings are global settings (ungrouped snippets)
# unit_settings.json helps find the order of the weeks each snippet appears in
#
# Output: compiled .tex files for each Application with corresponding snippets

from string import Template
import os
import linecache
from user_functions import *

import json
apps = json.loads(open("applications.json").read())
settings = json.loads(open("website-settings.json").read())

# returns unit_settings JSON file as a dictionary
unitData = json.loads(open("unit_settings.json").read())


# Credit: Professor Politz code from outcomes-list.py
applications = []
for (k, v) in apps.items():
    applications.append(k.replace(" ", "-").lower())
# debug: shows applications as filenames
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

#if file in lessons directory is not found within a week on the website/unit_settings.json, then it will have 99 as a week number, 
#so that it is sorted to the end of compiled .tex files 
UNGROUPED = 99
weekNumber = UNGROUPED

weeklyDirectory = "notes/lessons"
for filename in os.listdir(weeklyDirectory):
    # print(filename)
    weekly = open (weeklyDirectory+"/"+filename, "r")

    #remove .tex extension from filename
    editFilename= filename.replace(".tex","")
    # debug: print("editFilename: "+editFilename)

    #get week number/order from unit_settings.json file, this will be the order in which files appear on the website
    for element in unitData:
        if('pdfs' in element):
            for pdf in element['pdfs']:
                if( editFilename in pdf['file']):
                

                    weekNumber= unitData.index(element)+1

                #debug
                # print(pdf['file'])
                # print(" index: "+str(unitData.index(element)+1))
    
    
    #debug
    #print(filename+" "+str(weekNumber))
    

    lines = weekly.readlines()

    for line in lines: 
        if (line.startswith("\input{../")) and not ("lesson-head.tex" in line):
            
            snippetsFile= line.replace("\input{../activity-snippets/", "").replace("}","").replace("\n", "")
            
            #debug
            # print(snippetsFile)

            # Get the second line of each file and clean the string
            snippetsDirectory= "notes/activity-snippets/"


            # Get the line which %! app: is there (without hard coding)
            activitysnippet = open(snippetsDirectory+snippetsFile, "r")
            
            particularLine = ""

            for theline in activitysnippet:
                if("%! app:" in theline):
                    particularLine = theline.replace("%! app:", "").replace("\n", "").strip()
                    break



            # particularLine = linecache.getline(snippetsDirectory+snippetsFile, 1).replace("%! app:", "").replace("\n", "").strip()
            
            #debug
            # print(snippetsFile)
            # print(particularLine)
    

            # Split small outcomes with the delimiter ", " into a list
            li = list(particularLine.split(", "))
            for element in li:
                # lowercase outcomes and replace whitespace with dashes (to make them uniform as future .tex file names)
                test = element.replace(" ", "-").replace(",","").lower()
                
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
                    appsDict[test].append(snippetWeek)

                    #debug
                    #print(snippetWeek)
            
                #if IncludeUngroupedSnippets is false, then only include those snippets who aren't 
                # ungrouped (these are set to the UNGROUPED constant value)
                elif (weekNumber != UNGROUPED):
                    snippetWeek = [snippetsFile, weekNumber]
            
                    # add that tex filename to the dictionary
                    appsDict[test].append(snippetWeek)

                    #debug
                    #print(snippetWeek)

                #sort each outcome by week, findWeek function returns the week number of the snippet
                appsDict[test].sort(key=findWeek)
# debug: UNCOMMENT if want to see how the dictionary looks
# for k in appsDict:
    # print(k + ": " + str(appsDict[k]) + "\n")

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

        write_if_different("generated/notes/app/"+ key + ".tex", result)
