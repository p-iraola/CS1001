'''
Please write a function named no_vowels, which takes a string argument. 
The function returns a new string, which should be the same as the original but with all vowels removed.

You can assume the string will contain only characters from the lowercase English alphabet a...z.
'''

def no_vowels(string):
    vowels = ['a','e','i','o','u']
    for i in string:
        if i in vowels:
            string = string.replace(i, '')
    return string