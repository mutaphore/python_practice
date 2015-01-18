# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

nums = range(2000, 3201)
ans = []

for i in nums:
	if (i % 7 == 0) and (i % 5 != 0):
		ans.append(str(i))

print ','.join(ans)