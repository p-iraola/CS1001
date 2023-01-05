'''
Please write a function named spruce, which takes one argument. 
The function prints out the text a spruce!, and the a spruce tree, 
the size of which is specified by the argument.

Calling spruce(3) should print out

a spruce!
  *
 ***
*****
  *

'''

def spruce(size):
    character = '*'
    length = 1
    i = 0
    white_length = size - 1
    white_space = white_length*' '
    first = white_space
    
    print('a spruce!')
    while i < size:
        print(f'{white_space}{character*length}')
        length += 2
        i += 1
        white_length -= 1
        white_space = white_length*' '
    print(f'{first}{character}')