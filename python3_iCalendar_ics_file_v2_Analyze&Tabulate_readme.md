### iCalendar ics file Analyze and Tabulate ###

The input file is read and the following operations are performed:

1. Continuation lines are appended to property lines and property lines without continuation are written to a temporary file.
2. property levels are maintained through BEGIN properties.
3. For visual convenience, the property lines are written to another temporary file by adding tab characters as much as their levels.
4. A unique properties list is prepared. The list includes **level** and **higher level property** information together with **number of occurrences**.
5. DTSTART, RRULE and SUMMARY properties were used while tabulating calendar events. ACTION, TRIGGER and DESCRIPTION alarm properties were also tabulated. Up to 4 alarms were tabulated for any event.

