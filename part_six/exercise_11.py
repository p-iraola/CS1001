'''
The file lottery_numbers.csv containts winning lottery numbers in the following format:

week 1;5,7,11,13,23,24,30
week 2;9,13,14,24,34,35,37

Please write a function named filter_incorrect(), 
which creates a file called correct_numbers.csv. 
The file should contain only those lines from the original file which are in the correct format.
'''

def filter_incorrect():
    weeks_nums = []
    correct_weeks = []
    correct_both = []
    final_list = []
    
    with open('lottery_numbers.csv') as f:
        for line in f:
            line = line.strip()
            parts = line.split(';')
            weeks_nums.append(parts)
            for i in range(1,len(weeks_nums)):
                if parts[0] == f'week {str(i)}':
                    correct_weeks.append(parts)
                    nums = parts[1].split(',')
                    try:
                        count = 0
                        for num in nums:
                            if int(num) >= 1 and int(num) <= 39:
                                count += 1
                    except ValueError:
                        pass
                    if count == 7:
                        correct_both.append(parts)
                        if parts in correct_both:
                            final_list.append(line)

    with open('correct_numbers.csv', 'w') as f:
        f.writelines('\n'.join(final_list))