#!/bin/python

# Script name: lotto.py
# Script date: 2016-08-21
# Script author: Dominik Szynk
# Script version: 1

import random
import os

os.system('clear')

def drawsQuantity():
	is_valid = 0
	while not is_valid:
		try:
			draw_qty = int(raw_input('\v\v\tHow many draws? '))
			if draw_qty == 0:
				is_valid = 0
				print("Try again!")
			else:
				is_valid = 1
		except e:
			print ("'%s' is not a number!." % e.args[0].split(": ")[1])
	return draw_qty

def numberQuantity():
	is_valid = 0
	while not is_valid:
		try:
			numbers_qty = int(raw_input('\v\v\tHow many numbers to draw from? '))
			if numbers_qty == 0:
				is_valid = 0
				print("Try again!")
			else:
				is_valid = 1
		except e:
			print ("'%s' is not a number!." % e.args[0].split(": ")[1])
	return numbers_qty

def drawNumbersQuantity():
	is_valid = 0
	while not is_valid:
		try:
			draw_numbers_qty = int(raw_input('\v\v\tHow many numbers to draw? '))
			if draw_numbers_qty == 0:
				is_valid = 0
				print("Try again!")
			else:
				is_valid = 1
		except e:
			print ("'%s' is not a number!." % e.args[0].split(": ")[1])
	return draw_numbers_qty

newDrawsQty = drawsQuantity()
newDrawNumbersQty = drawNumbersQuantity()
newNumberQty = numberQuantity()

for draw in range(0, newDrawsQty) :
	print("")
	print("Draw number - %d" % (draw+1))
	print("--------------------")
	for x in range(0,newDrawNumbersQty):
		lotto_no = random.randrange(1,newNumberQty,2)
    		print("Number %d = %d" %(x+1,lotto_no))
