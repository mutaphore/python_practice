# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

import string

num_letters = 0
num_digits = 0

sentence = raw_input("Enter a sentence: ")

for ch in sentence:
	if string.ascii_letters.find(ch) != -1:
		num_letters += 1
	elif string.digits.find(ch) != -1:
		num_digits += 1

print "LETTERS %d" % num_letters
print "DIGITS %d" % num_digits