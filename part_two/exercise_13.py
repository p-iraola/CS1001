'''
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Change the program so that the loop ends also if the user types in the same word twice.
'''

story = ''
double_check = ''
while True:
    word = input('Please type in a word: ')
    if word == 'end' or word == double_check:
        print(story)
        break
    else:
        story += word + ' '
        double_check = word