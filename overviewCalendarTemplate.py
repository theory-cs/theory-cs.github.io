from string import Template
import json
  
# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())


#Sidebar top with title of course offering
sidebarButtons = """<div class="sidebar" id="unit">
		<div class="logo-details">
		  
		    <div class="logo_name"><i class='bx bx-home-smile'></i> </div>
			<a href="index.html" class="logo_name">""" + websiteData['Course Offering Title']+"""</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
		</div>

		<ul class="nav-list">
			
			<li>
				<a href="overview.html" aria-label="Go to Calendar">
					<i class='bx bx-calendar'></i>
					<span class="links_name">Calendar</span>
				</a>
				<span class="tooltip">Calendar</span>
			</li>"""


# Generate sidebar buttons
for i in range(0,len(unitData)):
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= " """ + 'unit'+str(i+1) + """.html" aria-label="Go to """ + unitData[i]['header'] + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i+1) + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + unitData[i]['header'] + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + unitData[i]['header'] + """</span>"""
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
				closeBtn.classList.replace("bx-chevron-right", "bx-chevron-left");//replacing the iocns class
			}
			else {
				closeBtn.classList.replace("bx-chevron-left","bx-chevron-right");//replacing the iocns class
			}
		}
	</script>"""


#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = """ <div id="mySidebar" class="collapsedSidebar">
		<a href="index.html" class="homeMobile"> """ + websiteData['Course Offering Title']+"""</a> <!--NAME-->
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
			
		<a href="overview.html">Calendar</a>"""

# Generate mobile sidebar buttons
for i in range(0,len(unitData)):
   mobileSidebar += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + unitData[i]['header'] + """</a>"""

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


# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

# Substitute settings unitData with appropriate variables 
result = templateString.safe_substitute(   
    sidebar = sidebarButtons,
    mobile = mobileSidebar
)


resultFile = open("generated/website/overview.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
unitTemplate.close()
