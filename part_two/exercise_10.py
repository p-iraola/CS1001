'''
Please write a program which asks the user for a password. 
The program should then ask the user to type in the password again. 
If the user types in something else than the first password, 
the program should keep on asking until the user types the first password again correctly.
'''

p1 = input('Password: ')
while True:
    p2 = input('Repeart password: ')
    if p2 == p1:
        print('User account created!')
        break
    else:
        print('They do not match!')
