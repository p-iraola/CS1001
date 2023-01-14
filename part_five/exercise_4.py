'''
Please write a function named column_correct(sudoku: list, column_no: int), 
which takes a two-dimensional array representing a sudoku grid, 
and an integer referring to a single column, as its arguments. 
Columns are indexed from 0.

The function should return True or False, 
depending on whether the column is filled in correctly, 
that is, whether it contains each of the numbers 1 to 9 at most once.
'''

def column_correct(sudoku: list, column_no: int):
    check = []
    for i in range(len(sudoku)):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] not in check:
            check.append(sudoku[i][column_no])
        elif sudoku[i][column_no] in check:
            return False
    
    return True