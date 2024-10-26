#!/usr/bin/python3

# iCalendar v2.0 analyze and tabulate as csv

# useful for organizing mobile phone calendars

# ruler
#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8

# iCalendar wiki page -- https://en.wikipedia.org/wiki/ICalendar

# iCalendar 2016 specs -- https://icalendar.org/RFC-Specifications/iCalendar-RFC-7986/

def write_line(file1, line1):
    file1.write(line1 + "\n")
    
    return

def decompose_property(str_property):
    global n_level

    dp_str1 = str_property.replace(":", " ")
    dp_str1 =      dp_str1.replace(";", " ")

    dp_list1 = dp_str1.split()

    dp_len1 = len(dp_list1[0]) + 1                      # length of property name with colon/ semicolon

    dp_prop1 = str_property[:dp_len1]                   # name of property
    dp_prop2 = str_property[dp_len1:]                   # value of property

    dp_prev_prop = list_levels[n_level]                 # name of higher level property

    if (str_property[:5] == "BEGIN"):
        n_level += 1

        if (n_level == len(list_levels)):               # set new level
            list_levels.append(dp_prop2)
        elif (n_level < len(list_levels)):
            list_levels[n_level] = dp_prop2
        else:                                           # n_level > len(list_levels)
            print()
            print("1 *** Should not occur", n_level, len(list_levels))
            exit()

    dp_list_property = [n_level, dp_prev_prop, dp_prop1]    # set analysis list

    dp_str2 = str(n_level) + delim1 + dp_prev_prop + (delim1 * n_level) + str_property  # set leveled string

    write_line(file3_output, dp_str2)                   # write leveled string
    
    if (str_property[:3] == "END"):
        n_level -= 1

    found = False

    for dp_ix1, dp_list2 in enumerate(list_unique_properties): # search for analysis list in unique properties table
        if (dp_list_property == dp_list2[0]):
            found = True
            dp_list2[1] += 1                            # increment analysis list
            break

    if (not found):                                     # add analysis list if not found
        list_unique_properties.append([dp_list_property, 1, dp_prop2])
            
    return

def property2list(str_property):
    global begin_vevent
    global begin_valarm

    global vevent_dtstart
    global vevent_rrule
    global vevent_summary

    global list_vevent
    global list_valarm

    pl_str1 = str_property.replace(":", " ")
    pl_str1 =      pl_str1.replace(";", " ")

    pl_list1 = pl_str1.split()

    pl_len1 = len(pl_list1[0])

    pl_prop1 = str_property[:pl_len1]
    pl_prop2 = str_property[pl_len1 + 1:]

    pl_list_property = [pl_prop1, pl_prop2]

    if   (pl_list_property == ["BEGIN", "VEVENT"]):
        begin_vevent = True
    elif (pl_list_property == ["END", "VEVENT"]):
        begin_vevent = False
        list_vevent.append(vevent_dtstart)
        list_vevent.append(vevent_rrule)
        list_vevent.append(vevent_summary)
        list_vevent += list_valarm

        str_vevent = delim1.join(list_vevent)

        write_line(file4_output, str_vevent)

        vevent_dtstart = ""
        vevent_rrule = ""
        vevent_summary = ""

        list_vevent = []
        list_valarm = []
        
    elif (pl_list_property == ["BEGIN", "VALARM"]):
        begin_valarm = True
        
    elif (pl_list_property == ["END", "VALARM"]):
        begin_valarm = False
        
    elif (begin_vevent and pl_prop1 == "DTSTART"):
        vevent_dtstart = pl_prop2
        
    elif (begin_vevent and pl_prop1 == "RRULE"):
        vevent_rrule = pl_prop2
        
    elif (begin_vevent and pl_prop1 == "SUMMARY"):
        vevent_summary = pl_prop2
        
    elif (begin_valarm and pl_prop1 == "ACTION"):
        list_valarm.append(pl_prop2)
        
    elif (begin_valarm and pl_prop1 == "TRIGGER"):
        list_valarm.append(pl_prop2)

    elif (begin_valarm and pl_prop1 == "DESCRIPTION"):
        list_valarm.append(pl_prop2)

    else:
        pass
    
    return

