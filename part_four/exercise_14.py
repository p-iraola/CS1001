'''
In this exercise you will write a program for printing out grade statistics for a university course.
The program asks the user for results from different students on the course. 
These include exam points and numbers of exercises completed. 
The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. 
The number of exercises completed is an integer between 0 and 100.

The program kees asking for input until the user types in an empty line. 
You may assume all lines contain valid input, 
which means that there are two integers on each line, or the line is empty.

And example of how the data is typed in:

Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed:
Statistics:

When the user types in an empty line, the program prints out statistics. They are formulated as follows:

The exercises completed are converted into exercise points, 
so that completing at least 10% of the exercises grants one point, 
20% grants two points, and so forth. 
Completing all 100 exercises grants 10 exercise points. 
The number of exercise points granted is an integer value, rounded down.

The grade for the course is determined based on the following table:

exam points + exercise points	grade
0–14	0 (i.e. fail)
15–17	1
18–20	2
21–23	3
24–27	4
28–30	5
There is also an exam cutoff threshold. 
If a student received less than 10 points from the exam, 
they automatically fail the course, regardless of their total number of points.

With the example input from above the program would print out the following statistics:

Sample output
Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *
Floating point numbers should be printed out with one decimal precision.
'''

def main():
    scores = enter_points()
   
    scores = convert_to_int(scores)
    
    scores = convert_exercise_points(scores)

    total_points = calculate_total_score(scores)
    
    grades = calculate_grade(scores)
    
    percentage = calculate_pass_percentage(grades)

    print('Statistics:')
    print(f'Points average: {sum(total_points)/len(total_points):.1f}')
    print(f'Pass percentage: {percentage:.1f}')
    print('Grade distribution: ')
    print(f"5: {grades.count(5)*'*'}")
    print(f"4: {grades.count(4)*'*'}")
    print(f"3: {grades.count(3)*'*'}")
    print(f"2: {grades.count(2)*'*'}")
    print(f"1: {grades.count(1)*'*'}")
    print(f"0: {grades.count(0)*'*'}")
    

def enter_points():
    scores = []
    while True:
        points = input('Exam points and exercises completed: ')
        
        if points == '':
            break
        elif points != '':
            scores.append(points.split())
    return scores


def convert_to_int(scores):
    return [[int(i) for i in inner] for inner in scores]

def convert_exercise_points(scores):
    for i in scores:
        i[1] = i[1]//10
    return(scores)

def calculate_total_score(scores):
    new_scores = []
    for i in scores:
        total = sum(i)
        new_scores.append(total)
    return new_scores


def calculate_grade(scores):
    grades = []
    for i in scores:
        if i[0] < 10:
            grades.append(0)
        elif i[0] + i[1] < 14:
            grades.append(0)
        elif i[0] + i[1] >= 15 and i[0] + i[1] <= 17:
            grades.append(1)
        elif i[0] + i[1] >= 18 and i[0] + i[1] <= 20:
            grades.append(2)
        elif i[0] + i[1] >= 21 and i[0] + i[1] <= 23:
            grades.append(3)
        elif i[0] + i[1] >= 24 and i[0] + i[1] <= 27:
            grades.append(4)
        elif i[0] + i[1] >= 28:
            grades.append(5)

    return grades

def calculate_pass_percentage(grades):
    percentage = 0
    for i in grades:
        if i > 0:
            percentage += 1

    percentage = percentage/len(grades)
    return percentage*100

main()