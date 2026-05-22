# a programme to calculate the simultaneous linear equation

def get_a():
    try: 
        a = float(input('Enter value for a: ').strip())
        return a
    except ValueError:
        print('\nInvalid input. Enter a number please.')
        get_a()
        
def get_b():
    try: 
        b = float(input('Enter value for b: ').strip())
        return b
    except ValueError:
        print('\nInvalid input. Enter a number please.')
        get_b()
        
def get_p():
    try: 
        p = float(input('Enter value for p: ').strip())
        return p
    except ValueError:
        print('\nInvalid input. Enter a number please.')
        get_p()
        
def get_c():
    try: 
        c = float(input('Enter value for c: ').strip())
        return c
    except ValueError:
        print('\nInvalid input. Enter a number please.')
        get_c()
        
def get_d():
    try: 
        d = float(input('Enter value for d: ').strip())
        return d
    except ValueError:
        print('\nInvalid input. Enter a number please.')
        get_d()
        
def get_q():
    try: 
        q = float(input('Enter value for q: ').strip())
        return q
    except ValueError:
        print('\nInvalid input. Enter a number please.')
        get_q()


def repeat():
    confirm_repeat = input('\nDo you want to enter a new set of values? (y/n): ').strip().lower()
    if confirm_repeat == 'y':
        programme_flow()
    elif confirm_repeat == 'n':
        print('Thanks for using this calculator.')
    else: 
        print('Sorry, invalid input. Enter y for yes and n for no.')
        repeat()


print('Welcome to this simultaneous linear equation calculator.')

def programme_flow():

    print('\nThis is the form of the equation.')
    print('ax + by = p')
    print('cx + dy = q')
    print('Enter appropraite values and it will generate the answers for x and y.')
    
    print('\nFirst equation: ax + by = p')
    a = get_a()
    b = get_b()
    p = get_p()

    print('\nSecond equation: cx + dy = q')
    c = get_c()
    d = get_d()
    q = get_q()

    print(f'\n{a}x + {b}y = {p}')
    print(f'{c}x + {d}y = {q}')

    try:
        x = (d * p - b * q) / (a * d -  c * b)
        y = (a * q - c * p) / (a * d -  c * b)
        print('\nHere are your answers.')

        print(f'x: {x}')
        print(f'y: {y}')
        repeat()
    except Exception:
        print('\nSorry, the values you inputted gave an error. Try using a correct question.')
        input('Press enter to continue. \n')
        programme_flow()


programme_flow()