'''
Please write a program which keeps asking the user for a PIN code until they type in the correct one, 
which is 4321. 
The program should then print out the number of times the user tried different codes.
'''

pin = 4321
tries = 0

while True:
    attempt = int(input('PIN: '))
    tries += 1
    if attempt == pin and tries == 1:
        print('Correct! It only took you one single attempt!')
        break
    elif attempt == pin:
        print(f'Correct! It took you {tries} attempts')
        break
    else:
        print('Wrong')