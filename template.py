from string import Template
import json
from user_functions import *

template = ["index_template", "feedback_template", "overview_calendar_template", "overview_topic_template", "overview_application_template", "assignment_template"]
generated = ["index", "feedback", "overviewCalendar", "overview_topic", "overview_application", "assignments"]

for i in range (len(template)):
    substitute_template(template[i], generated[i])