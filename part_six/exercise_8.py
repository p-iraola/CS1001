'''
Please write a function named store_personal_data(person: tuple), 
which takes a tuple containing some identifying information as its argument.

The tuple contains the following elements:

Name (string)
Age (integer)
Height (float)

This should be processed and written into the file people.csv. 
The file may already contain some data; the new entry goes to the end of the file. 

The data should be written in the format:
name;age;height

Each entry should be on a separate line.
'''

def store_personal_data(person:tuple):
    person_stats = []
    with open('people.csv', 'w') as f:
        for i in person:
            person_stats.append(f'{i}')
        f.write(f'{person_stats[0]};{person_stats[1]};{person_stats[2]}\n')