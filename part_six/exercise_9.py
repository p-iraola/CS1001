'''
Please write a program which functions as a dictionary. 
The user can type in new entries or look for existing entries.
'''

while True:
    print('1- Add word, 2 - Search, 3 - Quit')
    function = input('Function: ')

    if function == '3':
        print('Bye!')
        break

    elif function == '1': 
        finnish = input('Word in Finnish: ')
        english = input('Word in English: ')

        with open('dictionary.txt', 'a') as f:
            f.write(f'{finnish},{english}\n')

        print('Dictionary entry added')

    elif function == '2':
        search_term = input('Search term: ')
        
        words = []
        with open('dictionary.txt') as f:
            for line in f:
                line = line.strip()
                parts = line.split(',')
                words.append(parts)

        for word in words:
            check = any(search_term in sub for sub in word)
            if check == True:
                print(f'{word[0]} - {word[1]}')