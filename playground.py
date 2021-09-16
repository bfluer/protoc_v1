#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import sys

with open (sys.argv[1], 'r') as f:
    prot = f.read()
    for let in prot:
        print let
    f.closed
