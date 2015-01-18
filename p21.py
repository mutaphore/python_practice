# Question
# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current 
# position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

pos = {
	"x": 0, 
	"y": 0
}

while True:

	line = raw_input("> ")
	if not line:
		break

	direction, steps = line.split()
	if direction == "UP":
		pos["y"] += int(steps)
	elif direction == "DOWN":
		pos["y"] -= int(steps)
	elif direction == "LEFT":
		pos["x"] -= int(steps)
	elif direction == "RIGHT":
		pos["x"] += int(steps)

print int(round((pos["x"]**2 + pos["y"]**2)**0.5))