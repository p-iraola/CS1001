'''
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. 
'''

string = input('Please type in a string: ')

interval = 0
while interval < len(string)+1:
    print(string[0:interval])
    interval += 1