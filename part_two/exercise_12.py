'''
Please write a program which asks the user for a year, and prints out the next leap year.
'''

year1 = int(input('Year: '))
year2 = year1 + 1
while True:
    if year2 % 4 == 0:
        if year2 % 100 == 0:
            if year2 % 400 == 0:
                print(f'The next leap year after {year1} is {year2}')
                break
            else:
                year2 += 1
        else:
            print(f'The next leap year after {year1} is {year2}')
            break
    else:
        year2 += 1