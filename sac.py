#!/usr/bin/env python

import sys
import getopt

def usage():
    print "Usage:"
    print "  ./sac.py [-s] -i <annual_interest> -p <# months> -v <value> [-t <tax>]"
    print 
    print "  -s : simple interest"


try:
    opts, args = getopt.getopt(sys.argv[1:], "si:p:v:t:")
except:
    usage()
    sys.exit(1)

rate = -1
value = -1
period = -1
tax = 0
simple = False
total = 0

for k, v in opts:
    if k == "-i":
        rate = int(v)
    elif k == "-p":
        period = int(v)
    elif k == "-v":
        value = int(v)
    elif k == "-t":
        tax = int(v)
    elif k == "-s":
        simple = True

if (rate == -1 or period == -1 or value == -1):
    usage()
    sys.exit(1)

rate = rate/100.

if (simple == False):
    rate = (1 + rate)**(1/12.) - 1
else:
    rate = rate/12.

amort = 1.0*value/period

for i in range(1, period + 1):
    payment = amort + value*rate + tax
    total = total + payment
    value = value - amort
    print '%3d - R$ %.2f' % (i, payment)

print "Total paid: R$ %.2f" % total
