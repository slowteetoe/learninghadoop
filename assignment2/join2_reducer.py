#!/usr/bin/env python
import sys

# not much to this, keep track of the total, if you see a new key without seeing 'ABC', just ignore that key
show = ""
total = 0
saw_network = False

for line in sys.stdin:
    line = line.strip()
    kv = line.split('\t')
    this_show = kv[0]
    this_value = kv[1]
    if show != this_show:
        if saw_network == True:
            print('%s %s' % (show, total))
        # now reset fields, keeping in mind that this could be the network identifier
        show = this_show
        if this_value.isdigit():
            total = int(this_value)
            saw_network = False
        else:
            total = 0
            saw_network = True
    else:
        # decide if the value is a network identifier or a total
        if this_value.isdigit():
            total += int(this_value)
        else:
            saw_network = True

# finally, at the end, output the last show (if we saw the network)
if saw_network:
    print('%s %s' % (show, total))
