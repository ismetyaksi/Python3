readme_py_xml_v1.0_parser

## XML V1.0 Parser

Parser is useful to understand the structure of a new XML before importing

Program parses an XML v1.0 document and creates 3 output files:

1. File with one tag per line. Start tag and end tag are in different lines.
2. CSV file containing element name, minimum level, maximum level, # of start tags, # of end tags. Level is incremented for each start tag, decremented for each end tag.
3. CSV file with path name and # of occurrences. Path name is all higher levels of element tags.

Please see below notes about program.

* I used Ubuntu 24.10, Python 3.12.7 with tcl/tk 8.6.14 and integrated IDLE.
* Note #1: I used a Microsoft MSINFO file as input. This file is normally NFO type. My input file was utf-16 type file. I converted it to utf-8 by opening with Libreoffice Writer and saving after choosing encoding.
* Note #2: CDATA is a self closing tag.
* Note #3: The input file was read in entirely, not line by line. NewLine characters are removed. To keep the design simple, the username <SYSTEM> with separators inside was changed to SYS-USER.
* Note #4: Root end tag (</MsInfo> in our case) is not handled.

