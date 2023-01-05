'''
Please write a function named everything_reversed, 
which takes a list of strings as its argument. 
The function returns a new list with all of the items on the original list reversed. 
Also the order of items should be reversed on the new list.
'''

def everything_reversed(list):
    list = reversed(list)
    new_list = []
    for i in list:
        new_list.append(i[::-1])
    return new_list