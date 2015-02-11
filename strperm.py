#!/usr/local/bin/python

import sys

# Insert string c into string s at position index
def str_insert(s, c, index):
    if index == 0:
        return c + s
    elif index >= len(s):
        return s + c
    else:
        return s[:index] + c + s[index:]


# Recursively find permutations of a string
def perm(s):
    if len(s) > 1:
        perms = perm(s[:-1])
        new_perms = []
        for p in perms:
            for i in range(len(p)+1):
                new_perms.append(str_insert(p, s[-1], i))
        return new_perms
    else:
        return s


if __name__ == '__main__':
    s = raw_input("Enter a string to permute: ")
    perms = perm(s)
    print perms
    print "%d permutations" % len(perms)

#    a_b = []
#    for perm in perms:
#        if perm.index('b') > perm.index('a'):
#            a_b.append(perm)            
#    print "count %r \n%r" % (len(a_b), a_b)
#
#    a_c = []
#    for perm in a_b:
#        if perm.index('c') > perm.index('a'):
#            a_c.append(perm)
#    print "count %r \n%r" % (len(a_c), ",".join(a_c))
