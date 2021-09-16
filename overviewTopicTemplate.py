from string import Template
import json
from userFunctions import *

# UNIT
# Open overviewCalendarTemplate html file and read it into a string 
overviewCalendarTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(overviewCalendarTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict())

# Substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)

resultFile = open("generated/website/overviewCalendar.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
overviewCalendarTemplate.close()

# template = ["overviewTopicTemplate.html", "overviewApplicationTemplate.html"]
# result = ["overviewTopic.html", "overviewApplication.html"]

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
