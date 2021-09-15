from string import Template
import json


websiteData = json.loads(open("website-settings.json").read())

def sidebar(view):
	view = view.lower()
	
	sidebarButtons = """ <div class="sidebar"><div class="logo-details"><div class="logo_name"><i class='bx bx-home-smile'></i> </div> """

	if("application" in view):
		titleHref = "index.html"
		titleName = websiteData['Global Class Name']
		overviewHref = "overviewApplication.html"
		overviewName = "Overview"
		overviewIcon = "'bx bxs-shapes'"

	if("topic" in view):
		titleHref = "index.html"
		titleName = websiteData['Global Class Name']
		overviewHref = "overviewTopic.html"
		overviewName = "Overview"
		overviewIcon = "'bx bxs-shapes'"

	if("unit" in view):
		titleHref = "courseInfo.html"
		titleName = websiteData['Course Offering Title']
		overviewHref = "overviewCalendar.html"
		overviewName = "Calendar"
		overviewIcon = "'bx bx-calendar'"

	sidebarButtons += """ <a href=""" + titleHref +""" class="logo_name">""" + titleName + """</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
			</div>
			
			<ul class="nav-list">
			
			<li>
				<a href=""" + overviewHref + """ aria-label="Go to""" + overviewName + """\">
					<i class=""" + overviewIcon + """></i>
					<span class="links_name">""" + overviewName + """</span>
				</a>
				<span class="tooltip">""" + overviewName + """</span>
			</li>"""
			
	if("application" in view):
		appData = json.loads(open("applications.json").read())
		
		for i in appData:
			file = i.replace(" ", "-").lower()+".html"
			sidebarButtons += "<li>"
			sidebarButtons += """<a href= \"""" + file + """\" aria-label="Go to """ + i + """ ">"""
			sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + appData[i]['Icon'] + """</p></i>"""
			sidebarButtons += """<span class="links_name"> """ + i + """</span>"""
			sidebarButtons += "</a>"
			sidebarButtons += """<span class="tooltip"> """ + i + """</span>"""
			sidebarButtons += "</li>\n"

	if("topic" in view):
		outcomeData = json.loads(open("outcomes.json").read())
        
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

	if ("unit" in view):
		unitData = json.loads(open("unit-settings.json").read())
		
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
	
	return sidebarButtons



def mobileSidebar(view):

	if("application" in view):
		titleHref = "index.html"
		titleName = websiteData['Global Class Name']
		overviewHref = "overviewApplication.html"
		overviewName = "Overview"

	if("topic" in view):
		titleHref = "index.html"
		titleName = websiteData['Global Class Name']
		overviewHref = "overviewTopic.html"
		overviewName = "Overview"

	if("unit" in view):
		titleHref = "overviewCalendar.html"
		titleName = websiteData['Course Offering Title']
		overviewHref = "overviewCalendar.html"
		overviewName = "Calendar"


	mobileSidebarButtons = """ <div id="mySidebar" class="collapsedSidebar">
			<a href=""" + titleHref + """ class="homeMobile"> """ + titleName +"""</a> <!--NAME-->
		  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
			<a href=""" + overviewHref + """>""" + overviewName + """</a>"""

	if("application" in view):
		appData = json.loads(open("applications.json").read())
		for i in appData:
			file = i.replace(" ", "-").lower()+".html"
			mobileSidebarButtons += """<a href= \"""" + file + """\">""" + i + """</a>\n"""

	if("topic" in view):
		outcomeData = json.loads(open("outcomes.json").read())
		for big in outcomeData:
			for med in outcomeData[big]['Children']:
				#only put icon in sidebar of 2nd tier topics that have children 
				if(bool(outcomeData[big]['Children'][med]['Children'])):
					mobileSidebarButtons += """<a href= \"""" + outcomeData[big]['Children'][med]['file'] + """\"">""" + med + """</a>"""


	if("unit" in view):
		unitData = json.loads(open("unit-settings.json").read())
		for i in range(0,len(unitData)):
			mobileSidebarButtons += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + unitData[i]['header'] + """</a>"""


	mobileSidebarButtons += """ </div>

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

	return mobileSidebarButtons



    