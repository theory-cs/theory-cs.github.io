from string import Template
import json
from userFunctions import *

template = ["index_template", "feedback_template", "overview_calendar_template", "overview_topic_template", "overview_application_template", "assignment_template"]
generated = ["index", "feedback", "overviewCalendar", "overviewTopic", "overviewApplication", "assignments"]

for i in range (len(template)):
    substitute_template(template[i], generated[i])