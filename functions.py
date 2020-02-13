# derive_coordinates - Calculates the final coordinates from a set of starting coordinates and a list of commands
def derive_coordinates(list, x, y):
	# Cycles through each command in the list
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

	return x, y

# find_distance - Calculates the distance between the starting coordinates (0, 0) and a set of final coordinates
def find_distance(x, y):
	# Initializes return value for distance between starting and ending point
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

	return dist_to_start