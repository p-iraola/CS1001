'''
Please write a program which asks the user for a floating point number
and then prints out the integer part and the decimal part separately. 

You can assume the number given by the user is always greater than zero.
'''

num = input('Please type in a number: ')

decimal = num.find('.')

print(f'Integer part: {num[0:decimal]}')
print(f'Decimal part: 0{num[decimal:len(num)]}')