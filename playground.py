#!/usr/bin/env python3
# -*- coding: cp2352 -*-

import sys

with open (sys.argv[1], 'r') as f:
    prot = f.read()
    for let in prot:
        print let
    f.closed
