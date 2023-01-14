'''
Please write two functions, named matrix_sum and matrix_max. 
Both go through the matrix in the file, 
and then return the sum of the elements or the element with the greatest value, 
as the names of the functions imply.

Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. 
'''

def read_data():
    all_nums = []
    with open('matrix.txt') as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(',')
            
            for i in line:
                all_nums.append(int(i))
    
    return all_nums

def matrix_sum():
    nums = read_data()
    total = 0
    for i in nums:
        total += i
    return total

def matrix_max():
    nums = read_data()
    return max(nums)

def row_sums():
    lines = []
    sums = []
    with open('matrix.txt') as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(',')
            lines.append(line)
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    
        sums.append(sum(lines[i]))

    return sums