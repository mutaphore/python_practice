# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

from collections import OrderedDict

ans = {}

words = raw_input("Enter a sentence: ").split()
unique_words = set(words)

for item in unique_words:
	ans[item] = words.count(item)

od = OrderedDict(sorted(ans.items(), key=lambda e:e[0]))

for item in od.items():
	print "%s:%d" % (item[0],item[1])