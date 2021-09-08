from string import Template
import json
  
# Opening JSON file
fileJson = open('applications.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

sidebarButtons = ""
for i in data:
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= \"""" + data[i]['file'] + """\" aria-label="Go to """ + i + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + data[i]['Icon'] + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + i + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + i + """</span>"""
    sidebarButtons += "</li>"

mobileSidebar = ""
for i in data:
    mobileSidebar += """<a href= \"""" + data[i]['file'] + """\"">""" + i + """</a>"""

#big for loop begin
for i in data:
    #extract and format all PDFs and associated buttons
    pdfString = ""
    collapseVar = 1

   

    for k in data[i]['Children']:

            #format pdf/html/tex file names
            pdf="../output/"+data[i]['Children'][k]['filename']+".pdf"
            html="../output/"+data[i]['Children'][k]['filename']+".html"
            #where will tex file for applications be shown? 
            tex="../notes/"+data[i]['Children'][k]['filename']+".tex"

        #heading and collapsible card stuff
            pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
            href="#collapse"""+ str(collapseVar)+"\"> "+k+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
            class="collapse" data-parent="#accordion"><div class="card-body">"""
            
            #Learning Goal
            #pdfString += """ <p> Learning Goal: """+ data[i]['Children'][j]['Children'][k]['Description']+"""</p>"""
            
            #.pdf Download button
            pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
            href="""+pdf+""" download>PDF</a>"""

            #.tex Download button
            pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
            href=""" + tex + """ download>TeX</a> """
        
            #Open in Overleaf button
            pdfString += """ <a tabindex = "2" class="button Overleaf" aria-label="Open in Overleaf" 
            href= """ + data[i]['Children'][k]['overleaf']+ """ target="Overleaf">Overleaf</a> """

            #Raw HTML button 
            pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
            href= """ + html + """ target="HTML">Raw HTML</a>"""
        
            #pdf.js embed 
            pdfString += """ <br> <iframe class="PDFjs" id=\""""+ k +"""\" src="web/viewer.html?file="""+ pdf+ """" 
            title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

            #closing div for collapsible menu item 
            pdfString += """</div></div></div>"""
            
            #increment collapseVar
            collapseVar += 1

   #Information Section
    #infoString = "<p>"+ data[i]['Children'][j]['Description']+ "</p>" 
    
    
    #open unitTemplate html file and read it into a string 
    appTemplate = open("appTemplate.html", "r")
    templateString = Template(appTemplate.read())



    #substitute settings data with appropriate variables 
    result = templateString.safe_substitute(
    heading = i,
    #Information = infoString, 
    collapsibleMenu = pdfString,
    sidebar = sidebarButtons,
    mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+data[i]['file'], "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
fileJson.close()