'''
Please write a program which asks the user for a positive integer number. 
The program then prints out a list of multiplication operations until 
both operands reach the number given by the user.
'''

num = int(input('Number: '))

a = 1

while a <= num:
    b = 1
    while b < num:
        print(f'{a} x {b} = {a*b}')
        b += 1
    print(f'{a} x {b} = {a*b}')
    a += 1