# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence = raw_input("Enter a sentence: ")

d = {
	"UPPER": 0,
	"LOWER": 0
}

for ch in sentence:
	if ch.isupper():
		d["UPPER"] += 1
	elif ch.islower():
		d["LOWER"] += 1

print "UPPER CASE %d" % d["UPPER"]
print "LOWER CASE %d" % d["LOWER"]