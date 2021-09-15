from string import Template
from userFunctions import *

    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
))
#substitute settings topicData with appropriate variables 
result = templateString.substitute(page_variables)

resultFile = open("generated/website/overviewTopic.html", "w")
resultFile.write(result)
resultFile.close()




# Closing files
unitTemplate.close()
