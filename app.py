from functions import *

# Requests for INPUT (command string)
string = input("Enter a string:\n")

# Intializes starting coordinates
start_x = 0
start_y = 0

print("Starting coordinates are: " + "(" + str(start_x) + "," + str(start_y) + ")")

# Converts command string into a list 
string = string.replace(" ", "")
list = string.split(',')

# Retrieves final coordinates
end_x, end_y = derive_coordinates(list, start_x, start_y)

print("Final coordinates are: " + "(" + str(end_x) + "," + str(end_y) + ")")

# Creates OUTPUT variable
output = find_distance(start_x, start_y, end_x, end_y)

print("Minimum distance to starting point is " + str(output) + " units.")