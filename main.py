# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Python does not have a const like javascript
# const will declared using all caps
# PI shall always be constant for use in formula
PI = 3.141592653589793

#prompts user for input
print('Please enter a number and press enter. Please repeat steps so the volume of a right circular cone can be done.')

# user inputs a number for radius
r = int(input())

# user inputs a number for height
h = int(input())

volume = (PI*r**2*h)/3
total_rounded = round(volume, 2)

print('The volume of this right circular cone is: ', total_rounded)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
