'''
Please write a program which asks the user for the names of these two files, 
reads the files, and then prints out the total number of exercises completed by each student. 
'''
student_info = input('Student information: ')
exercise_data = input('Exercises completed: ')

students = {}
with open(student_info) as f:
    for line in f:
        parts = line.split(';')
        
        if parts[0] == 'id':
            continue
        
        students[parts[0]] = f'{parts[1].strip()} {parts[2].strip()}'


exercises = {}
with open(exercise_data) as f:
    for line in f:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        
        exercises[parts[0]] = [int(i) for i in parts[1:]]


for key, value in students.items():
    if key in exercises:
        print(f'{students[key]} {sum(exercises[key])}')
