# initialize coordinates (0, 0)
x = 0
y = 0

# Requests for INPUT (command string)
string = input("Enter a string:")
string = string.replace(" ", "")

# Creates a variable to store commands in a list
list = string.split(',')

# Cycles through each command
for i in range(len(list)):
	direction = list[i][0]
	direction = direction.lower()

	distance = list[i][1]

	# check if command = F
	if direction == 'f':		
		y += int(distance)		# increments y by distance

	# check if command = B
	elif direction == 'b':		
		y -= int(distance)		# decrements y by distance

	# check if command = R
	elif direction == 'r':		
		x += int(distance)		# increments x by distance

	# check if command = L
	elif direction == 'l':		
		x -= int(distance)		# decrements x by distance

print("Final coordinates are: " + "(" + str(x) + "," + str(y) + ")")

# Creates OUTPUT variable
dist_to_start = 0

# Add distance between starting and ending x coordinate
if x > 0:
	dist_to_start += x
elif x < 0:
	dist_to_start -= x

# Add distance between starting and ending y coordinate
if y > 0:
	dist_to_start += y
elif y < 0:
	dist_to_start -= y

print("Minimum distance to starting point is " + str(dist_to_start) + " units.")