'''
Please write a program which asks the user to type in values and adds them to a list. 
After each addition, the list is printed out in two different ways:

In the order the items were added
Ordered from smallest to greatest

The program exits when the user types in 0.
'''

list_1 = []

while True:
    num = int(input('New item: '))
    if num == 0:
        print('Bye!')
        break
    else:
        list_1.append(num)
        print(f'The list now: {list_1}')
        print(f'The list in order: {sorted(list_1)}')