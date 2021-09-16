#!/usr/bin/env python3
# -*- coding: cp852 -*-

import sys

NULL_CHAR = chr(0)
def write_report(report):
	with open ('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

write_report(NULL_CHAR*2+chr(51)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(52)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(47)+NULL_CHAR*5)
# with open (sys.argv[1], 'r') as f:
#    prot = f.read().decode('utf-8')
#    for let in prot:
#        print let
#    f.closed
