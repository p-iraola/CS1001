'''
Please write a program which asks the user for a string. 
The program then prints out the input string in reversed order, from end to beginning. 
Each character should be on a separate line.
'''

string = input('Please type in a string: ')
for letter in string[::-1]:
    print(letter)