# a programme to perform operations for sequence and series
from math import * 

# gets values
def get_a():
    a = float(input('\nEnter the first term (a): '))
    return a 

def get_n():
    n = float(input('\nEnter the number of terms (n): '))
    return n

def get_d():
    d = float(input('\nEnter the common difference (d): '))
    return d 

def get_r():
    r = float(input('\nEnter the common ratio (r): '))
    return r

def get_l():
    l = float(input('\nEnter the last term (l): '))
    return l

def get_Tn():
    Tn = float(input('\nEnter the n-th term (Tn): '))
    return Tn

def get_Sn():
    Sn = float(input('\nEnter the sum of the sequence / series (Sn): '))
    return Sn

    

# arithmetic progression operations
def arithmetic_progression():

    def repeat():
        response = input('\nDo you want to repeat an operation on arithmetic progression? (y/n) \n: ').lower().strip()
        if response == 'y':
            arithmetic_progression()
        elif response == 'n':
            programme_flow()
        else: 
            print('Invalid input. Enter y for yes or n for no.')
            repeat()

    def ap_sequence():

        def seq_calc_tn():
            print('\nTn = a + [(n - 1) * d]. Input the appropriate values.')
            try:
                a = get_a()
                n = get_n()
                d = get_d()
                Tn = a + ((n - 1) * d)
                print(f'\nTn = a + [(n - 1) * d]. \nTn = {Tn}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                seq_calc_tn()

        def seq_calc_a():
            print('\na = Tn - [(n - 1) * d]. Input the appropriate values.')
            try:
                Tn = get_Tn()
                n = get_n()
                d = get_d()
                a = Tn - ((n - 1) * d)
                print(f'\na = Tn - [(n - 1) * d]. \na = {a}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                seq_calc_a()

        def seq_calc_n():
            print('\nn = [(Tn - a) / d] + 1. Input the appropriate values.')
            try:
                Tn = get_Tn()
                a = get_a()
                d = get_d()
                n = ((Tn - a) / d) + 1
                print(f'\nn = [(Tn - a) / d] + 1. \nn = {n}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                seq_calc_n()

        def seq_calc_d():
            print('\nd = (Tn - a) / (n - 1). Input the appropriate values.')
            try:
                Tn = get_Tn()
                a = get_a()
                n = get_n()
                d = (Tn - a) / (n - 1)
                print(f'\nd = (Tn - a) / (n - 1). \nd = {d}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                seq_calc_d()

        print('\nThe form of the equation is Tn = a + [(n - 1) * d]. \nTn being the n-th term, a, the first term, n, the number of terms, and d, the common difference.')
        subject = input('\nEnter the Tn, a, n, or d to make that the subject of the formula and then enter the appropraite inputs. \n: ').strip().lower()
        if subject == 'tn':
            seq_calc_tn()
        elif subject == 'a':
            seq_calc_a()
        elif subject == 'n':
            seq_calc_n()
        elif subject == 'd':
            seq_calc_d()
        else: 
            print('Invalid input. Enter Tn, a, n, or d.')
            ap_sequence()


    def ap_series():

        def series_a():

            def ser_a_calc_sn():
                print('\nSn = (n / 2) * (a + l). Input the appropriate values.')
                try:
                    a = get_a()
                    n = get_n()
                    l = get_l()
                    Sn = (n / 2) * (a + l)
                    print(f'\nSn = (n / 2) * (a + l). \nSn = {Sn}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_sn()

            def ser_a_calc_a():
                print('\na = (2 * Sn / n) - l. Input the appropriate values.')
                try:
                    Sn = get_Sn()
                    n = get_n()
                    l = get_l()
                    a = (2 * Sn / n) - l
                    print(f'\na = (2 * Sn / n) - l. \na = {a}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_sn()

            def ser_a_calc_n():
                print('\nn = (2 * Sn) / (a + l). Input the appropriate values.')
                try:
                    Sn = get_Sn()
                    a = get_a()
                    l = get_l()
                    n = (2 * Sn) / (a + l)
                    print(f'\nn = (2 * Sn) / (a + l). \nn = {n}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_sn()

            def ser_a_calc_l():
                print('\nl = (2 * Sn / n) - a. Input the appropriate values.')
                try:
                    Sn = get_Sn()
                    n = get_n()
                    a = get_a()
                    l = (2 * Sn / n) - a
                    print(f'\nl = (2 * Sn / n) - a. \nl = {l}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_sn()

            print('\nThe form of the equation is Sn = (n / 2) * (a + l). \nSn being the sum of sequence / series, a, the first term, n, the number of terms, and l, the last term.')
            subject = input('\nEnter the Sn, a, n, or l to make that the subject of the formula and then enter the appropraite inputs. \n: ').strip().lower()
            if subject == 'sn':
                ser_a_calc_sn()
            elif subject == 'a':
                ser_a_calc_a()
            elif subject == 'n':
                ser_a_calc_n()
            elif subject == 'l':
                ser_a_calc_l()
            else: 
                print('Invalid input. Enter Sn, a, n, or l.')
                ap_series()


        def series_b():

            def ser_b_calc_sn():
                print('\nSn = (n / 2) * {(2 * a) + [(n - 1) * d]}. Input the appropriate values.')
                try:
                    n = get_n()
                    a = get_a()
                    d = get_d()
                    Sn = (n / 2) * ((2 * a) + ((n - 1) * d))
                    print('\nSn = (n / 2) * {(2 * a) + [(n - 1) * d]}.', f'\nSn = {Sn}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values or try validating your question values.')
                    ser_b_calc_sn()
            def ser_b_calc_a():
                print('\na = (Sn / n) - ((n - 1) * d / 2). Input the appropriate values.')
                try:
                    Sn = get_Sn()
                    n = get_n()
                    d = get_d()
                    a = (Sn / n) - ((n - 1) * d / 2)
                    print(f'\na = (Sn / n) - ((n - 1) * d / 2). \na = {a}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_b_calc_a()
            def ser_b_calc_n():
                print('\nn = {d - (2 * a) + or - sqrt[(8 * d * Sn) + (4 * a ^ 2)) - (4 * a * d) + (d ^ 2)]} / (2 * d). (To pick a positive number).\nInput the appropriate values.')
                try:
                    d = get_d()
                    a = get_a()
                    Sn = get_Sn()
                    
                    n1 = (d - (2 * a) + sqrt((8 * d * Sn) + (4 * (a ** 2)) - (4 * a * d) + (d ** 2))) / (2 * d) 
                    n2 = (d - (2 * a) - sqrt((8 * d * Sn) + (4 * (a ** 2)) - (4 * a * d) + (d ** 2))) / (2 * d) 

                    print('\nn = {d - (2 * a) + or - sqrt[(8 * d * Sn) + (4 * a ^ 2)) - (4 * a * d) + (d ^ 2)]} / (2 * d). (The positive answer)')
                    if abs(n1) == n1:
                        print(f'\nn = {n1}')
                    else:
                        print(f'\nn = {n2}')

                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_b_calc_n()
            def ser_b_calc_d():
                print('\nd = [(2 * Sn) - (2 * a * n)] / [(n ^ 2) - n]. Input the appropriate values.')
                try:
                    Sn = get_Sn()
                    a = get_a()
                    n = get_n()
                    d = ((2 * Sn) - (2 * a * n)) / ((n ** 2) - n)
                    print(f'\nd = [(2 * Sn) - (2 * a * n)] / [(n ^ 2) - n]. \nd = {d}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_b_calc_d()

            print('\nThe form of the equation is Sn = (n / 2) * {(2 * a) + [(n - 1) * d]}. \nSn being the sum of sequence / series, a, the first term, n, the number of terms, and d, the common difference.')
            subject = input('\nEnter the Sn, a, n, or d to make that the subject of the formula and then enter the appropraite inputs. \n: ').strip().lower()
            if subject == 'sn':
                ser_b_calc_sn()
            elif subject == 'a':
                ser_b_calc_a()
            elif subject == 'n':
                ser_b_calc_n()
            elif subject == 'd':
                ser_b_calc_d()
            else: 
                print('Invalid input. Enter Sn, a, n, or d.')
                ap_series()



        is_not_validated = False
        while not is_not_validated:
            is_not_validated = True
            response = input('\nChoose the form of equation you desire for this operation. \n(a) Sn = (n / 2) * (a + l) \n(b) Sn = (n / 2) * {(2 * a) + [(n - 1) * d]}. \nSn being the sum of sequence / series, a, the first term, n, the number of terms, and d, the common difference. \n: ').strip().lower()

            if response == 'a':
                series_a()
            elif response == 'b':
                series_b()
            else:
                print('Invalid input. Enter either a or b.')
                is_not_validated = False

    sequence_or_series = input('\nEnter "seq" to perform calculate on the basis of sequence \n"ser" to perform calculate on the basis of series. \n: ').strip().lower()
    if sequence_or_series == 'seq':
        ap_sequence()
    elif sequence_or_series == 'ser':
        ap_series()
    else: 
        print('Invalid input. Enter either "seq" or "ser".')
        arithmetic_progression()


def geometric_progression():

    def repeat():
        response = input('\nDo you want to repeat an operation on geometric progression? (y/n) \n: ').lower().strip()
        if response == 'y':
            geometric_progression()
        elif response == 'n':
            programme_flow()
        else: 
            print('Invalid input. Enter y for yes or n for no.')
            repeat()

    def gp_sequence():

        def ser_calc_tn():
            print('\nTn = a * r ^ (n - 1). Input the appropriate values.')
            try:
                a = get_a()
                n = get_n()
                r = get_r()
                Tn = a * r ** (n - 1)
                print(f'\nTn = a * r ^ (n - 1). \nTn = {Tn}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                ser_calc_tn()

        def ser_calc_a():
            print('\na = Tn / r ^ (n - 1). Input the appropriate values.')
            try:
                Tn = get_Tn()
                n = get_n()
                r = get_r()
                a = Tn / r ** (n - 1)
                print(f'\na = Tn / r ^ (n - 1). \na = {a}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                ser_calc_a()

        def ser_calc_n():
            print('\nn = [log (Tn) / log (ar)] + 1. Input the appropriate values.')
            try:
                Tn = get_Tn()
                a = get_a()
                r = get_r()
                n = (log(Tn) / log(a * r)) + 1
                print(f'\nn = [log (Tn) / log (ar)] + 1. \nn = {n}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                ser_calc_n()

        def ser_calc_r():
            print('\nr = (Tn / a) ^ [1 / (n - 1)]. Input the appropriate values.')
            try:
                Tn = get_Tn()
                a = get_a()
                n = get_n()
                r = pow((Tn / a), 1 / (n-1))
                print(f'\nr = (Tn / a) ^ [1 / (n - 1)]. \nr = {r}')
                repeat()
            except Exception: 
                print('Sorry, an error occured. Please re-enter all values.')
                ser_calc_r()

        print('\nThe form of the equation is Tn = a * r ^ (n - 1). \nTn being the n-th term, a, the first term, n, the number of terms, and r, the common ratio.')
        subject = input('\nEnter Tn, a, n, or r to make that the subject of the formula and then enter the appropraite inputs. \n: ').strip().lower()
        if subject == 'tn':
            ser_calc_tn()
        elif subject == 'a':
            ser_calc_a()
        elif subject == 'n':
            ser_calc_n()
        elif subject == 'r':
            ser_calc_r()
        else: 
            print('Invalid input. Enter Tn, a, n, or r.')
            gp_sequence()


    def gp_series():

        def series_n():
            def ser_a_calc_sn():
                print('\nSn = a * [(r ^ n) - 1] / (r - 1) or Sn = a * [1 - (r ^ n)] / (1 - r). Depending on the value of r. \nInput the appropriate values.')
                try:
                    a = get_a()
                    r = get_r()
                    n = get_n()
                    if r > 1:
                        Sn = a * ((r ** n) - 1) / (r - 1)
                        print(f'Sn = a * [(r ^ n) - 1] / (r - 1). \nSn = {Sn}')
                    else:
                        Sn = a * (1 - (r ** n)) / (1 - r)
                        print(f'Sn = a * [1 - (r ^ n)] / (1 - r). \nSn = {Sn}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_sn()

            def ser_a_calc_a():
                print('\na = Sn * (r - 1) / [(r ^ n) - 1] or a = Sn * (1 - r) / [1 - (r ^ n)]. Depending on the value of r. \nInput the appropriate values.')
                try:
                    Sn = get_Sn()
                    r = get_r()
                    n = get_n()
                    if r > 1:
                        a = Sn * (r - 1) / ((r ** n) - 1)
                        print(f'a = Sn * (r - 1) / [(r ^ n) - 1]. \na = {a}')
                    else:
                        a = Sn * (1 - r) / (1 - (r ** n))
                        print(f'a = Sn * (1 - r) / [1 - (r ^ n)]. \na = {a}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_a()

            def ser_a_calc_n():
                print('\nn = log(Sn * (r - 1) / a + 1) / log(r) or n = log(1 + Sn * (1 - r) / a) / log(r). Depending on the value of r. \nInput the appropriate values.')
                try:
                    Sn = get_Sn()
                    r = get_r()
                    a = get_a()
                    if r > 1:
                        n = log(Sn * (r - 1) / a + 1) / log(r)
                        print(f'n = log(Sn * (r - 1) / a + 1) / log(r). \nn = {n}')
                    else:
                        n = log(1 + Sn * (1 - r) / a) / log(r)
                        print(f'n = log(1 + Sn * (1 - r) / a) / log(r). \nn = {n}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_n()


            def ser_a_calc_r():
                print('\na = Sn * (r - 1) / [(r ^ n) - 1] or a = Sn * (1 - r) / [1 - (r ^ n)]. Depending on the value of r. \nInput the appropriate values.')
                try:
                    Sn = get_Sn()
                    r = get_r()
                    n = get_n()
                    if r > 1:
                        a = Sn * (r - 1) / ((r ** n) - 1)
                        print(f'a = Sn * (r - 1) / [(r ^ n) - 1]. \nr = {r}')
                    else:
                        a = Sn * (1 - r) / (1 - (r ** n))
                        print(f'a = Sn * (1 - r) / [1 - (r ^ n)]. \nr = {r}')
                    repeat()
                except Exception: 
                    print('Sorry, an error occured. Please re-enter all values.')
                    ser_a_calc_r()
                
                
            print('\nThe form of the eqation is Sn = a * [(r ^ n) - 1] / (r - 1) or Sn = a * [1 - (r ^ n)] / (1 - r). Depending on the value of r. (r > 1, and r < 1 respectively)')
            print('\nSn being the n-th term, a, the first term, n, the number of terms, and r, the common ratio.')
            subject = input('\nEnter the Sn, a, n, or r to make that the subject of the formula and then enter the appropraite inputs. \n: ').strip().lower()
            if subject == 'sn':
                ser_a_calc_sn()
            elif subject == 'a':
                ser_a_calc_a()
            elif subject == 'n':
                ser_a_calc_n()
            elif subject == 'r':
                ser_a_calc_r()
            else: 
                print('Invalid input. Enter Tn, a, n, or r.')
                series_n()
            

        def series_a():
            pass

        absolute_series = input('\nEnter "n" to specify the number of terms or "a" to proceed for the absolute series. \n: ').strip().lower()
        if absolute_series == 'n':
            series_n()
        elif absolute_series == 'a':
            series_a()
        else:
            print('Invalid input. Please enter either n or a.')
            gp_series()

    sequence_or_series = input('\nEnter "seq" to perform calculate on the basis of sequence \n"ser" to perform calculate on the basis of series. \n: ').strip().lower()
    if sequence_or_series == 'seq':
        gp_sequence()
    elif sequence_or_series == 'ser':
        gp_series()
    else: 
        print('Invalid input. Enter either "seq" or "ser".')
        geometric_progression()


def programme_flow():
    progression_type = input('\nEnter "ap" for operations on arithmetic progression (linear sequence and series) or \n"gp" for operations on geometric progression (exponential sequence and series). \n: ').lower().strip()
    if progression_type == 'ap':
        arithmetic_progression()
    elif progression_type == 'gp':
        geometric_progression()
    else:
        print('Invalid input. Enter ap or gp.')
        programme_flow()


print('Welcome to this terminal based Sequence and Series calculator.')
programme_flow()