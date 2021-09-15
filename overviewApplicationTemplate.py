from string import Template
import json
from userFunctions import *  

# returns unit-settings JSON file as a dictionary
appData = json.loads(open("applications.json").read())
websiteData = json.loads(open("website-settings.json").read())

headerHtml = head("application")

#Mobile Sidebar top with Title of Course Offering
mobileSidebar = mobileSidebar("application")

boxString = """<div class="box"> \n"""
#big for loop begin
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	boxString += """<h2> <i style= "font-size: 75%;" class='bx bxs-chevron-right-square'></i> <a href= \"""" + file + """\" style="color: #182B49; text-decoration: none; font-size: 75%; font-weight: normal;" >""" + i + """</a></h2>"""

boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewApplicationTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    head = headerHtml,
    mobile = mobileSidebar,
    boxes = boxString
))

#substitute settings appData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/overviewApplication.html", "w")
resultFile.write(result)
resultFile.close()

unitTemplate.close()
