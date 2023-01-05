'''
Please write a program which asks the user for a number. 
The program then prints out all integer numbers greater than zero but smaller than the input.
'''

num = int(input('Upper limit: '))
x = 1
while x < num:
    print(x)
    x += 1