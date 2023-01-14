'''
Please write a function named read_input, 
which asks the user for input until the user types in an integer 
which falls within the bounds given as arguments to the function. 
The function should return the final valid integer value typed in by the user.
'''

def read_input(user_input, lower_num, upper_num):
    while True:
        try:
            num = input(user_input)
            num = int(num)
            if num > lower_num and num < upper_num:
                return num
        
        except ValueError:
            pass

        print(f'You must type in an integer between {lower_num} and {upper_num}')