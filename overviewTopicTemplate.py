from string import Template
from userFunctions import *

headerHtml = head("topic")

#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = mobileSidebar("topic")

    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    head = headerHtml,
    mobile = mobileSidebar,
))
#substitute settings topicData with appropriate variables 
result = templateString.substitute(page_variables)

resultFile = open("generated/website/overviewTopic.html", "w")
resultFile.write(result)
resultFile.close()



# Closing files
unitTemplate.close()
