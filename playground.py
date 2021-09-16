#!/usr/bin/env python3
# -*- coding: cp852 -*-

import sys

with open (sys.argv[1], 'r') as f:
    prot = f.read().decode('utf-8')
    for let in prot:
        print let
    f.closed
