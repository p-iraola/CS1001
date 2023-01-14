'''
Please write a program which works as a simply diary. 
The diary entries should be saved in the file diary.txt. 
When the program is executed, it should first read any entries already in the file.
'''

print('1 - add an entry, 2 - read entries, 0 = quit')
question = int(input('Function: '))

while True:
    if question == 1:
        entry = input('Diary entry: ')
        with open('diary.txt', 'a') as f:
            f.write(f'{entry}\n')
        print('Diary saved')
        print('1 - add an entry, 2 - read entries, 0 = quit')
        question = int(input('Function: '))

    elif question == 2:
        with open('diary.txt') as f:
            for line in f:
                line = line.replace('\n', '')
                print(line)
        print('1 - add an entry, 2 - read entries, 0 = quit')
        question = int(input('Function: '))
    
    elif question == 0:
        print('Bye now!')
        break