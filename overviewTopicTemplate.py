from string import Template
import json
from userFunctions import *

# UNIT
unitData = json.loads(open("unit-settings.json").read())

for i in range (1, len(unitData)+1):
    boxString =""
    
    # Set appropriate variables with information from unit-settings.json
    weekNumber = i
    info = ""

    if ('CalendarInfo' in unitData[i-1]):
        dates = unitData[i-1]['CalendarInfo']

    assignments=""
    if ('Assignments' in unitData[i-1]):
        assignments = unitData[i-1]['Assignments']
    
    # Box heading and subheading/description
    boxString += """<div class="box"> \n"""
    boxString += "<h2> Week " + str(weekNumber) + "</h2>"
    boxString += "<p> " + info + "</p>"
    boxString += "<hr>"

    # List begins
    boxString += """<div class="column"> <dl> \n"""

    boxString += "</dl>"
    boxString += "</div>"
    boxString += "</div><br><br>"


# Open overviewCalendarTemplate html file and read it into a string 
overviewCalendarTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(overviewCalendarTemplate.read())

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
overviewCalendarTemplate.close()


# TOPIC
# Open overviewTopicTemplate html file and read it into a string 
overviewTopicTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(overviewTopicTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict())

# Substitute settings topicData with appropriate variables 
result = templateString.substitute(page_variables)

resultFile = open("generated/website/overviewTopic.html", "w")
resultFile.write(result)
resultFile.close()

# Closing files
overviewTopicTemplate.close()


# APPLICATION
# returns unit-settings JSON file as a dictionary
   
#open overviewApplicationTemplate html file and read it into a string 
overviewApplicationTemplate = open("overviewApplicationTemplate.html", "r")
templateString = Template(overviewApplicationTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict())

#substitute settings appData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/overviewApplication.html", "w")
resultFile.write(result)
resultFile.close()

overviewApplicationTemplate.close()
