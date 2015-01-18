# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

special_str = "$#@"
accepted = []

passwords = raw_input("Enter comma-separated passwords: ").split(',')

for password in passwords:

	lower = 0
	upper = 0
	digits = 0
	special = 0

	for char in password:

		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		elif char.isdigit():
			digits += 1
		elif special_str.find(char) != -1:
			special += 1

	if lower >= 1 and upper >= 1 and digits >= 1 and special >= 1 and len(password) in range(6,13):
		accepted.append(password)

print ",".join(accepted)



