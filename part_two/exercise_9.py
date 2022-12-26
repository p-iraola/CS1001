'''
Please write a program which asks the user for integer numbers.

If the number is below zero, the program should print out the message "Invalid number".

If the number is above zero, the program should print out the square root of the number 
using the Python sqrt function.

In either case, the program should then ask for another number.

If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

Below you'll find a reminder of how the sqrt function is used. Remember to import it
in the beginning of the program.
'''

from math import sqrt

while True:
    num = int(input('Please type in a number: '))
    if num == 0:
        print('Exiting...')
        break
    if num < 0:
        print('Invalid number')
    elif num > 0:
        print(sqrt(num))