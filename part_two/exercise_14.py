'''
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in zero.

After reading in the numbers the program should print out how many numbers were typed in. 
The zero at the end should not be included in the count.

The program should also print out the sum of all the numbers typed in. 
The zero at the end should not be included in the calculation.

The program should also print out the mean of the numbers. 
The zero at the end should not be included in the calculation. 
You may assume the user will always type in at least one valid non-zero number.

The program should also print out statistics on how many of the numbers were positive 
and how many were negative. The zero at the end should not be included in the calculation.
'''

num_list = []
pos = 0
neg = 0

print('Please type in integer numbers. Type in 0 to finish.')
while True:
    num = int(input('Please type in numbers: '))
    if num == 0:
        print(f'Numbers typed in {len(num_list)}')
        print(f'The sum of the numbers is {sum(num_list)}')
        print(f'The mean of the numbers is {sum(num_list) / len(num_list)}')
        print(f'Positive numbers {pos}')
        print(f'Negative numbers {neg}')
        break
    else:
        num_list.append(num)
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
