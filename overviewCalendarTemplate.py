from string import Template
import json
  
# Opening JSON file
fileJson = open('unit-settings.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)


# Generate sidebar buttons
sidebarButtons = ""
for i in range(0,len(data)):
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= " """ + 'unit'+str(i+1) + """.html" aria-label="Go to """ + data[i]['header'] + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i+1) + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + data[i]['header'] + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + data[i]['header'] + """</span>"""
    sidebarButtons += "</li>"


# Generate mobile sidebar buttons
mobileSidebar = ""
for i in range(0,len(data)):
   mobileSidebar += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + data[i]['header'] + """</a>"""

# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

# Substitute settings data with appropriate variables 
result = templateString.safe_substitute(   
    sidebar = sidebarButtons,
    mobile = mobileSidebar
)


resultFile = open("generated/website/overview.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
fileJson.close()
unitTemplate.close()
