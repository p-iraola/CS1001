'''
Please write a function named palindromes, 
which takes a string argument and returns True if the string is a palindrome. 
Palindromes are words which are spelled exactly the same backwards and forwards.
'''

def palindromes(word):
    if word == word[::-1]:
        return True
    else:
        return False

while True:
    palindrome = input('Please type in a palindrome: ') 
    if palindromes(palindrome) == True:
        print(f'{palindrome} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")