# discrete-math-for-cs.github.io
 Put instructions for how to build and how to deploy, 
 where to make edits.

 Weekly instructor workflow: edit .tex files by selecting snippets and adding custom text, then 
 update unit-settings.json paths with current files.

 JSON Settings files: 
 
 website-settings.json: contains Global Class Name, Course Offering Name, Feedback, Copyright Year, Copyright Name, and IncludeUngroupedSnippets keys.

    Global Class Name (str)- this name is the generic title of the class (i.e. Discrete Math for CS)

    Course Offering Name (str)- this name is specific to a certain university/term, used on unit and calendar overview sidebar menus 

    Feedback (str)- iframe embed html code for a feedback form for website function and user experience

    Copyright Year + Copyright Name (str)- copyright information

    IncludeUngroupedSnippets (boolean)- flag
        if true: all snippets present in notes/activity-snippets will be added to the end of topic/application compiled files (generated/notes/topic or /app)
        if false: snippets which are not included in any lesons/ .tex files will not be included in topic/application compiled files (generated/notes/topic or /app)

