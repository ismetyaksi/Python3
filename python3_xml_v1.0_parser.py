#!/usr/bin/python3

# xml v1.0 parser

# ruler
#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8

def get_label(str1):
    str2 = str1.replace("</", "")
    str2 = str2.replace("<", "")
    str2 = str2.replace(">", " ")
    list1 = str2.split(" ")

    return list1[0]

def write_file(file1, str1):
    file1.write(str1 + "\n")

delim1 = ";"
delim2 = ":"

filename_input1 = "aa1_xml_parser.xml"

filename_output1 = "zz1_tags.txt"
filename_output2 = "zz2_elements.txt"
filename_output3 = "zz3_paths.txt"

file_output1 = open(filename_output1, "w")		# a APPEND, w OUTPUT
file_output2 = open(filename_output2, "w")		# a APPEND, w OUTPUT
file_output3 = open(filename_output3, "w")		# a APPEND, w OUTPUT

with open(filename_input1, "r") as file_input1:
    str_input1 = file_input1.read()                                 # see note #3

print(">>>", len(str_input1))

str_input1 = str_input1.replace("\n", "")                           # see note #3
str_input1 = str_input1.replace("<SYSTEM>", "SYS-USER")             # see note #3

print(">>>", len(str_input1))

level1 = 0

list_labels = []

list_recent_path = []
list_paths = []

ix1 = 0
ix2 = str_input1.find("<", ix1+1)

print("1 >>>", ix2)

while ix2 != -1:            # extract each
    #print(">>>", ix2)
    str2 = str_input1[ix1:ix2]

    if (str2.count("<") > 1 or str2.count(">") > 1):
        print("2 >>> parsing error", str2)

    if (str2.find("<![CDATA[") == 0):       # see note #2
        #print("2 >>>", str2[:16])
        label1 = "CDATA"
        list_recent_path.append(label1)     # save paths for cdata 1/2
        start1 = True
        end1 = False
        # level does not change for cdata
    elif (str2.find("<!--") == 0):
        label1 = "comment"
        start1 = True
        end1 = False
        # level does not change for comment
    elif (str2.find("</") == 0):
        label1 = get_label(str2)
        list_recent_path.remove(label1)     # save paths
        level1 -= 1
        start1 = False
        end1 = True
        # end of a label 
    elif (str2 in ['<?xml version="1.0"?>']):   # , '<MsInfo>']):
        label1 = "instruction"
        start1 = True
        end1 = False
        # level does not change
    else:
        label1 = get_label(str2)
        list_recent_path.append(label1)     # save paths
        #print("4 >>>", list_recent_path)
        level1 += 1
        start1 = True
        end1 = False

    write_file(file_output1, str2)

# count statements

# list1 = [label1, level1 (min), level1 (max), 0 (#start), 0 (#end)]

    found1 = False
    
    for ix3, list_stmt in enumerate(list_labels):
        if (list_stmt[0] == label1):
            list1 = list_stmt

            #print("4 >>>", list1)
            
            list1[1] = min(level1, list1[1])
            list1[2] = max(level1, list1[2])
            if (start1):
                list1[3] += 1
            if (end1):
                list1[4] += 1

            list_labels[ix3] = list1

            found1 = True

            break
            
    if (not found1):
        list1 = [label1, level1, level1, 0, 0]

        if (start1):
            list1[3] += 1
        if (end1):
            list1[4] += 1

        list_labels.append(list1)

# end of count statements

# save paths

    str_recent_path = delim2.join(list_recent_path)
    if (str_recent_path != ""):
##        write_file(file_output3, str_recent_path)

        #found2 = False
        not_found2 = True
        
        for ix4, ix_path in enumerate(list_paths):
            if (ix_path[0] == str_recent_path):
                list1 = ix_path
                list1[1] += 1
                list_paths[ix4] = list1
                
                #found2 = True
                not_found2 = False

                break

        #if (not found2):
        if (not_found2):
            list_paths.append([str_recent_path, 1])

    if (label1 == "CDATA"):                 # see note #2
        #print("40 >>>", delim1.join(list_recent_path))        
        list_recent_path.remove(label1)     # save paths for cdata 2/2
        # level does not change for cdata

# end of save paths

    ix1 = ix2
    ix2 = str_input1.find("<", ix1+1)

# end of while ix2 != -1:            # extract each

print("30 >>>", len(list_labels), len(list_paths))

list_labels.sort()
list_paths.sort()

for ix1, list_stmt in enumerate(list_labels):
    list1 = list_stmt
    list1[1] = str(list1[1])
    list1[2] = str(list1[2])
    list1[3] = str(list1[3])
    list1[4] = str(list1[4])
    
    str3 = delim1.join(list1)
    write_file(file_output2, str3)

for ix1, ix_path in enumerate(list_paths):
    list1 = ix_path
    list1[1] = str(list1[1])
    str1 = delim1.join(list1)
    write_file(file_output3, str1)

file_output1.close()
file_output2.close()
file_output3.close()



exit()
