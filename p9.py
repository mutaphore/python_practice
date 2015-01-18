# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

from string import *

lines = []
print "Enter sequence of lines: "

while True:
	line = raw_input("> ")
	if not line:
		break
	lines.append(line.upper())

print lines