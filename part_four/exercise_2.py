'''
Please write a function named square, which prints out a square of characters, and takes two arguments. 
The first parameter specifies the length of the side of the square. 
The second parameter specifies the character used to draw the square.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. 
Please don't change anything in the line function.
'''

def line(integer, string):
    if string == '':
        print(integer*'*')
    else:
        string = string[0]
        print(integer*string)


def square(size, character):
     for i in range(size): 
        line(size, character)