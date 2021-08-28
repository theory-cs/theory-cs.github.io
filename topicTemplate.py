from string import Template
import json
  
# Opening JSON file
fileJson = open('outcomes.json',)
path = open('outcomesPath.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)
path = json.load(path)

sidebarButtons = ""
for i in data:
    for j in data['i']['Children']:
        sidebarButtons += "<li>"
        # we worked until here 8/27
        sidebarButtons += """<a href= " """ + j + """.html" aria-label="Go to """ + j + """ ">"""
        sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i) + """</p></i>"""
        sidebarButtons += """<span class="links_name"> """ + data['unit'+str(i)]['header'] + """</span>"""
        sidebarButtons += "</a>"
        sidebarButtons += """<span class="tooltip"> """ + data['unit'+str(i)]['header'] + """</span>"""
        sidebarButtons += "</li>"

mobileSidebar = ""
for i in range(1,len(data)+1):
   mobileSidebar += """<a href= \"""" + 'unit'+str(i) + """.html\"">""" + data['unit'+str(i)]['header'] + """</a>"""

#big for loop begin
for i in range(1,len(data)+1):

    #extract and format all PDFs and associated buttons
    pdfString="" 
    for j in range(len(data['unit'+str(i)]['pdfs'])):
        #heading and PDF download button
        pdfString += """<h2 tabindex = "2"> """+ data['unit'+str(i)]['pdfs'][j]['name'] +"""</h2>
           <a tabindex = "2" class="button PDF" aria-label="Download PDF" href="""+ data['unit'+str(i)]['pdfs'][j]['filePath']+ """ download>PDF</a> """
        
        #.tex Download button
        if(data['unit'+str(i)]['pdfs'][j]['.texIncluded']):
            pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
            href=""" + data['unit'+str(i)]['pdfs'][j]['.texPath'] + """ download>TeX</a> """
        
        #Open in Overleaf button
        if(data['unit'+str(i)]['pdfs'][j]['overleafIncluded']):
            pdfString += """ <a tabindex = "2" class="button Overleaf" aria-label="Open in Overleaf" 
            href= """ + data['unit'+str(i)]['pdfs'][j]['overleafLink'] + """ target="Overleaf">Overleaf</a> """

        #Raw HTML button 
        if(data['unit'+str(i)]['pdfs'][j]['htmlIncluded']):
            pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
            href= """ + data['unit'+str(i)]['pdfs'][j]['htmlPath'] + """ target="HTML">Raw HTML</a>"""
        
        #Annotations on/off buttons 
        if(data['unit'+str(i)]['pdfs'][j]['annotated']):
            pdfString += """ <a tabindex = "2" class="button on" aria-label="Annotations On" id="annotationsOnButton" href="javascript:void(0)" >Annotations On</a>
					<a tabindex = "2" class="button off" aria-label="Annotations Off" id="annotationsOffButton" href="javascript:void(0)" >Annotations Off</a> """

            #annotations on
            pdfString += """ <script> document.getElementById("annotationsOnButton").onclick = function() {annotations(1,
            \""""+data['unit'+str(i)]['pdfs'][j]['filePath']+ """\",\""""+data['unit'+str(i)]['pdfs'][j]['annotatedPath']+"""\", \""""+data['unit'+str(i)]['pdfs'][j]['name']+ """\")};"""
            
            #annotations off
            pdfString +="""document.getElementById("annotationsOffButton").onclick = function() {annotations(0,
            \""""+data['unit'+str(i)]['pdfs'][j]['filePath']+ """\",\""""+data['unit'+str(i)]['pdfs'][j]['annotatedPath']+"""\", \""""+data['unit'+str(i)]['pdfs'][j]['name']+ """\")};
            </script>"""
    
        #pdf.js embed 
        pdfString += """ <br> <iframe class="PDFjs" id=\""""+ data['unit'+str(i)]['pdfs'][j]['name'] +"""\" src="web/viewer.html?file="""+ data['unit'+str(i)]['pdfs'][j]['filePath']+ """" 
        title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

    #Information Section
    if(data['unit'+str(i)]['Information'][0]): 
        infoString = "<dl><dt>"+ data['unit'+str(i)]['Information'][1]+ "</dt>"   
        data['unit'+str(i)]['Information']                 
        for k in range(2, len(data['unit'+str(i)]['Information'])) :              
            infoString += "<dd>"+ data['unit'+str(i)]['Information'][k] +"</dd>"
    infoString += "</dl>"

    
    #Embedded links section
    embedString = ""
    for j in range(len(data['unit'+str(i)]['embed'])): 
        embedString += "<h2>"+data['unit'+str(i)]['embed'][j]['name']+"</h2>"+ data['unit'+str(i)]['embed'][j]['embedCode']



    #open unitTemplate html file and read it into a string 
    unitTemplate = open("unitTemplate.html", "r")
    templateString = Template(unitTemplate.read())

    #substitute settings data with appropriate variables 
    result = templateString.safe_substitute(
        heading = data['unit'+str(i)]['header'],
        Information = infoString, 
        PDF = pdfString,
        embed = embedString,
        sidebar = sidebarButtons,
        mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+'unit'+str(i)+".html", "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
fileJson.close()
path.close()
