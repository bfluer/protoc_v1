#!/usr/bin/env python3

import sys

NULL_CHAR = chr(0)

def write_report(report):
        with open ('/dev/hidg0', 'rb+') as fd:
                fd.write(report.encode())
with open(sys.argv[1]) as f:
        writingtext = f.readlines()
        writingtext =

scancodes_letters={
        'a' : 4,
        'b' : 5,
        'c' : 6,
        'd' : 7,
        'e' : 8,
        'f' : 9,
        'g' : 10,
        'h' : 11,
        'i' : 12,
        'j' : 13,
        'k' : 14,
        'l' : 15,
        'm' : 16,
        'n' : 17,
        'o' : 18,
        'p' : 19,
        'q' : 20,
        'r' : 21,
        's' : 22,
        't' : 23,
        'u' : 24,
        'v' : 25,
        'w' : 26,
        'x' : 27,
        'y' : 28,
        'z' : 29,
        ':' : 51,
        ' ' : 44,
        '/n' :40
}

for line in writingtext:
    for let in line:
        cod = scancodes_letters.get(let, 4)
        write_report(NULL_CHAR*2+chr(cod)+NULL_CHAR*5)
        write_report(NULL_CHAR*8)
