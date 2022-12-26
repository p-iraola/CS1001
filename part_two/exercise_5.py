'''
The table below outlines the grade boundaries on a certain university course. 
Please write a program which asks for the amount of points received
and then prints out the grade attained according to the table.
'''

pts = int(input('How many points [0-100]: '))
if pts < 0 or pts > 100:
    print('Grade: impossible!')
elif pts > 0 and pts < 49:
    print('Grade: fail')
elif pts >= 50 and pts <= 59:
    print('Grade: 1')
elif pts >= 60 and pts <= 69:
    print('Grade: 2')
elif pts >= 70 and pts <= 79:
    print('Grade: 3')
elif pts >= 80 and pts <= 89:
    print('Grade: 4')
elif pts >= 90 and pts <= 100:
    print('Grade: 5')