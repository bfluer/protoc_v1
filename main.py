##!/usr/bin/env python3

import subprocess

NULL_CHAR = chr(0)
def write_report(report):
	with open ('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

while(1):
    try:
        write_report(NULL_CHAR)
    except:
        continue
    subprocess.call(['sh', '/home/pi/SANWriter/protoc_v1/start.sh'])
    break
