'''
Please write a function named chessboard, which prints out a chessboard 
made out of ones and zeroes. 
The function takes an integer argument, which specifies the length of the side of the board. 
'''

def chessboard(size):
    row_one = ''
    row_two = ''
    total_rows = 0
    while len(row_one) < size:
        row_one += '1'
        row_two += '0'
        if len(row_one) < size:
            row_one += '0'
            row_two += '1'
    while total_rows < size:
        print(row_one)
        total_rows += 1
        if total_rows < size:
            print(row_two)
            total_rows += 1