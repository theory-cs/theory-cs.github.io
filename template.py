from string import Template
import json
from userFunctions import *

template = ["indexTemplate", "feedbackTemplate", "overviewCalendarTemplate", "overviewTopicTemplate", "overviewApplicationTemplate", "assignment-template"]
generated = ["index", "feedback", "overviewCalendar", "overviewTopic", "overviewApplication", "assignments"]

for i in range (len(template)):
    templateOpener = open("templates/"+template[i] + ".html", "r")
    templateString = Template(templateOpener.read())
    
    page_variables = site_variables.copy()
    page_variables.update(dict())
    
    # Substitute settings unitData with appropriate variables 
    result = templateString.substitute(page_variables)
    
    resultFile = open("generated/website/" + generated[i] + ".html", "w")
    resultFile.write(result)
    resultFile.close()
    
    # Close files
    templateOpener.close()