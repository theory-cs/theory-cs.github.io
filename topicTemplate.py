from string import Template
import json
  
# Opening JSON file
outcomeData = json.loads(open("outcomes.json").read())
websiteData = json.loads(open("website-settings.json").read())

sidebarButtons = """<div class="sidebar">
		<div class="logo-details">
		  <!--<i class='bx bxl-c-plus-plus icon'></i>-->
			<div class="logo_name"><a href="index.html" aria-label="Go to Homepage">""" + websiteData['Course Offering Title'] +"""</a></div>
			<i class='bx bx-menu' id="btn" ></i>
		</div>

		<ul class="nav-list">"""

for big in outcomeData:
    for med in outcomeData[big]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(outcomeData[big]['Children'][med]['Children'])):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= \"""" +outcomeData[big]['Children'][med]['file'] + """\" aria-label="Go to """ + med + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + outcomeData[big]['Children'][med]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + med + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + med + """</span>"""
            sidebarButtons += "</li>"

#end div tags and script for sidebar
sidebarButtons += """</ul>
	</div> 
		
	<script>
		let sidebar = document.querySelector(".sidebar");
		let closeBtn = document.querySelector("#btn");
		
		closeBtn.addEventListener("click", ()=>{
			sidebar.classList.toggle("open");
			menuBtnChange();//calling the function(optional)
		});
		
		searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
			sidebar.classList.toggle("open");
			menuBtnChange(); //calling the function(optional)
		});
		
		// following are the code to change sidebar button(optional)
		function menuBtnChange() {
			if(sidebar.classList.contains("open")){
				closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
		   	}

			else {
				closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
		   	}
		}
	</script>		"""

mobileSidebar = ""
for big in outcomeData:
    for med in outcomeData[big]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(outcomeData[big]['Children'][med]['Children'])):
            mobileSidebar += """<a href= \"""" + outcomeData[big]['Children'][med]['file'] + """\"">""" + med + """</a>"""

#main for loop begin
for big in outcomeData:
    for med in outcomeData[big]['Children']:

    #extract and format all PDFs and associated buttons
        pdfString = ""
        collapseVar = 1

        for small in outcomeData[big]['Children'][med]['Children']:
            #format pdf/html/tex file names
            pdf="../output/"+outcomeData[big]['Children'][med]['Children'][small]['filename']+".pdf"
            html="../output/"+outcomeData[big]['Children'][med]['Children'][small]['filename']+".html"
            ##where will tex file for topics be shown? 
            tex="../notes/"+outcomeData[big]['Children'][med]['Children'][small]['filename']+".tex"
            
            #heading and collapsible card stuff
            pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" outcomeData-toggle="collapse" 
            href="#collapse"""+ str(collapseVar)+"\"> "+small+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
            class="collapse" outcomeData-parent="#accordion"><div class="card-body">"""
            
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
            pdfString += """ <br> <iframe class="PDFjs" id=\""""+ small +"""\" src="web/viewer.html?file="""+ pdf+ """" 
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
