# discrete-math-for-cs.github.io
 Put instructions for how to build and how to deploy, 
 where to make edits.

 Weekly instructor workflow: edit .tex files by selecting snippets and adding custom text, then 
 update unit-settings.json paths with current files.

 JSON Settings files: 
 
 website-settings.json: contains Global Class Name, Course Offering Name, Feedback, Copyright Year, Copyright Name, and IncludeUngroupedSnippets keys.

    Global Class Name (str): this name is the generic title of the class (i.e. Discrete Math for CS)

    Course Offering Name (str): this name is specific to a certain university/term, used on unit and calendar overview sidebar menus 

    Feedback (str): iframe embed html code for a feedback form for website function and user experience

    Copyright Year + Copyright Name (str): copyright information

    IncludeUngroupedSnippets (boolean): flag
        if true: all snippets present in notes/activity-snippets will be added to the end of topic/application compiled files (generated/notes/topic or /app)
        if false: snippets which are not included in any lesons/ .tex files will not be included in topic/application compiled files (generated/notes/topic or /app)

 outcomes.json: contains first, second, and third tier learning outcomes of Discrete Maths (specifically CSE 20) and the attributes of each outcome
    
    First tier outcome (top-level key) (str) : these are program/theory outcomes and are displayed as box titles on overviewTopic.html
        Description (str): description of the first tier outcome
        Icon (str): html code of the icon featured beside the first tier outcome on the overviewTopic.html (i.e. a paper airplane)
    
    Second tier outcome (child of top-level key) (str): these are the sidebar menu options and are individual web pages
        Description (str): description of the second tier outcome
        Icon (str): one-two letter acronym for second tier outcome, shown on sidebar menu
        file (str): html file which features the webpage for the second tier outcome (format - "x.html")
    
    Third tier outcome (child of second tier outcome): these are the collapsible menu options on each second tier webpage, each has its own pdf of compiled snippets
        Description (str): description of the third tier outcome
        filename (str): pdf file which displays compiled snippets in which third tier outcome is featured 
            (format - do not include .pdf file extension)




        
