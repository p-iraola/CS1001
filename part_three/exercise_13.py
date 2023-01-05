'''
Please write a function named hash_square(length), which takes an integer argument. 
The function prints out a square of hash characters, and the argument specifies 
the length of the side of the square.
'''

def hash_square(length):
    square = '#' * length
    for i in range(0,length):
        print(square)