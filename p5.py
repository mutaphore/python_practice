class prompter(object):

	def __init__(self):
		self.string = None

	def getString(self):
		self.string = raw_input("Enter a string: ")

	def printString(self):
		print self.string

myPrompter = prompter()
myPrompter.getString()
myPrompter.printString()