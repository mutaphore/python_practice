#!/usr/local/bin/python

def checkUnique():
    s = raw_input("Enter a string: ").upper()
    alpha = {}
    for ch in s:
        if not alpha.get(ord(ch)):
            alpha[ord(ch)] = 1
        else:
            return False
    return True

if __name__ == '__main__':
    if checkUnique():
        print "Unique"
    else:
        print "Not Unique"
