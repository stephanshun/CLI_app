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

		# raise ValueError if any other commands are inputted
		else: raise ValueError("Invalid command in string, available commands are 'F', 'B', 'R', 'L'.")

	return x, y


# find_distance - Calculates the distance between a set of starting coordinates and a set of final coordinates
def find_distance(start_x, start_y, end_x, end_y):
	# Initializes return value for distance between starting and ending point
	dist_to_start = 0

	# Adds distance between starting and ending x coordinate
	if start_x > end_x:
		dist_to_start += (start_x-end_x)
	elif start_x < end_x:
		dist_to_start += (end_x-start_x)

	# Adds distance between starting and ending y coordinate
	if start_y > end_y:
		dist_to_start += (start_y-end_y)
	elif start_y < end_y:
		dist_to_start += (end_y-start_y)

	return dist_to_start