#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys

with open (sys.argv[1], 'r') as f:
    prot = f.read()
    prot.encode()
    for let in prot:
        print let
    f.closed
