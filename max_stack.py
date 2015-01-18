#!/usr/local/bin/python

import os
import sys

class MaxStack:
    stack = []
    size = 10
    max_val = 0
    max_stack = []
    def __init__(self, size):
        self.size = size
    def push(self, val):
        self.stack.append(val)
        if val > self.max_val:
            self.max_val = val
            self.max_stack.append(val)
    def pop(self):
        val = self.stack.pop()
        if val == self.max_val:
            self.max_stack.pop()
            self.max_val = self.max_stack[-1]
        return val
    def get_max(self):
        return self.max_val
    def print_stk(self):
        for e in self.stack:
            print e,
        print ""

if __name__ == '__main__':
    stk = MaxStack(20)
    stk.push(3)
    stk.push(1)
    stk.push(4)
    stk.push(2)
    stk.push(6)
    stk.print_stk()
    print stk.get_max()
    stk.pop()
    print stk.get_max()
    stk.pop()
    print stk.get_max()
    stk.pop()
    print stk.get_max()
    stk.pop()
    print stk.get_max()
