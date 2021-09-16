#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import codecs

with codecs.open (sys.argv[1], 'r', 'UTF-8') as f:
    prot = f.read()
    prot.decode()
    for let in prot:
        print let
    f.closed
