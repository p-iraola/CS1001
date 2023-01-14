'''
Please write a function named read_fruits, 
which reads the file and returns a dictionary based on the contents. 
In the dictionary, the name of the fruit should be the key, 
and the value should be its price. Prices should be of type float.
'''

def read_fruits():
    dictionary = {}
    with open('fruits.csv') as f:
        for line in f:
            line = line.replace('\n', '')
            diff_parts = line.split(';')
            fruit = diff_parts[0]
            price = float(diff_parts[1])
            dictionary[fruit] = price
    return dictionary