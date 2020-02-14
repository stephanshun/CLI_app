## CLI_app

The program allows the user to input a string of commands that will tell a virtual robot to move forwards, backwards, left or right. Each command in the string has to be in the format <command><number> with commas separating each command. For example, 'F1,R1,B3,L2' instructs the robot to move 1 unit forwards, 1 unit to the right, 3 units backwards and 2 units to the left. The program uses a 2D coordinate to map the robots location from the starting point. The minimum distance between the robot and the starting point will be outputted (e.g. 'F1, R1' will output a distance of 2).

# Executing the program
Open your command line terminal and enter the program's directory. The program's file is named 'app.py'. Run the command 'python3 app.py' to start the program.

# Testing
Open your command line terminal and enter the program's directory. The program has a unit testing file named 'test_functions.py' that tests the functions used in the app.py program. Run the command 'python3 test_functions.py' to run the unit tests.

# Additional information
There are two areas of code that may seem ineffficient or unneccesary. 

The first occurs in line 13 and 14 of app.py where black spaces are removed and the string is split by commas. This was done to help organise the commands into a list, and also accomodates user input with spaces after/before commas.

The second is the use of start_x, start_y and end_x, end_y in app.py and the function find_distance(). This was to provide extensiblity to the code. For example, if instead the program can take in multiple string inputs, the starting coordinates will not always be (0,0). Having two different variables labels the difference and is necessary in the find_distance() function to calculate the minimum distance between two points (including starting coordinates that is not (0,0).
