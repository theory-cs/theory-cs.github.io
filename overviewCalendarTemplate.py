from string import Template
import json
from userFunctions import *
  
# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())

for i in range (1, len(unitData)+1):
    index = i-1
    boxString =""
    
    #set appropriate variables for top calendar information section and title 
    weekNumber = i
    info=""
    if('CalendarInfo' in unitData[index]):
        info=unitData[index]['CalendarInfo']
    
    
    #box heading and subheading/description
    boxString += """<div class="box"> \n"""
    boxString += "<h2> Week " + str(weekNumber) + "</h2>"
    boxString += "<p> " + info + "</p>"
    boxString += "<hr>"

    #list begins
    boxString += """<div class="column"> <dl> \n"""

    #Learning Materials (link to contents on weekly page)
    boxString += """<dt><i class='bx bxs-right-arrow'></i>Learning Materials</dt> \n"""
    #pdfs
    if('pdfs' in unitData[index]):
        for pdf in unitData[index]['pdfs']:
            pdfjsID = pdf['name'].replace(" ", "-")
            boxString += "<dd> <a href=\"unit""" +str(i)+ """.html#"""+ pdfjsID+"""\" >""" + pdf['name'] + """</a></dd>\n"""
    #embeds
    if('embed' in unitData[index]):
        for embed in unitData[index]['embed']:
            embedID = embed['name'].replace(" ", "-")
            boxString += "<dd> <a href=\"unit""" +str(i)+ """.html#"""+ embedID+"""\" >""" + embed['name'] + """</a></dd>\n"""

    #Assignments
    boxString += """<dt><i class='bx bxs-right-arrow'></i>Assignments</dt> \n"""
    if('Assignments' in unitData[index]):
        for assignment in unitData[index]['Assignments']:
           
            #if link is provided use that link
            link=""
            if('link' in assignment):
                link=assignment['link']
            #else refer to the assignments page (default)
            else:
                cardID = assignment['name'].replace(" ", "").lower()
                link="""assignments.html#collapse"""+cardID
            
            boxString += "<dd> <a href=\"""" +link+ """\">"""+assignment['name']+"""</a></dd>\n"""  

    
    boxString += "</dl>"


    boxString += "</div>"
    boxString += "</div><br><br>"

    



# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    unitBoxes = boxString
))

# Substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/overviewCalendar.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
unitTemplate.close()
