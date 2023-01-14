'''
This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.

Each row contains the information for a single student. 
The number of exercises completed, the number of exercise points awarded, 
the number of exam points awarded, the total number of points awarded, 
and the grade are all displayed in tidy columns. 

The width of the column for the name should be 30 characters, 
while the other columns should be 10 characters wide.
'''

student_info = input('Students: ')
exercise_data = input('Exercises: ')
exam_data = input('Exams: ')

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

exams = {}
with open(exam_data) as f:
    for line in f:
        parts = line.split(';')
        if parts[0] == 'id':
            continue

        exams[parts[0]] = sum([int(i) for i in parts[1:]])

print(f'{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}')
for key, value in students.items():
    if key in exercises:
        exercise_percentage = sum(exercises[key])/40
        final_score = int(exercise_percentage*10) + exams[key]
        
        result = 0
        if final_score <= 14:
            result = 0
        elif final_score >= 15 and final_score <= 17:
            result = 1
        elif final_score >= 18 and final_score <= 20:
            result = 2
        elif final_score >= 21 and final_score <= 23:
            result = 3
        elif final_score >= 24 and final_score <= 27:
            result = 4
        elif final_score >= 28:
            result = 5
        
        print(f'{students[key]:<30}{sum(exercises[key]):<10}{int(exercise_percentage*10):<10}{exams[key]:<10}{final_score:<10}{result:<10}')