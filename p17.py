# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

net = 0

while True:
	line = raw_input("> ").split()
	if not line:
		break;
		
	amt = int(line[1])
	if line[0] == 'D':
		net += amt
	elif line[0] == 'W':
		net -= amt

print net
