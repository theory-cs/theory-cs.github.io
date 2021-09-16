from string import Template 
import json
from userFunctions import *
  
# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())

for i in range (1, len(unitData)+1):
    boxString =""
    
    #set appropriate variables with information from unit-settings.json
    weekNumber = i
    info=""
    if('CalendarInfo' in unitData[i-1]):
        dates=unitData[i-1]['CalendarInfo']
    assignments=""
    if('Assignments' in unitData[i-1]):
        assignments= unitData[i-1]['Assignments']
    
    #box heading and subheading/description
    boxString += """<div class="box"> \n"""
    boxString += "<h2> Week " + str(weekNumber) + "</h2>"
    boxString += "<p> " + info + "</p>"
    boxString += "<hr>"

    #list begins
    boxString += """<div class="column"> <dl> \n"""

    boxString += "</dl>"
    boxString += "</div>"
    boxString += "</div><br><br>"

    



# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    unitBoxes = boxString
))

# Substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/overviewCalendar.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
unitTemplate.close()
