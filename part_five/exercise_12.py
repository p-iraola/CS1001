'''
In this series of exercises you will create a simple student database.

First write a function named add_student, 
which adds a new student to the database. 
Also write a preliminary version of the function print_student, 
which prints out the information of a single student.


Please write a function named add_course, 
which adds a completed course to the information of a specific student in the database. 
The course data is a tuple consisting of the name of the course and the grade:

Courses with grade 0 should be ignored when adding course information. 
Additionally, if the course is already in the database in that specific student's information, 
the grade recorded in the database should never be lowered if the course is repeated.

Please write a function named summary, 
which prints out a summary based on all the information stored in the database.
'''

def add_student(students, student):
    students[student] = []

def add_course(students, student, course):
    if student in students and course[1] > 0:
        for i, j in enumerate(students[student]):
            if j[0] == course[0]:
                if j[1] < course[1]:
                    students[student][i] = course
                return
        students[student].append((course))

def print_student(students, student):
    if student in students:
        if len(students[student]) > 0:
            print(f'{student}:')
            print(f' {len(students[student])} completed courses:')
            
            total = 0
            for course, grade in students[student]:
                total += grade
                print(f'  {course} {grade}')
            print(f' average grade {total/len(students[student])} ')
        
        else:
            print(f'{student}:')
            print(' no completed courses')

    else:
        print(f'{student}: no such person in the database')

def summary(students):
    print(f'students {len(students)}')
    
    classes = 0
    student = ''
    for i in students: 
        if len(students[i]) > classes:
            classes = len(students[i])
            student = i
    print(f'most courses completed {classes} {student}')
    
    check = 0
    student = ''
    for i in students:
        total = 0
        for j in students[i]:
            total += j[1]
        total = total/len(students[i])
        
        if total > check:
            check = total
            student = i
    print(f'best average grade {check} {student}')