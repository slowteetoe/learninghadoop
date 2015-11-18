#!/usr/bin/env python
import sys

#
# Files will consist of either:
# Almost_News, 25
# Hourly_Show,30
# - or -
# Almost_News, ABC
# Hourly_Show, COM
# Hot_Cooking, FNT

# We'll just get rid of anything that isn't 'ABC'

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    k     = key_value[0]  #key is first item in list
    v   = key_value[1]   #value is 2nd item

    if v.isdigit(): # if it's the number of viewers, just output it
        print('%s\t%s' % (k, v) )
    else:   # otherwise we eliminate all shows that aren't on ABC
        if v == 'ABC':
            print('%s\t%s' % (k, v))
