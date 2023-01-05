'''
Please write a function named all_the_longest, 
which takes a list of strings as its argument. 
The function should return a new list containing the longest string in the original list. 
If more than one are equally long, the function should return all of the longest strings.
'''

def all_the_longest(list):
    new_list = []
    final_list = []
    long = list[0]
    for i in list:
        if len(i) >= len(long):
            long = i
            new_list.append(i)
    for i in new_list:
        if len(i) == len(long):
            final_list.append(i)
            
    return final_list