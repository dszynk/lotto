#!/bin/python

# Script name: lotto.py
# Script date: 2016-08-21
# Script author: Dominik Szynk
# Script version: 1

import random

is_valid = 0
while not is_valid:
	try:
		draw_count = int(raw_input('Enter the number of draws: '))
		if draw_count == 0 :
			is_valid = 0
			print "Try again!"
		else:
			is_valid = 1
	except ValueError, e :
                print ("'%s' is not a number!." % e.args[0].split(": ")[1])

for draw in range(0, draw_count) :
	print
	print "Draw number - %d" % (draw+1)
	print "--------------------"
	for x in range(0,6):
		lotto_no = random.randrange(1,49,2)
    		print 'Number %d = %d' % (x+1, lotto_no)
