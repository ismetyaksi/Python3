#!/usr/bin/python3

# VCF v2.1 VCARDs to CSV

# ruler
#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8

import quopri

def write_line(file_output1, line_output1):
    file_output1.write(line_output1 + "\n")

    return()

def analyze_parm(ap_line_input):                    # extract unique properties (elements) in a list
    if (ap_line_input == ""):
        global n_null_line

        n_null_line += 1
        print("1 >>> Null line after photo", n_null_line)
    else:
        ap_list1 = split_parm(ap_line_input)

        ap_len1 = len(ap_list1[0])
        ap_parm2 = ap_list1[0] + ap_line_input[ap_len1: ap_len1 + 1]
        ap_len2 = len(ap_parm2)

        ap_found = False
        
        for ix1, ap_list2 in enumerate(list_parm):
            if (ap_list2[0] == ap_parm2):
                ap_found = True

                list_parm[ix1][2] += 1              # increment existing property count

                break

        if (not ap_found):
            list_parm.append([ap_parm2, ap_len2, 1]) # add property in the list as 1st occurrence

    return()

def split_parm(line_input3):                        # convert property in a line to a list 
    sp_p1 = line_input3.replace(":", " ")
    sp_p1 =       sp_p1.replace(";", " ")

    return(sp_p1.split())
    
# Pass #1 Append Continuations

delim1 = "\t"

prev_line = ""
n_parm_line = 0
n_continuation = 0
n_cont_quo_pri = 0
n_out_line = 0
n_null_line = 0
list_parm = []

# Open Output File

filename2 = "zz1_no_continuations.txt"

file_output1 = open(filename2, "w")                 # a APPEND, w OUTPUT

with open("aa_vcards_vcf.txt", "r") as file_input1:
    for line_input1 in file_input1:
        line_input2 = line_input1.rstrip("\n")      # REMOVE NEWLINE
        if (line_input2[:1] == " "):                # 1/3 continuation line
            n_continuation += 1

            prev_line += line_input2[1:]            # append continuation line
            
        elif (line_input2[:1] == "="):              # 2/3 continuation line with quoted printable
            n_cont_quo_pri += 1

            prev_line += line_input2[1:]            # append continuation line with quoted printable

        else:                                       # 3/3 parameter line
            n_parm_line += 1

            if (prev_line != ""):                   # process prev parameter line
                write_line(file_output1, prev_line) # write prev line
                n_out_line += 1

            prev_line = line_input2                 # set prev line

            analyze_parm(line_input2)               # analyze parameter

if (prev_line != ""):                               # process last parameter line
    write_line(file_output1, prev_line)             # write prev line
    n_out_line += 1

print()                                             # list pass # 1 totals
print("1 >>> Parameter lines ...................", n_parm_line)
print("1 >>> Continuation lines ................", n_continuation)
print("1 >>> Continuation lines with quo pri ...", n_cont_quo_pri)
print("1 >>> Total input lines .................", n_parm_line + n_continuation + n_cont_quo_pri)
print("1 >>> Total output lines ................", n_out_line)

print()
print("1 >>> Parameters")                           # list unique properties
print()

for ix1, ap_list2 in enumerate(list_parm):
    print("1 >>>", ap_list2)

list_parm.sort()                                    # list properties in alphabetical order

print()
print("1 >>> Sorted Parameters")
print()

for ix1, ap_list2 in enumerate(list_parm):
    print(ap_list2[0])

# Close Output File

file_output1.close()

# Pass #2 analyze VCARD parameters and tabulate

n_quoted_pri = 0
n_utf8 = 0
n_max_tel = 0

n_vcard = 0

str_email = ""                                          # clear parameteres
str_note = ""
str_org = ""
str_photo = ""
str_title = ""
str_fn = ""
list_tel = []

parm_charset = "CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"
len_parm_charset = len(parm_charset)

# Open Output File

file_output1 = open("zz2_vcard_analysis.txt", "w")      # a APPEND, w OUTPUT
file_output2 = open("zz3_contacts&phones.txt", "w")     # a APPEND, w OUTPUT

list_input4 = ["#vcard", "email", "note", "org", "photo", "title", "fn", "tel1", "tel2"]
line_input4 = delim1.join(list_input4)    
write_line(file_output2, line_input4)                   # write header

with open(filename2, "r") as file_input1:
    for line_input1 in file_input1:
        line_input2 = line_input1.rstrip("\n")          # REMOVE NEWLINE

        ix_quoted_pri = line_input2.find(parm_charset)
        
        if (ix_quoted_pri > -1):                        # convert quoted printable to utf8
            n_quoted_pri += 1
            str_input1 = line_input2[:ix_quoted_pri]
            str_input2 = line_input2[ix_quoted_pri+len_parm_charset:]
            str_input2 = quopri.decodestring(str_input2)
            str_input2 = str_input2.decode("UTF-8")
            line_input3 = str_input1 + str_input2
        else:
            n_utf8 += 1
            line_input3 = line_input2
        
        write_line(file_output1, line_input3)           # write line

        if   (line_input3[:3] == "END"):
            n_vcard += 1
            
            list_input4 = [str(n_vcard), str_email, str_note, str_org, str_photo, str_title, str_fn]

            n_max_tel = max(n_max_tel, len(list_tel))
                            
            for ix_tel in list_tel:
                list_input4.append(ix_tel)

            line_input4 = delim1.join(list_input4)    
            write_line(file_output2, line_input4)       # write line

            str_email = ""                              # clear parameteres
            str_note = ""
            str_org = ""
            str_photo = ""
            str_title = ""
            str_fn = ""
            list_tel = []

        elif (line_input3[:3] == "TEL"):            # phone property
            list_parm1 = split_parm(line_input3)

            if (len(list_parm1) == 3):              # extract phone number
                str_tel1 = list_parm1[2]

                if (str_tel1[:3] == "+90"):         # strip country code for turkey
                    str_tel1 = str_tel1[2:]

                if (str_tel1 not in list_tel):      # add phone number if not duplicate
                    list_tel.append(str_tel1)
            
        elif (line_input3[:2] == "FN"):             # process full name 
            str_fn = line_input3[3:]
            
        elif (line_input3[:5] == "EMAIL"):
            list_parm1 = split_parm(line_input3)
            str_email = list_parm1[2]
            
        elif (line_input3[:4] == "NOTE"):
            str_note = line_input3[5:]
            
        elif (line_input3[:3] == "ORG"):
            str_org = line_input3[4:]
            
        elif (line_input3[:5] == "PHOTO"):          # mention if photo exists
            str_photo = "photo exists"
            
        elif (line_input3[:5] == "TITLE"):
            str_title = line_input3[6:]
            
        else:
            pass
            
# Close Output File

file_output1.close()
file_output2.close()

print()                                             # list pass #2 totals
print("1 >>> # quoted printable ................", n_quoted_pri)
print("1 >>> # utf-8 ...........................", n_utf8)
print("1 >>> # total lines .....................", n_quoted_pri + n_utf8)
print("1 >>> # max tel .........................", n_max_tel)
print("1 >>> # vcards ..........................", n_vcard)

exit()

exit()
