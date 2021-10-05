from string import Template
import json
from userFunctions import *

# Opening JSON file
outcomeData = json.loads(open("outcomes.json").read())

#main for loop begin
for big in outcomeData:
  for med in outcomeData[big]['Children']:

    #extract and format all PDFs and associated buttons
    pdfString = ""
    collapseVar = 1

    for small in outcomeData[big]['Children'][med]['Children']:
      
      #format pdf/html/tex file names
      file = outcomeData[big]['Children'][med]['Children'][small]['filename']
      pdf="../output/topic/" + file + ".pdf"
      html="../output/topic/" + file + ".html"
      tex="../notes/topic-flat/" + file + ".tex"
            
      #heading and collapsible card stuff
      pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
      href="#collapse"""+ str(collapseVar)+"\"> "+small+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
      class="collapse" data-parent="#accordion"><div class="card-body">"""
            
      #Learning Goal
      pdfString += """ <p> Learning Goal: """+ outcomeData[big]['Children'][med]['Children'][small]['Description']+"""</p>"""
            
      #.pdf Download button
      pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
      href="""+pdf+""" download>PDF</a>"""

      #.tex Download button
      pdfString += """ <a tabindex = "2" class="button LaTeX" aria-label="Download .LaTeX" 
      href=""" + tex + """ download>LaTeX</a> """

      #Raw HTML button 
      pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
      href= """ + html + """ target="HTML">Raw HTML</a>"""
        
      #pdf.js embed 
      pdfString += """ <br> <iframe class="PDFjs" id=\""""+ small +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
      title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

      #closing div for collapsible menu item 
      pdfString += """</div></div></div>"""
            
      #increment collapseVar
      collapseVar += 1

    #Information Section
    infoString = "<p>"+ outcomeData[big]['Children'][med]['Description']+ "</p>" 
    
    
    #open topicTemplate html file and read it into a string 
    topicTemplate = open("templates/topicTemplate.html", "r")
    templateString = Template(topicTemplate.read())


    page_variables = site_variables.copy()
    page_variables.update(dict(
    heading = med,
    Information = infoString, 
    collapsibleMenu = pdfString
    ))

    #substitute settings outcomeData with appropriate variables 
    result = templateString.substitute(page_variables)

    resultFile = open("generated/website/"+outcomeData[big]['Children'][med]['file'], "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
topicTemplate.close()
