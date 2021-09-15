from string import Template
import json
from sidebarFunction import *

# Opening JSON file
outcomeData = json.loads(open("outcomes.json").read())
websiteData = json.loads(open("website-settings.json").read())
sidebarButtons = sidebar("topic")

mobileSidebar = """<div id="mySidebar" class="collapsedSidebar">
		<a href="index.html" class="homeMobile"> """ + websiteData['Global Class Name']+ """</a>
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
			
		<a href="overviewTopic.html">Overview</a>"""

for big in outcomeData:
    for med in outcomeData[big]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(outcomeData[big]['Children'][med]['Children'])):
            mobileSidebar += """<a href= \"""" + outcomeData[big]['Children'][med]['file'] + """\"">""" + med + """</a>"""

mobileSidebar += """ </div>

		<div class="openbutton">
			<button class="openbtn"  onclick="openNav()">☰ Open Sidebar</button> 
		</div> 
		  
		<script>
		  function openNav() {
			document.getElementById("mySidebar").style.width = "100%";
			document.getElementById("content").style.marginLeft = "100%";
		  }
		  
		  function closeNav() {
			document.getElementById("mySidebar").style.width = "0";
			document.getElementById("content").style.marginLeft= "0";
		  }
		</script>
"""


#main for loop begin
for big in outcomeData:
  for med in outcomeData[big]['Children']:

    #extract and format all PDFs and associated buttons
    pdfString = ""
    collapseVar = 1

    for small in outcomeData[big]['Children'][med]['Children']:
      #format pdf/html/tex file names
      pdf="../output/topic/"+outcomeData[big]['Children'][med]['Children'][small]['filename']+".pdf"
      html="../output/topic/"+outcomeData[big]['Children'][med]['Children'][small]['filename']+".html"
      tex="../notes/topic/"+outcomeData[big]['Children'][med]['Children'][small]['filename']+".tex"
            
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
      pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
      href=""" + tex + """ download>TeX</a> """

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
    
    
    #open unitTemplate html file and read it into a string 
    unitTemplate = open("topicTemplate.html", "r")
    templateString = Template(unitTemplate.read())



    #substitute settings outcomeData with appropriate variables 
    result = templateString.safe_substitute(
    heading = med,
    Information = infoString, 
    collapsibleMenu = pdfString,
    sidebar = sidebarButtons,
    mobile = mobileSidebar
    )
    

    resultFile = open("generated/website/"+outcomeData[big]['Children'][med]['file'], "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
unitTemplate.close()
