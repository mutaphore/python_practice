# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

ans = []

for num in range(1000, 3001):
	
	num_str = str(num)
	is_ok = True

	for char in num_str:
		if int(char) % 2:
			is_ok = False
			break
	if is_ok:
		ans.append(str(num))

print ",".join(ans)