# basic statistics
import math

def mean(entered_list): 
    sum = 0
    for number in entered_list: 
        sum += number
    length = len(entered_list)
    
    result = sum / length
    print(result)

def median(entered_list):
    entered_list = sorted(entered_list)
    length = len(entered_list)
    if length % 2 == 1:
        index = (length - 1) / 2
        result = entered_list[int(index)]
        print(result)
    else:
        index_1 = (length / 2) - 1
        index_2 = (length / 2)
        first_num = entered_list[int(index_1)]
        second_num = entered_list[int(index_2)]
        
        print([first_num, second_num])
        mean([first_num, second_num])

def mode(entered_list):
    frequency = {}
    for item in entered_list:
        frequency[item] = frequency.get(item, 0) + 1

        max_count = max(frequency.values())
        modes = []
        
    for key, count in frequency.items():
        if count == max_count:
            modes.append(key)

    if len(modes) == 1:
        print(modes[0]) 
    else: print(modes) 

def clean_data(values):
        cleaned_inputs = []
        for num in values:
            if not num == '':
                cleaned_inputs.append(float(num))
        return cleaned_inputs

def refined_values():
    try: 
        entered_values = input('\nEnter numbers only and separate them with a comma. \n[e.g.: 3, 3, 4, 5, 4, 6]\n: ').split(',')
        entered_values = clean_data(entered_values)
        return entered_values
    except ValueError:
        print('One or all of the values you entered is not a number')
        refined_values()
    except:
        print('Incorrect syntax. Please emulate examples: comma and space to separate values.')


def calc_mean():
    values = refined_values()
    mean(values)
    programme_flow()

def calc_median():
    values = refined_values()
    median(values)
    programme_flow()

def calc_mode():
    values = refined_values()
    mode(values)
    programme_flow()


def programme_flow():
    stat_function = input('\nEnter "mean" to calculate the mean, "median" to calculate the median, or "mode" to calculate the mode \n: ').lower().strip()
    if stat_function == 'mean':
        calc_mean()
    elif stat_function == 'median':
        calc_median()
    elif stat_function == 'mode' :
        calc_mode()
    else: 
        print('Invalid input, enter either "mean", "median", or "mode".')
        programme_flow()
        
print('Welcome to this terminal based statistical calculator')    
programme_flow()