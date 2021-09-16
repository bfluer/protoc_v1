#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from time import sleep

NULL_CHAR = chr(0)
def write_report(report):
	with open ('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
	writingtext = f.readlines().decode('utf-8')
	f.closed


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
	'y' : 29,
	'z' : 28,
	':' : 55,
	' ' : 44,
	'(' : 37,
	')' : 38,
	'/' : 36,
	'0' : 39,
	'1' : 30,
	'2' : 31,
	'3' : 32,
	'4' : 33,
	'5' : 34,
	'6' : 35,
	'7' : 36,
	'8' : 37,
	'9' : 38,
	'ä' : 52,
	'ö' : 51,
	'ü' : 47
}

sonderzeichen = {':','(',')','/'}

for line in writingtext:
	for let in line:
		write_report(NULL_CHAR*10)
		if let.isupper() or let in sonderzeichen:
			cod = scancodes_letters.get(let.lower(), 0)
			write_report(chr(32)+NULL_CHAR+chr(cod)+NULL_CHAR*5)
		else:
			cod = scancodes_letters.get(let, 0)
			write_report(NULL_CHAR*2+chr(cod)+NULL_CHAR*5)
	write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
	write_report(NULL_CHAR*8)
