from string import Template
import json
  
# Opening JSON file
fileJson = open('outcomeTest.json',)
path = open('outcomesPath.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)
path = json.load(path)

sidebarButtons = ""
for i in data:
    for j in data[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[i]['Children'][j]['Children'])):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= " """ + j + """.html" aria-label="Go to """ + j + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + data[i]['Children'][j]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + j + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + j + """</span>"""
            sidebarButtons += "</li>"

mobileSidebar = ""
for i in data:
    for j in data[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[i]['Children'][j]['Children'])):
            mobileSidebar += """<a href= \"""" + data[i]['Children'][j]['file'] + """\"">""" + j + """</a>"""

#big for loop begin
for i in data:
    for j in data[i]['Children']:

    #extract and format all PDFs and associated buttons
        pdfString = ""
        collapseVar = 1

        for k in data[i]['Children'][j]['Children']:
            #heading and collapsible card stuff
            pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
            href="#collapse"""+ str(collapseVar)+"\"> "+k+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
            class="collapse" data-parent="#accordion"><div class="card-body">"""
            
            #Learning Goal
            pdfString += """ <p> Learning Goal: """+ data[i]['Children'][j]['Children'][k]['Description']+"""</p>"""
            
            #.pdf Download button
            pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
            href="""+data[i]['Children'][j]['Children'][k]['pdf']+""" download>PDF</a>"""

            #.tex Download button
            pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
            href=""" + data[i]['Children'][j]['Children'][k]['.tex'] + """ download>TeX</a> """
        
            #Open in Overleaf button
            pdfString += """ <a tabindex = "2" class="button Overleaf" aria-label="Open in Overleaf" 
            href= """ + data[i]['Children'][j]['Children'][k]['overleaf'] + """ target="Overleaf">Overleaf</a> """

            #Raw HTML button 
            pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
            href= """ + data[i]['Children'][j]['Children'][k]['html'] + """ target="HTML">Raw HTML</a>"""
        
            #pdf.js embed 
            pdfString += """ <br> <iframe class="PDFjs" id=\""""+ k +"""\" src="web/viewer.html?file="""+ data[i]['Children'][j]['Children'][k]['pdf']+ """" 
            title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

            #closing div for collapsible menu item 
            pdfString += """</div></div></div>"""
            
            #increment collapseVar
            collapseVar += 1

   #Information Section
    infoString = "<p>"+ data[i]['Children'][j]['Description']+ "</p>" 
    
    
    #open unitTemplate html file and read it into a string 
    unitTemplate = open("topicTemplate.html", "r")
    templateString = Template(unitTemplate.read())



    #substitute settings data with appropriate variables 
    result = templateString.safe_substitute(
    heading = j,
    Information = infoString, 
    collapsibleMenu = pdfString,
    sidebar = sidebarButtons,
    mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+data[i]['Children'][j]['file'], "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
fileJson.close()
