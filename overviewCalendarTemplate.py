from string import Template
import json
from userFunctions import *
  
# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())

headHtml = head("unit")


# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    head = headHtml
))

# Substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/overviewCalendar.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
unitTemplate.close()
