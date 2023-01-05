'''
Please write a program which asks the user for a string and then prints out
a frame of * characters with the word in the centre. The width of the frame should be 30 characters. 
You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the
word in either of the two possible centre locations.
'''

word = input('Word: ')
blank = 28 - len(word)

if blank % 2 == 1:
    distance1 = (blank//2) + 1
    distance2 = blank//2
else:
    distance1 = blank//2
    distance2 = blank//2
distance1 = ' ' * distance1
distance2 = ' ' * distance2

print(30*'*')
print(f'*{distance1}{word}{distance2}*')
print(30*'*')
