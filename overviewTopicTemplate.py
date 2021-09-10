from string import Template
import json
  
# Opening JSON file
fileJson = open('outcomes.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
sidebarButtons = ""
for i in data:
    for j in data[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[i]['Children'][j]['Children'])):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= \"""" +data[i]['Children'][j]['file'] + """\" aria-label="Go to """ + j + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + data[i]['Children'][j]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + j + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + j + """</span>"""
            sidebarButtons += "</li>"

#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
mobileSidebar = ""
for i in data:
    for j in data[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[i]['Children'][j]['Children'])):
            mobileSidebar += """<a href= \"""" + data[i]['Children'][j]['file'] + """\"">""" + j + """</a>"""



boxString = ""
#big for loop begin
for i in data:

    boxString += """<div class="box"> \n"""

    boxString += "<h2>" + data[i]['Icon'] + i + "</h2>"
    boxString += "<p> Description: " + data[i]['Description'] + "</p>"
    boxString += "<hr>"

    boxString += """<div class="column"> <dl> \n"""

    
    for j in data[i]['Children']:

        #add link to page of 2nd tier children with subtopics (only link to pages of 2nd tier children with content)
        if(bool(data[i]['Children'][j]['Children'])):
             boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href=\"""" + data[i]['Children'][j]['file'] + """\" >""" + j + """</a></dt> \n"""
             
        else:
            boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href="javascript:void(0)" >""" + j + """</a></dt> \n"""
           

        #list children of 2nd tier children (subtopics under outcomes, these will be included on the webpage for the outcomes as PDFs and menu options)
        if(bool(data[i]['Children'][j]['Children'])):
            for k in data[i]['Children'][j]['Children']:
                boxString += "<dd>" + k + "</dd>\n"
            
            boxString += "</dl>"

    boxString += "</div>"

    boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewTopicTemplate.html", "w")
resultFile.write(result)
resultFile.close()



# Closing files
fileJson.close()
