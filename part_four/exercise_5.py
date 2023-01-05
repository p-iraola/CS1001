'''
Please write a program which first asks the user for the number of items to be added. 
Then the program should ask for the given number of values, one by one, and adds them to a list 
in the order they were typed in. Finally, the list is printed out.
'''

num_items = int(input("How many items: "))
items = []
for i in range(num_items):
    item = int(input(f"Item {i + 1}: "))
    items.append(item)
print(items)
    