### VCF v2.1 VCARD to CSV

It is useful for organizing and cleaning mobile phone contacts lists.

1. Program converts VCF v2.1 VCARDs listing to CSV

2. All properties are read and continuations are appended to first line

3. **Unique property names** and counts are collected in a list

4. On the first pass a **temporary file** is created.

5. On the second pass temporary file is read and VCF related information is collected and inserted to a text file 

###Following is **IDLE** output of the program

1 >>> Null line after photo 1

1 >>> Null line after photo 2

1 >>> Null line after photo 3

1 >>> Null line after photo 4

1 >>> Null line after photo 5

1 >>> Null line after photo 6

1 >>> Parameter lines ................... 2426

1 >>> Continuation lines ................ 477

1 >>> Continuation lines with quo pri ... 27

1 >>> Total input lines ................. 2930

1 >>> Total output lines ................ 2420

1 >>> Parameters

1 >>> ['BEGIN:', 6, 351]

1 >>> ['VERSION:', 8, 351]

1 >>> ['N:', 2, 149]

1 >>> ['FN:', 3, 149]

1 >>> ['TEL;', 4, 612]

1 >>> ['END:', 4, 351]

1 >>> ['N;', 2, 201]

1 >>> ['FN;', 3, 201]

1 >>> ['EMAIL;', 6, 3]

1 >>> ['ORG;', 4, 39]

1 >>> ['ORG:', 4, 4]

1 >>> ['PHOTO;', 6, 6]

1 >>> ['NOTE:', 5, 1]

1 >>> ['TITLE:', 6, 1]

1 >>> ['TITLE;', 6, 1]

1 >>> Sorted Parameters

BEGIN:

EMAIL;

END:

FN:

FN;

N:

N;

NOTE:

ORG:

ORG;

PHOTO;

TEL;

TITLE:

TITLE;

VERSION:

1 >>> # quoted printable ................ 442

1 >>> # utf-8 ........................... 1978

1 >>> # total lines ..................... 2420

1 >>> # max tel ......................... 2

1 >>> # vcards .......................... 351

