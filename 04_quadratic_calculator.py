from math import sqrt

def get_a():
    try: 
        a = float(input('Enter value for a: ')).strip()
        return a
    except ValueError:
        print('Invalid input. Enter a number only')
        get_a()

def get_b():
    try: 
        b = float(input('Enter value for b: ')).strip()
        return b
    except ValueError:
        print('Invalid input. Enter a number only')
        get_b()

def get_c():
    try: 
        c = float(input('Enter value for c: ')).strip()
        return c
    except ValueError:
        print('Invalid input. Enter a number only')
        get_c()

def repeat():
    response = input('\nDo you want to enter another set of values? (y/n): ').strip().lower()
    if response == 'y':
        calculate_x()
    elif response == 'n':
        print('Thanks for using this calculator.')
    else:
        print('Invalid input. Enter y for yes and n for no.')
        repeat()

def calculate_x():
    a = get_a()
    b = get_b()
    c = get_c()
    d = float(b ** 2 - 4 * a * c)
    try:
        num1 = round((-b + sqrt(d)) / 2 * a)
        num2 = round((-b - sqrt(d)) / 2 * a)
        print(f'\nx is both {num1} and {num1}')
    except ValueError:
        print('\nSorry, the values inputted gave an error in the calculation.')
        calculate_x()
    repeat()

print('Welcome to this quadratic calculator.')
print('\nThe equation goes: ax^2 + bx + c = 0.')
calculate_x()