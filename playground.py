#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys

with open (sys.argv[1], 'r') as f:
    print f.read()
    f.closed
