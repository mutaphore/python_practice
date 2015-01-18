#!/usr/bin/env python

class Parent(object):

   def __init__(self):
      print "Hello from parent"

class Child(Parent):

   def __init_(self):
      super(Child, self).__init__()
      print "Hello from child"

son = Child()
