#!/usr/local/bin/python

def double_char(str):
	temp = ""
	for ch in str:
		temp += 2 * ch
	return temp

def count_hi(str):
	return str.count("hi")
