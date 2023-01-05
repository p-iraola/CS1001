'''
Please write a program which asks the user to type in a number. 
The program then prints out all the positive integer values from 1 up to the number. 
However, the order of the numbers is changed so that each pair or numbers is flipped. 
That is, 2 comes before 1, 4 before 3 and so forth. 
'''

num = int(input("Please type in a number: "))

numbers = list(range(1, num + 1))

for i in range(0, len(numbers), 2):
    if i+1 < len(numbers):
        print(numbers[i+1])
        print(numbers[i])
    else:
        print(numbers[i])