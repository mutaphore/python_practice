# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

nums = raw_input("Enter comma-separated numbers: ").split(',')
ans = [str(int(num) * int(num)) for num in nums if int(num) % 2 != 0]

# ans = []
# for num in nums:
# 	temp = int(num)
# 	if temp % 2 != 0:
# 		ans.append(str(temp * temp))

print ",".join(ans)
