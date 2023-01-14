'''
Please write a function named factorials(n: int), 
which returns the factorials of the numbers 1 to n in a dictionary. 
The number is the key, and the factorial of that number is the value mapped to it.
'''

def factorials(n: int):
    total = 1
    dictionary = {}
    for i in range(1,n+1):
        total *= i
        dictionary[i] = total
    
    return(dictionary)