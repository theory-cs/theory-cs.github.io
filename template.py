from string import Template
import json
from user_functions import *

# Template for each webpage view and Generated for the result file name
template = ["index_template", "feedback_template", "overview_calendar_template", "overview_outcome_template", "overview_application_template", "assignment_template", "course_info_template", "office_hours_template"]
generated = ["index", "feedback", "overview_calendar", "overview_outcome", "overview_application", "assignments", "courseInfo", "office_hours"]

# Substitute template 
for i in range (len(template)):
    substitute_template(template[i], generated[i])