delim1 = "\t"

str_mask1 = ""                                          
#str_mask1 = (2 * "*Masked") + "*"                       # masking sensitive data, comment out before using with your own data

if (str_mask1 != ""):
    print()
    print("1 >>> Masking in effect")
    print()
    
# open files

filename2 = "zz1_calendar_file2.txt"

file2_output = open(filename2, "w")                     # a APPEND, w OUTPUT

file3_output = open("zz2_leveled_properties.txt", "w")  # a APPEND, w OUTPUT

# pass #1 analyze input calendar file

n_property = 0
n_continuation = 0
n_property_written = 0
n_null_property = 0
longest_linesize = 0

str_property = ""

n_level = 0

list_levels = [""]

list_unique_properties = []

with open("aa_calendar_ics.txt", "r") as file_input1:
    for line_input1 in file_input1:
        line_input2 = line_input1.rstrip("\n")          # REMOVE NEWLINE

        if (line_input2[:1] == " "):                    # 1/2 continuation line
            n_continuation += 1

            line_input3 = line_input2
            
            if (str_mask1 != ""):
                line_input3 = str_mask1 

            print("1 >>> Continuation #", n_continuation, "--", line_input3)

            str_property += line_input2[1:]             # append continuation line

        else:                                           # 2/2 property line
            n_property += 1

            if (str_property == ""):                    # previous of 1st line is null
                n_null_property += 1
            else:
                write_line(file2_output, str_property)  # write previous property line
                n_property_written += 1

                decompose_property(str_property)        # decompose property

            str_property = line_input2                  # move proverty line to previous line

            longest_linesize = max(len(line_input2), longest_linesize)

if (str_property == ""):                                # at eof check with last property
    n_null_property += 1
else:
    write_line(file2_output, str_property)              # write last property
    n_property_written += 1

    decompose_property(str_property)                    # decompose property

print()
print("1 >>> # of property lines .......", n_property)
print("1 >>> # of continuation lines ...", n_continuation)
print("1 >>> # of total lines ..........", n_property + n_continuation)
print("1 >>> # of properties written ...", n_property_written)
print("1 >>> # of null lines skipped ...", n_null_property)

print("1 >>> Longest line size .........", longest_linesize)

print()
print("1 >>> List of properties")
print()

for ix1, list_property1 in enumerate(list_unique_properties):
    list_property2 = list_property1

    if (str_mask1 != ""):
        list_property2[2] = str_mask1
        
    print("1 >>>", ix1, list_property1)

list_unique_properties.sort()

print()
print("1 >>> List of sorted properties")
print()

for ix1, list_property1 in enumerate(list_unique_properties):
    print("1 >>>", str(ix1) + delim1 + str(list_property1[0][0]) + delim1 + list_property1[0][1] + delim1 + list_property1[0][2] + delim1 + str(list_property1[1]) + delim1 + list_property1[2][:32])

# close files

file2_output.close()
file3_output.close()

# open_files

file4_output = open("zz3_tabulated_calendar.txt", "w")  # a APPEND, w OUTPUT

# pass #2 tabulate calendar events to a csv file

list_vevent = []                                        # write header line
list_vevent.append("EVENT-DTSTART")
list_vevent.append("EVENT-RRULE")
list_vevent.append("EVENT-SUMMARY")

for ix1 in range(4):
    list_vevent.append("ALARM-ACTION-" + str(ix1 + 1))
    list_vevent.append("ALARM-TRIGGER-" + str(ix1 + 1))
    list_vevent.append("ALARM-DESCR-" + str(ix1 + 1))

str_vevent = delim1.join(list_vevent)
write_line(file4_output, str_vevent)

begin_vevent = False                                    # initialize variables
begin_valarm = False

vevent_dtstart = ""
vevent_rrule = ""
vevent_summary = ""

list_vevent = []
list_valarm = []

with open(filename2, "r") as file_input1:
    for line_input1 in file_input1:
        line_input2 = line_input1.rstrip("\n")          # REMOVE NEWLINE

        property2list(line_input2)

# close files

file4_output.close()

print()
print(">>> EOP")

exit()
exit()
