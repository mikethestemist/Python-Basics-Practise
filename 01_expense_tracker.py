# expense tracker

import json, random

FILENAME = 'expenses.json'

def add_expense(amount: float, item: str):
    try:
        file = open(FILENAME, 'r') 
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        data = []

    data.append({'id': random.randint(int(1e4),int(1e5)), 'amount': amount, 'item': item})

    file = open(FILENAME, 'w')
    json.dump(data, file)
    file.close()

def loop_add_expense():
    try: 
        amount = float(input('Enter amount ($) [e.g. -> 25.75, 400] \n: ')).strip()
    except ValueError:
        print('Enter numbers only.')
        loop_add_expense()
    
    item = input('Enter item [e.g. -> shoes]\n: ').title().strip()
    add_expense(amount, item)

    print(f'\nYou spent {amount} on {item}.')

    repeat = True
    while repeat:
        repeat_response = input('\nDo you want to enter another expense entry? (y/n) \n: ').lower().strip()
        repeat = False

        if repeat_response == 'y':
            print('')
            loop_add_expense()
        elif repeat_response == 'n':
            programme_flow()
        else:
            print('Invalid input. Enter "y" for yes and "n" for no.')
            repeat = True

def view_expenses():
    try: 
        file = open(FILENAME, 'r')
        data = json.load(file)
        for expense in data:
            print(expense)
        file.close()
    except FileNotFoundError:
        print('\nYou have not inputed any entry in your expenses')
    finally:
        programme_flow()

def clear_all_entries():
    confirm_clear = input('\nAre you sure you want to erase all entries? (y/n)\n: ').lower().strip()
    if confirm_clear == 'y':
        try: 
            file = open(FILENAME, 'w')
            json.dump([], file)
            file.close()
            print('Cleared successfully.')
            programme_flow()    
        except FileNotFoundError:
            print('Expenses database didn\'t exist initially.')
    elif confirm_clear == 'n':
        print('Clear request declined.')
        programme_flow()
    else: 
        print('Invalid input, enter "y" for yes and "n" for no.')
        clear_all_entries()
    

def programme_flow():
    prompt = input('\nEnter "add" to add expense entrys, "view" to see all entries, or "clear" to erase all entries.\n: ').lower().strip()
    if prompt == 'add':
        loop_add_expense()
    elif prompt == 'view':
        view_expenses()
    elif prompt == 'clear':
        clear_all_entries()
    else: 
        print('\nSorry, invalid input. Enter "add" or "view".')
        programme_flow()

print('Welcome to this terminal based expense tracker.')
programme_flow()



