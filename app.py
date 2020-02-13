from functions import *

# Requests for INPUT (command string)
string = input("Enter a string:\n")

# Intializes starting coordinates
x = 0
y = 0

print("Starting coordinates are: " + "(" + str(x) + "," + str(y) + ")")

# Converts command string into a list 
string = string.replace(" ", "")
list = string.split(',')

# Retrieves final coordinates
x, y = derive_coordinates(list, x, y)

print("Final coordinates are: " + "(" + str(x) + "," + str(y) + ")")

# Creates OUTPUT variable
output = find_distance(x, y)

print("Minimum distance to starting point is " + str(output) + " units.")