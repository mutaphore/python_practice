# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

nums = raw_input("Enter number(s): ").split(' ')
ans = []

for num in nums:
	factorial = 1
	for i in range(1, int(num) + 1):
		factorial = factorial * i

	ans.append(str(factorial))

print ','.join(ans)