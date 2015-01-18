# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

a = raw_input("Enter a digit: ")
print int(a) + int(a + a) + int(a + a + a) + int(a + a + a + a)