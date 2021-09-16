from string import Template
import json
from userFunctions import *

template = ["overviewCalendarTemplate", "overviewTopicTemplate", "overviewApplicationTemplate"]
generated = ["overviewCalendar", "overviewTopic", "overviewApplication"]

for i in range (len(template)):
    overviewTemplate = open(template[i] + ".html", "r")
    templateString = Template(overviewTemplate.read())
    
    page_variables = site_variables.copy()
    page_variables.update(dict())
    
    # Substitute settings unitData with appropriate variables 
    result = templateString.substitute(page_variables)
    
    resultFile = open("generated/website/" + generated[i] + ".html", "w")
    resultFile.write(result)
    resultFile.close()
    
    # Close files
    overviewTemplate.close()