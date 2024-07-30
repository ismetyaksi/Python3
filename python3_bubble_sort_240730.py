#!/usr/bin/python3

# bubble sort

# ruler
#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8

# sample output

# 0 >>> list size.. 1,000

# 1 >>> sort ascending

# 1 >>> #iterations 499,500
# 1 >>> #swaps..... 256,297

# 1 >>> sort ascending optimized

# 1 >>> #iterations 499,269
# 1 >>> #swaps..... 256,297

# 2 >>> sort descending

# 2 >>> #iterations 499,500
# 2 >>> #swaps..... 242,729

# 2 >>> sort descending optimized

# 2 >>> #iterations 497,609
# 2 >>> #swaps..... 242,729

import random

def init_list(len1, order1):
    random.seed(17)
    list1 = []
    for ix1 in range(len1):
        if (order1 == "ascending"):
            list1.append(ix1)
        elif (order1 == "descending"):
            list1.append(len1-ix1)
        else:
            list1.append(random.randint(len1, 2*len1))

    return(list1)

len_list = 1000

print("0 >>> list size..", f"{len_list:,d}")
print()

print("1 >>> sort ascending")
print()

list1 = init_list(len_list, "random")       # initialize list

n_iterations = 0
n_swaps = 0

for ix1 in range(len(list1)-1, 0, -1):      # iterate bottom up
    for ix2 in range(ix1):  
        #print("1 >>>", ix1, ix2)
        n_iterations += 1
        if (list1[ix2] > list1[ix2+1]):     # swap if greater than next item
            n_swaps += 1
            tmp1 = list1[ix2]
            list1[ix2] = list1[ix2+1]
            list1[ix2+1] = tmp1

if (list1 == sorted(list1)):                # test whether sort order correct or not
    print("1 >>> #iterations", f"{n_iterations:,d}")
    print("1 >>> #swaps.....", f"{n_swaps:,d}")
    print()
else:
    print("1 >>> sort order not ok!", list1)
    exit()

print("1 >>> sort ascending optimized")
print()

list1 = init_list(len_list, "random")       # initialize list

n_iterations = 0
n_swaps = 0

for ix1 in range(len(list1)-1, 0, -1):      # iterate bottom up
    any_swap = False                        # reset inner swap flag
    for ix2 in range(ix1):  
        #print("1 >>>", ix1, ix2)
        n_iterations += 1
        if (list1[ix2] > list1[ix2+1]):     # swap if greater than next item
            any_swap = True                 # set swap flag
            n_swaps += 1
            tmp1 = list1[ix2]
            list1[ix2] = list1[ix2+1]
            list1[ix2+1] = tmp1
    if (not any_swap):                      # If no inner swaps, already ordered, terminate
      break
if (list1 == sorted(list1)):                # test whether sort order correct or not
    print("1 >>> #iterations", f"{n_iterations:,d}")
    print("1 >>> #swaps.....", f"{n_swaps:,d}")
    print()
else:
    print("1 >>> sort order not ok!", list1)
    exit()

print("2 >>> sort descending")
print()

list1 = init_list(len_list, "random")       # initialize list

n_iterations = 0
n_swaps = 0

for ix1 in range(len(list1)-1, 0, -1):      # iterate bottom up
    for ix2 in range(ix1):  
        #print("1 >>>", ix1, ix2)
        n_iterations += 1
        if (list1[ix2] < list1[ix2+1]):     # swap if less than next item
            n_swaps += 1
            tmp1 = list1[ix2]
            list1[ix2] = list1[ix2+1]
            list1[ix2+1] = tmp1

if (list1 == sorted(list1, reverse=True)):  # test whether sort order correct or not
    print("2 >>> #iterations", f"{n_iterations:,d}")
    print("2 >>> #swaps.....", f"{n_swaps:,d}")
    print()
else:
    print("2 >>> sort order not ok!", list1)
    exit()

print("2 >>> sort descending optimized")
print()

list1 = init_list(len_list, "random")       # initialize list

n_iterations = 0
n_swaps = 0

for ix1 in range(len(list1)-1, 0, -1):      # iterate bottom up
    any_swap = False                        # reset inner swap flag
    for ix2 in range(ix1):  
        #print("1 >>>", ix1, ix2)
        n_iterations += 1
        if (list1[ix2] < list1[ix2+1]):     # swap if less than next item
            any_swap = True                 # set swap flag
            n_swaps += 1
            tmp1 = list1[ix2]
            list1[ix2] = list1[ix2+1]
            list1[ix2+1] = tmp1
    if (not any_swap):                      # If no inner swaps, already ordered, terminate
      break

if (list1 == sorted(list1, reverse=True)):  # test whether sort order correct or not
    print("2 >>> #iterations", f"{n_iterations:,d}")
    print("2 >>> #swaps.....", f"{n_swaps:,d}")
    print()
else:
    print("2 >>> sort order not ok!", list1)
    exit()
