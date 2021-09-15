from string import Template
import json
from userFunctions import *

# returns unit-settings JSON file as a dictionary
topicData = json.loads(open("outcomes.json").read())
websiteData = json.loads(open("website-settings.json").read())

headerHtml = head()

#Sidebar top with title of course offering
sidebarButtons = sidebar("topic")

#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = mobileSidebar("topic")

boxString = ""
#big for loop begin
for i in topicData:

    boxString += """<div class="box"> \n"""

    boxString += "<h2>" + topicData[i]['Icon'] + i + "</h2>"
    boxString += "<p> Description: " + topicData[i]['Description'] + "</p>"
    boxString += "<hr>"

    boxString += """<div class="column"> <dl> \n"""

    
    for j in topicData[i]['Children']:

        #add link to page of 2nd tier children with subtopics (only link to pages of 2nd tier children with content)
        if(bool(topicData[i]['Children'][j]['Children'])):
             boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href=\"""" + topicData[i]['Children'][j]['file'] + """\" >""" + j + """</a></dt> \n"""
             
        else:
            boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href="javascript:void(0)" >""" + j + """</a></dt> \n"""
           

        #list children of 2nd tier children (subtopics under outcomes, these will be included on the webpage for the outcomes as PDFs and menu options)
        if(bool(topicData[i]['Children'][j]['Children'])):
            for k in topicData[i]['Children'][j]['Children']:
                boxString += "<dd>" + k + "</dd>\n"
            
            boxString += "</dl>"

    boxString += "</div>"

    boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings topicData with appropriate variables 
result = templateString.safe_substitute(
    head = headerHtml,
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewTopic.html", "w")
resultFile.write(result)
resultFile.close()



# Closing files
unitTemplate.close()
