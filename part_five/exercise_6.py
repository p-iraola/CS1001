'''
Please write a function named sudoku_grid_correct(sudoku: list), 
which takes a two-dimensional array representing a sudoku grid as its argument. 
The function should use the functions from the three previous exercises 
to determine whether the complete sudoku grid is filled in correctly. 
Copy the functions from the exercises above into your Python code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. 
If all contain each of the numbers 1 to 9 at most once, 
the function returns True. 
If a single one is filled in incorrectly, the function returns False.

The image of a sudoku grid above these exercises has the nine blocks 
within the grid indicated with thicker borders. 
These are the blocks the function should check, and they begin at the indexes 
(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

'''

def row_correct(sudoku: list, row_no: int):
    check = []
    for i in sudoku[row_no]:
        if i > 0 and i not in check:
            check.append(i)
        elif i in check:
            return False
    
    return True

def column_correct(sudoku: list, column_no: int):
    check = []
    for i in range(len(sudoku)):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] not in check:
            check.append(sudoku[i][column_no])
        elif sudoku[i][column_no] in check:
            return False
    
    return True

def block_correct(sudoku:list, row_no: int, column_no: int):
    check = []
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            if sudoku[i][j] > 0 and sudoku[i][j] not in check:
                check.append(sudoku[i][j])
            elif sudoku[i][j] in check:
                return False
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(0,7,3):
        if row_correct(sudoku,i) == False:
            row_test = False
            break
        else:
            row_test = True
    
    for i in range(0,7,3):
        if column_correct(sudoku,i) == False:
            column_test = False
            break
        else:
            column_test = True

    for i in range(0,7,3):
        if block_correct(sudoku,i,i) == False:
            block_test = False
            break
        else:
            block_test = True
    
    if row_test == True and column_test == True and block_test == True:
        return True
    else:
        return False