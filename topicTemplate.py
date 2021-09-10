from string import Template
import json
  
# Opening JSON file
#fileJson = open('outcomeTest.json',)
fileJson = open('outcomes.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

sidebarButtons = ""
for big in data:
    for med in data[big]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[big]['Children'][med]['Children'])):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= \"""" +data[big]['Children'][med]['file'] + """\" aria-label="Go to """ + med + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + data[big]['Children'][med]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + med + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + med + """</span>"""
            sidebarButtons += "</li>"

mobileSidebar = ""
for big in data:
    for med in data[big]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[big]['Children'][med]['Children'])):
            mobileSidebar += """<a href= \"""" + data[big]['Children'][med]['file'] + """\"">""" + med + """</a>"""

#main for loop begin
for big in data:
    for med in data[big]['Children']:

    #extract and format all PDFs and associated buttons
        pdfString = ""
        collapseVar = 1

        for small in data[big]['Children'][med]['Children']:
            #format pdf/html/tex file names
            pdf="../output/"+data[big]['Children'][med]['Children'][small]['filename']+".pdf"
            html="../output/"+data[big]['Children'][med]['Children'][small]['filename']+".html"
            ##where will tex file for topics be shown? 
            tex="../notes/"+data[big]['Children'][med]['Children'][small]['filename']+".tex"
            
            #heading and collapsible card stuff
            pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
            href="#collapse"""+ str(collapseVar)+"\"> "+small+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
            class="collapse" data-parent="#accordion"><div class="card-body">"""
            
            #Learning Goal
            pdfString += """ <p> Learning Goal: """+ data[big]['Children'][med]['Children'][small]['Description']+"""</p>"""
            
            #.pdf Download button
            pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
            href="""+pdf+""" download>PDF</a>"""

            #.tex Download button
            pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
            href=""" + tex + """ download>TeX</a> """

            #Raw HTML button 
            pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
            href= """ + html + """ target="HTML">Raw HTML</a>"""
        
            #pdf.js embed 
            pdfString += """ <br> <iframe class="PDFjs" id=\""""+ small +"""\" src="web/viewer.html?file="""+ pdf+ """" 
            title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

            #closing div for collapsible menu item 
            pdfString += """</div></div></div>"""
            
            #increment collapseVar
            collapseVar += 1

   #Information Section
    infoString = "<p>"+ data[big]['Children'][med]['Description']+ "</p>" 
    
    
    #open unitTemplate html file and read it into a string 
    unitTemplate = open("topicTemplate.html", "r")
    templateString = Template(unitTemplate.read())



    #substitute settings data with appropriate variables 
    result = templateString.safe_substitute(
    heading = med,
    Information = infoString, 
    collapsibleMenu = pdfString,
    sidebar = sidebarButtons,
    mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+data[big]['Children'][med]['file'], "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
fileJson.close()
