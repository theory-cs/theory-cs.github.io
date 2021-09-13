from string import Template
import json
  

# returns unit-settings JSON file as a dictionary
appData = json.loads(open("applications.json").read())
websiteData = json.loads(open("website-settings.json").read())

#Sidebar top with title of course offering
sidebarButtons = """<div class="sidebar">
		<div class="logo-details">
		  
		    <div class="logo_name"><i class='bx bx-home-smile'></i> </div>
			<a href="index.html" class="logo_name">""" + websiteData['Global Class Name']+"""</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
		</div>

		<ul class="nav-list">
			
			<li>
				<a href="overviewApplication.html" aria-label="Go to Overview">
					<i class='bx bx-list-ul'></i>
					<span class="links_name">Overview</span>
				</a>
				<span class="tooltip">Overview</span>
			</li>"""

#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
for i in appData:
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= \"""" +appData[i]['file'] + """\" aria-label="Go to """ + i + """">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + appData[i]['Icon'] + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + i + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + i + """</span>"""
    sidebarButtons += "</li>\n"


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
		<a href="index.html" class="homeMobile"> """ + websiteData['Global Class Name']+"""</a> <!--NAME-->
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
        <a href="overviewApplication.html">Overview</a>
		"""



#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
for i in appData:
    mobileSidebar += """<a href= \"""" + appData[i]['file'] + """">""" + i + """</a>"""


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


boxString = """<div class="box"> \n"""
#big for loop begin
for i in appData:
    boxString += """<h2> <i style= "font-size: 75%;" class='bx bxs-chevron-right-square'></i> <a href= \"""" + appData[i]['file'] + """\" style="color: #182B49; text-decoration: none; font-size: 75%; font-weight: normal;" >""" + i + """</a></h2>"""

boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewApplicationTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings appData with appropriate variables 
result = templateString.safe_substitute(
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewApplication.html", "w")
resultFile.write(result)
resultFile.close()

unitTemplate.close()
