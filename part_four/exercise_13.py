'''
Given a list of integers, 
let's decide that two consecutive items in the list are neighbours if their difference is 1. 
So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, 
which looks for the longest series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], 
with a length of 4.
'''

def longest_series_of_neighbours(lst):
    max_length = 1
    current_length = 1
    for i in range(1, len(lst)):
        if abs(lst[i-1] - lst[i]) == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length