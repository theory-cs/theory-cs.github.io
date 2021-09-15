from string import Template
import json
from userFunctions import *
  
# returns unit-settings JSON file as a dictionary
appData = json.loads(open("applications.json").read())
websiteData = json.loads(open("website-settings.json").read())


headHtml = head()

#Sidebar top with title of course offering
sidebarButtons = sidebar("application")

#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = mobileSidebar("application")

for (k,v) in appData.items():
    #extract and format all PDFs and associated buttons
    file = k.replace(" ", "-").lower()

    pdfString = ""
    collapseVar = 1

    #format pdf/html/tex file names
    pdf="../output/app/"+file+".pdf"
    html="../output/app/"+file+".html"
    #where will tex file for applications be shown? 
    tex="../notes/app/"+file+".tex"

    #heading and collapsible card stuff
    #pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
    #href="#collapse"""+ str(collapseVar)+"\"> "+k+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
    #class="collapse" data-parent="#accordion"><div class="card-body">"""
            
    #Learning Goal
    #pdfString += """ <p> Learning Goal: """+ appData[i]['Children'][j]['Children'][k]['Description']+"""</p>"""
            
    #.pdf Download button
    pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
    href="""+pdf+""" download>PDF</a>"""

    #.tex Download button
    pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
    href=""" + tex + """ download>TeX</a> """
        
    #Open in Overleaf button
    # pdfString += """ <a tabindex = "2" class="button Overleaf" aria-label="Open in Overleaf" 
    # href= """ + appData[i]['Children'][k]['overleaf']+ """ target="Overleaf">Overleaf</a> """

    #Raw HTML button 
    pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
    href= """ + html + """ target="HTML">Raw HTML</a>"""
        
    #pdf.js embed 
    pdfString += """ <br> <iframe class="PDFjs" id=\""""+ k +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

    #closing div for collapsible menu item 
    # pdfString += """</div></div></div>"""
            
    #increment collapseVar
    collapseVar += 1

   #Information Section
    #infoString = "<p>"+ appData[i]['Children'][j]['Description']+ "</p>" 
    
    
    #open unitTemplate html file and read it into a string 
    appTemplate = open("appTemplate.html", "r")
    templateString = Template(appTemplate.read())

    #substitute settings appData with appropriate variables 
    result = templateString.safe_substitute(
    heading = k,
    #Information = infoString, 
    collapsibleMenu = pdfString,
    sidebar = sidebarButtons,
    head = headHtml,
    mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+file+".html", "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
appTemplate.close()