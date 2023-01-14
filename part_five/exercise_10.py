'''
Please write an improved version of the phone book application. 
Each entry should now accommodate multiple phone numbers. 
The application should work otherwise exactly as above, 
but this time all numbers attached to a name should be printed.
'''

dictionary = {}
while True:
    command = input('command(1 search, 2 add, 3 quit): ')
    if command == '3':
        print('quitting...')
        break
    
    elif command == '2':
        name = input('name: ')
        if name not in dictionary:
            dictionary[name] = []
        number = input('number: ')
        dictionary[name].append(number)
        print('ok!')
    
    elif command == '1':
        name = input('name: ')
        if name in dictionary:
            for num in dictionary[name]:
                print(num)
        else:
            print('no number')