from string import Template
import json
from userFunctions import *

# Opening JSON file
assignmentData = json.loads(open("assignments.json").read())
websiteData = json.loads(open("website-settings.json").read())



templateString = ""
collapseVar = 0
#main for loop begin (only for collapsible menu items)
for element in assignmentData:
    pdf=""
    tex=""
    html=""

    #increment collapseVar (helps with collapsible card menu function)
    collapseVar+= 1

    #format all filenames if addExtensions is true
    if(element['addExtensions']):
       pdf="../output/lessons/"+element['file']+".pdf"
       tex="../notes/lessons/"+element['file']+".tex"
       html="../output/lessons/"+element['file']+".html"
    else:
        pdf="../output/lessons/"+element['file']+".pdf"
    
    #heading and collapsible card stuff
    cardID = element['name'].replace(" ", "").lower()
    templateString += """<div class="card" id=\""""+cardID+"""\"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
      href="#collapse"""+ cardID+"\"> "+element['name']+"""</a> </div> <div id="collapse""" + cardID+ """""
      class="collapse" data-parent="#accordion"><div class="card-body">"""

    #Assignment Information
    templateString += """ <p> """+ element['Information']+"""</p>"""

    #.pdf Download button
    templateString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
    href="""+pdf+""" download>PDF</a>"""

    #html and tex download buttons
    if(element['addExtensions']):
        #.tex
        templateString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
        href=""" + tex + """ download>TeX</a> """

        #.html
        templateString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
        href= """ + html + """ target="HTML">Raw HTML</a>"""
        
    #Solutions on/off buttons 
    if('solutionsFile' in element):
        #id of pdf.js element formatting
        pdfjsID = element['name'].replace(" ", "-")
        
        templateString += """ <a tabindex = "2" class="button on" aria-label="Solutions On" id="solutionsOnButton"""+str(collapseVar)+ """/" href="javascript:void(0)" >Solutions On</a>
		<a tabindex = "2" class="button off" aria-label="Solutions Off" id="solutionsOffButton"""+str(collapseVar)+ """/" href="javascript:void(0)" >Solutions Off</a> """

       #annotations on
        templateString += """ <script> document.getElementById("solutionsOnButton"""+str(collapseVar)+ """/").onclick = function() {annotations(1,
        \""""+pdf+ """\",\"../files/"""+element['solutionsFile']+"""\", \""""+pdfjsID+ """\")};"""
            
        #annotations off
        templateString +="""document.getElementById("solutionsOffButton"""+str(collapseVar)+ """/").onclick = function() {annotations(0,
        \""""+pdf+ """\",\"../files/"""+element['solutionsFile']+"""\", \""""+pdfjsID+ """\")};
        </script>"""
            
    #pdf.js embed 
    templateString += """ <br> <iframe class="PDFjs" id=\""""+ pdfjsID +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

    #closing div for collapsible menu item 
    templateString += """</div></div></div>"""

#end for loop
        
        
#open assignmentTemplate html file and read it into a string 
assignmentTemplate = open("assignment-template.html", "r")
substituteString = Template(assignmentTemplate.read())


page_variables = site_variables.copy()
page_variables.update(dict(
    collapsibleMenu = templateString
))

#substitute settings outcomeData with appropriate variables 
result = substituteString.substitute(page_variables)
    

        
        
resultFile = open("generated/website/assignments.html", "w")
resultFile.write(result)
resultFile.close()

   


# Closing files
assignmentTemplate.close()
        

    

