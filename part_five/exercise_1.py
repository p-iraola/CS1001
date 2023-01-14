'''
Please write a function named longest(strings: list), 
which takes a list of strings as its argument. 
The function finds and returns the longest string in the list. 
You may assume there is always a single longest string in the list.
'''

def longest(strings: list):
    length = []
    for i in strings:
        length.append(len(i))
    
    combined = zip(length,strings)

    longest = max(combined)

    return(longest[1])