#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("UTF-8")

with open (sys.argv[1], 'r') as f:
    prot = f.read()
    prot.decode("UTF-8")
    for let in prot:
        print let
    f.closed
