'''
Please write a program which finds the second occurrence of a substring. 
If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. 
For example, in the string aaaa the second occurrence of the substring aa is at index 2.
'''

text = input('Please type in a string: ')
substring = input('Please type in a substring: ')
index = 0
occurences = []

while index < len(text):
    index = text.find(substring, index)
    if index == -1:
        break
    occurences.append(index)
    index += len(substring)

if len(occurences) > 1:
    print(f'The second occurrence of the substring is at index {occurences[1]}.')
else:
    print('The substring does not occur twice in the string.')