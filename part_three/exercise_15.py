'''
Please write a function named squared, which takes a string argument 
and an integer argument, and prints out a square of characters 
as specified by the examples below.
'''

def squared(string, integer):
    word = string * (integer**2)
    
    for i in range(integer):
        print(word[0:integer])
        word = word[integer:]