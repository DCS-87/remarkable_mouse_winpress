#!/usr/bin/env python

# Generate file of evdev codes from libevdev that is importable on OSX/Windows.
# Only runs on Linux.

import libevdev
import pprint
pp = pprint.PrettyPrinter()

types = {}
codes = {}

for t in libevdev.types:
    types[t.value] = t.name
    codes[t.value] = {}
    for c in t.codes:
        codes[t.value][c.value] = c.name

with open('codes.py', 'w') as f:
    f.write('# generated by generate_codes.py\n')
    f.write('\ntypes= ')
    f.write(pp.pformat(types))
    f.write('\ncodes = ')
    f.write(pp.pformat(codes))
