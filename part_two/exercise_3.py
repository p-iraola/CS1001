'''
Please write a program which asks for two integer numbers. 
The program should then print out whichever is greater. 
If the numbers are equal, the program should print a different message.
'''

num1 = int(input('Please type in the first number: '))
num2 = int(input('Please type in the second number: '))

if num1 > num2:
    print(f'The greater number was: {num1}')
elif num2 > num1:
    print(f'The greater number was: {num2}')
else:
    print('The numbers are equal!')