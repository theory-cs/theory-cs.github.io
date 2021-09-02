from string import Template
import json
  
# Opening JSON file
fileJson = open('unitTemplate.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

sidebarButtons = ""
for i in range(1,len(data)+1):
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= " """ + 'unit'+str(i) + """.html" aria-label="Go to """ + data['unit'+str(i)]['header'] + """ ">"""
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
    pdf=""
    tex=""
    html=""

    #extract and format all PDFs and associated buttons
    pdfString="" 
    for j in range(len(data['unit'+str(i)]['pdfs'])):


        if(data['unit'+str(i)]['pdfs'][j]['addExtensions']):
            #format all filenames 
            pdf= "../output/"+data['unit'+str(i)]['pdfs'][j]['file']+".pdf"
            tex= "../notes/Lessons/"+data['unit'+str(i)]['pdfs'][j]['file']+".tex"
            html="../output/"+data['unit'+str(i)]['pdfs'][j]['file']+".html"
        else:
             pdf=data['unit'+str(i)]['pdfs'][j]['file']

        #heading and PDF download button
        pdfString += """<h2 tabindex = "2"> """+ data['unit'+str(i)]['pdfs'][j]['name'] +"""</h2>
           <a tabindex = "2" class="button PDF" aria-label="Download PDF" href="""+ pdf+ """ download>PDF</a> """
        
        #.tex/.html button
        if( data['unit'+str(i)]['pdfs'][j]['addExtensions']):
            #.tex
            pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
            href=""" + tex + """ download>TeX</a> """
            #.html
            pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
            href= """ + html + """ target="HTML">Raw HTML</a>"""

        
        #Open in Overleaf button
        if('overleafLink' in data['unit'+str(i)]['pdfs'][j]):
            pdfString += """ <a tabindex = "2" class="button Overleaf" aria-label="Open in Overleaf" 
            href= """ + data['unit'+str(i)]['pdfs'][j]['overleafLink'] + """ target="Overleaf">Overleaf</a> """

        #Annotations on/off buttons 
        if('annotatedFile' in data['unit'+str(i)]['pdfs'][j]):
            pdfString += """ <a tabindex = "2" class="button on" aria-label="Annotations On" id="annotationsOnButton" href="javascript:void(0)" >Annotations On</a>
					<a tabindex = "2" class="button off" aria-label="Annotations Off" id="annotationsOffButton" href="javascript:void(0)" >Annotations Off</a> """

            #annotations on
            pdfString += """ <script> document.getElementById("annotationsOnButton").onclick = function() {annotations(1,
            \""""+pdf+ """\",\"../files/"""+data['unit'+str(i)]['pdfs'][j]['annotatedFile']+"""\", \""""+data['unit'+str(i)]['pdfs'][j]['name']+ """\")};"""
            
            #annotations off
            pdfString +="""document.getElementById("annotationsOffButton").onclick = function() {annotations(0,
            \""""+pdf+ """\",\"../files/"""+data['unit'+str(i)]['pdfs'][j]['annotatedFile']+"""\", \""""+data['unit'+str(i)]['pdfs'][j]['name']+ """\")};
            </script>"""

       #if addExtensions is false, then the displayed pdf will be in the files directory 
        if(not data['unit'+str(i)]['pdfs'][j]['addExtensions']): 
            #pdf.js embed from files
            pdfString += """ <br> <iframe class="PDFjs" id=\""""+ data['unit'+str(i)]['pdfs'][j]['name'] +"""\" src="web/viewer.html?file=../../files/"""+ pdf+ """" 
            title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
        else:     
            #pdf.js embed default 
            pdfString += """ <br> <iframe class="PDFjs" id=\""""+ data['unit'+str(i)]['pdfs'][j]['name'] +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
            title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

    #Information Section
    if('Information' in data['unit'+str(i)]): 
        infoString = "<dl><dt>"+ data['unit'+str(i)]['Information'][0]+ "</dt>"   
        data['unit'+str(i)]['Information']                 
        for k in range(1, len(data['unit'+str(i)]['Information'])) :              
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
unitTemplate.close()
