#/usr/local/bin/python

#A. Sum Sort
#The letters A-Z are given the values 1-26, respectively. The value of a word is the sum of
#the values of the letters in it. Given a list of words composed entirely of uppercase letters,
#sort them in ascending order by their value. If there is a tie, arrange them lexicographically
#(i.e., alphabetically).
#Input
#The first line contains the number T (1  T  100) giving the number of test cases. The
#first line of each test case will contain the number n (1  n  100) giving the number of
#words. The following n lines will each contain a string of k uppercase letters (1  k  100).
#Output
#For each case, output the given words in sorted order, with one word one each line. There
#should be a blank line output between each test case.

import sys

class Word(object):
    
    def __init__(self, string):
        self.string = string
        self.total = reduce(lambda x, y: x + y, [ord(x) for x in self.string])

#T = int(sys.stdin.readline())
n = int(sys.stdin.readline())

words = []
for i in range(n):
   words.append(Word(sys.stdin.readline().strip())) 
# 2 pass sorting
words = sorted(words, cmp=lambda x, y: cmp(x.string, y.string))
words = sorted(words, cmp=lambda x, y: cmp(x.total, y.total))
for word in words:
    print word.string
