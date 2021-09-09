from string import Template
import json
  
# Opening JSON file
fileJson = open('unitTemplate.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

sidebarButtons = ""
for i in range(0,len(data)):
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= " """ + 'unit'+str(i+1) + """.html" aria-label="Go to """ + data[i]['header'] + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i+1) + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + data[i]['header'] + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + data[i]['header'] + """</span>"""
    sidebarButtons += "</li>"

mobileSidebar = ""
for i in range(0,len(data)):
   mobileSidebar += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + data[i]['header'] + """</a>"""

#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(   
    sidebar = sidebarButtons,
    mobile = mobileSidebar
)


resultFile = open("generated/website/overview.html", "w")
resultFile.write(result)
resultFile.close()

# Closing files
fileJson.close()
unitTemplate.close()
