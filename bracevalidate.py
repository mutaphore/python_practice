#!/usr/local/bin/python

def braceValidate(s):
    stk = []

    for c in s:
        if c == '{':
            stk.append(1)
        elif c == '(':
            stk.append(2)
        elif c == '[':
            stk.append(3)
        elif c == '}':
            if stk.pop(-1) != 1:
                return False
        elif c == ')':
            if stk.pop(-1) != 2:
                return False
        elif c == ']':
            if stk.pop(-1) != 3:
                return False
    if stk:
        return False

    return True

if __name__ == '__main__':
    if braceValidate("{ [ }"):
        print "Match"
    else:
        print "Mismatched brackets"
