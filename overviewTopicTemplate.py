from string import Template
import json

# returns unit-settings JSON file as a dictionary
topicData = json.loads(open("outcomes.json").read())
websiteData = json.loads(open("website-settings.json").read())


#Sidebar top with title of course offering
sidebarButtons = """<div class="sidebar">
		<div class="logo-details">
		  
		    <div class="logo_name"><i class='bx bx-home-smile'></i> </div>
			<a href="index.html" class="logo_name">""" + websiteData['Global Class Name']+"""</a> <!--NAME-->
			<i class='bx bx-menu' id="btn" ></i>
		</div>

		<ul class="nav-list">
			
			<li>
				<a href="overviewTopic.html" aria-label="Go to Overview">
					<i class='bx bx-list-ul'></i>
					<span class="links_name">Overview</span>
				</a>
				<span class="tooltip">Overview</span>
			</li>"""


#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
for i in topicData:
    for j in topicData[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(topicData[i]['Children'][j]['Children'])):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= \"""" +topicData[i]['Children'][j]['file'] + """\" aria-label="Go to """ + j + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + topicData[i]['Children'][j]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + j + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + j + """</span>"""
            sidebarButtons += "</li>"

#end div tags and script for sidebar
sidebarButtons += """</ul> </div> 
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
	</script>"""


#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = """ <div id="mySidebar" class="collapsedSidebar">
		<a href="index.html" class="homeMobile"> """ + websiteData['Global Class Name']+"""</a> <!--NAME-->
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
        <a href="overviewTopic.html">Overview</a>
			"""


#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
for i in topicData:
    for j in topicData[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(topicData[i]['Children'][j]['Children'])):
            mobileSidebar += """<a href= \"""" + topicData[i]['Children'][j]['file'] + """\"">""" + j + """</a>"""

#end div tags, open button, and script for mobile sidebar 
mobileSidebar += """</div> <br>
	<div class="openbutton" style="margin-left: 10px;">
		<button class="openbtn"  onclick="openNav()">☰ Open Sidebar</button> <br><br>
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
	</script> """


boxString = ""
#big for loop begin
for i in topicData:

    boxString += """<div class="box"> \n"""

    boxString += "<h2>" + topicData[i]['Icon'] + i + "</h2>"
    boxString += "<p> Description: " + topicData[i]['Description'] + "</p>"
    boxString += "<hr>"

    boxString += """<div class="column"> <dl> \n"""

    
    for j in topicData[i]['Children']:

        #add link to page of 2nd tier children with subtopics (only link to pages of 2nd tier children with content)
        if(bool(topicData[i]['Children'][j]['Children'])):
             boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href=\"""" + topicData[i]['Children'][j]['file'] + """\" >""" + j + """</a></dt> \n"""
             
        else:
            boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href="javascript:void(0)" >""" + j + """</a></dt> \n"""
           

        #list children of 2nd tier children (subtopics under outcomes, these will be included on the webpage for the outcomes as PDFs and menu options)
        if(bool(topicData[i]['Children'][j]['Children'])):
            for k in topicData[i]['Children'][j]['Children']:
                boxString += "<dd>" + k + "</dd>\n"
            
            boxString += "</dl>"

    boxString += "</div>"

    boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings topicData with appropriate variables 
result = templateString.safe_substitute(
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewTopic.html", "w")
resultFile.write(result)
resultFile.close()



# Closing files
unitTemplate.close()
