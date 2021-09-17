from string import Template
import json
from userFunctions import *

template = ["indexTemplate", "feedbackTemplate", "overviewCalendarTemplate", "overviewTopicTemplate", "overviewApplicationTemplate", "assignment-template"]
generated = ["index", "feedback", "overviewCalendar", "overviewTopic", "overviewApplication", "assignments"]

for i in range (len(template)):
    substitute_template(template[i], generated[i])