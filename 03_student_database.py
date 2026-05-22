# exercise: programme to collect students' data and store it as objects

# todo: show how many entries are in the data, delete entry/student
import json, random
def load_data():
    try: 
        with open('database.json', 'r') as database:
            data = json.load(database)
            database.close()
    except FileNotFoundError:
        data = []
    finally: 
        return data

class Student_Profile:
    def __init__(self, name: str, major: str, gpa: float, is_on_probation: bool):
        self.name = name 
        self.major = major 
        self.gpa = gpa 
        self.is_on_probation = is_on_probation


def input_data():
    to_repeat = True 
    while to_repeat:
        print("\nWelcome to this student's database") 
        name = input("Input your name: ").title()
        major = input("Major: ").title()

        is_correct_gpa = False
        while not is_correct_gpa:
            try:
                gpa = float(input("GPA: "))
                is_correct_gpa = True
                if gpa < 0 or gpa > 5:
                    is_correct_gpa = False 
                    print("\nSorry, input between 0 and 5")
            except ValueError as err:
                print('\nInput a number instead')
        
        is_correct_probation = False
        while not is_correct_probation:
            probation = input("Are you on probation: y/n ").lower()
            if probation == "y": 
                probation = True
                is_correct_probation = True
            elif probation == "n":
                probation = False
                is_correct_probation = True
            else: 
                print("Invalid input")
                is_correct_probation = False


        loop_is_correct_data = True
        while loop_is_correct_data:
            correct = input("\nDo you think the data you entered is correct? y/n ").lower()
            loop_is_correct_data = False
            if correct == "y":

                data = load_data()

                new_student = Student_Profile(name, major, gpa, probation)
                name = str(new_student.name).strip()
                major = str(new_student.major).strip()
                gpa = str(new_student.gpa).strip()
                probation = str(new_student.is_on_probation).strip()

                new_data = {'id': random.randint(int(1e5),int(1e6)), 'name': name, 'major': major, 'gpa': gpa, 'probation': probation}
                data.append(new_data)

                with open('database.json', 'w') as database:
                    json.dump(data, database)
                    database.close()
                
                    data = load_data()
                    print('\n', data[len(data) - 1])
                    database.close()
            elif correct == "n": 
                print('Add new entry prompt declined.')
            else:
                print('Invalid response.')
                loop_is_correct_data = True
        

        repeat_more_data_prompt = True
        while repeat_more_data_prompt: 
            more_data = input('Do you want to enter more data? y/n ')
            if more_data == "y": 
                to_repeat = True
                repeat_more_data_prompt = False
            elif more_data == "n":
                to_repeat = False
                repeat_more_data_prompt = False
                programme_flow()
            else: 
                print('Sorry, invalid input.')
        

def search_data():
    data = load_data()
    search_by = input("\nSelect your key for searching. \na Name \nb Major \nc GPA \nd Probation status\n: ").lower()

    if search_by == "a":
        search = input("\nEnter the person's name: ").lower().strip()
        response = []
        for entry in data:
            if entry['name'].lower() == search:
                response.append(entry)
        if len(response) == 0: 
            print("No search result found.")
        else:
            for search_result in response:
                print(search_result)    
            return search_result

    elif search_by == "b":
        search = input("\nEnter the person's major: ").lower().strip()
        response = []
        for entry in data:
            if entry['major'].lower() == search:
                response.append(entry)
        if len(response) == 0: 
            print("No search result found.")
        else:
            for search_result in response:
                print(search_result)    
            return search_result

    elif search_by == "c":
        repeat_this = True
        while repeat_this:
            try:
                search = float(input("\nEnter the person's gpa: "))
                repeat_this = False
            except ValueError as err:
                print('Invalid input.')
                repeat_this = True
            
        response = []
        for record in data:
            if float(record['gpa']) == search:
                response.append(record)
        if len(response) == 0: 
            print("No search result found.")
        else:
            for search_result in response:
                print(search_result)    
            return search_result

        
    elif search_by == "d":
        loop_validate_probation_search = True
        while loop_validate_probation_search:
            search = input("\nEnter the person's probation status (t/f) \n: ").lower().strip()
            
            if search == 't':
                loop_validate_probation_search = False
                response = []
                for record in data:
                    if record['probation'] == 'True':
                        response.append(record)
                if len(response) == 0: 
                    print("No search result found.")
                else:
                    for search_result in response:
                        print(search_result)    
                    return search_result
            elif search == 'f':
                loop_validate_probation_search = False
                response = []
                for record in data:
                    if record['probation'].strip() == 'False':
                        response.append(record)
                if len(response) == 0: 
                    print("No search result found.")
                else:
                    for search_result in response:
                        print(search_result)    
                    return search_result
            else:
                loop_validate_probation_search = True
                print('Invalid input. Enter t for true and f for false')

    else: 
        print("Invalid input. Enter from a - d")
        search_data()
    programme_flow()

# def count_entries():
#     data = load_data()
#     print('\n', len(data) + ' entries.')
#     programme_flow()

# def delete_entry():
#     selected_entry = search_data()
#     confirm_delete = input('Are you sure you want to delete this entry? (y/n) \n:').lower().strip()
#     loop_confirm_delete = True
#     while loop_confirm_delete:
#         loop_confirm_delete = False
#         if confirm_delete == 'y':
#             with open('database.json', 'w') as database:
#                 data = json.load(database)
                
#                 for entry in data:
#                     if entry == selected_entry:

#         elif confirm_delete == 'n':
#             print('Delete request declined.')
#         else: 
#             print('Invalid input. Enter y for yes and n for no.')
#             loop_confirm_delete = True

def clear_data():
    request = input("Are you sure you want to erase all entries? (y/n) \n: ").lower()
    if request == 'y':
        with open('database.json', 'w') as database:
            json.dump([], database)
            database.close()
        print('All entries cleared successfully') 
    elif request == 'n':
        print('Erase request ignored.')
    else: 
        print('Invalid input. Enter y for yes and n for no.')
        clear_data()
    programme_flow()


print('Welcome to this student\'s database')
def programme_flow():
    request = input('\nEnter \n\'add\' to input data, \n\'search\' to search through data records and \n\'clear\' to clear data records \n: ').lower()

    if request == 'add':
        input_data()
    elif request == 'search':
        search_data()
    elif request == 'clear':
        clear_data()
    else:
        print('Invalid input.')
        programme_flow()
    
programme_flow()