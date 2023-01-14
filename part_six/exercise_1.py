'''
Please write a function named largest, which reads the file and returns the largest number in the file.

Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.
'''


def largest():
    with open('numbers.txt') as f:
        largest = 0
        for number in f:
            if int(number) > largest:
                largest = int(number)
    return(largest)