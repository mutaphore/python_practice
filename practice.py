#!/usr/local/bin/python

def double_char(str):
	temp = ""
	for ch in str:
		temp += 2 * ch
	return temp

def count_hi(str):
	return str.count("hi")


def rule_sequence(s, rules):

    if s and rules:
        return rule_sequence(rules[0](s), rules[1:])


def pluck(keys):
    def plucker(obj):
        ret = {}
        map(lambda x : ret[x] = obj[x], keys)
        return ret
            
    return plucker
        
