import sys

# either run this file in the terminal like this:   py root.py 234
# or go to the bottom of this file and enter:       print(square_root(234))

def square_root(num: float): 

    def derive_relatives(num):
        # check for actual perfect squares and the numbers close to it: x_l and x_u
        derived_x_l_and_u = True
        i = 0
        prev_i = i
        while derived_x_l_and_u: 
            x_l = i * i
            # print(i)
            # print(x_l)
            if num == x_l: 
                return [i]
            elif x_l < num: 
                prev_i = i
                i = i + 1
            elif x_l > num: 
                derived_x_l_and_u = False
                return [prev_i, i]

    result = derive_relatives(num)
    if len(result) == 1: 
        return result[0]
    else: 
        x_l, x_u = result

    def get_approx_root(num, x_l, x_u):
        # use sqrt(x_l + dx) = sqrt(x_l) + sqrt'(x_l)*dx to get estimate
            # if dx > sqrt'(x), use sqrt(x_u + dx) = sqrt(x_u) + sqrt'(x_u)*dx
        discriminant = x_l * 2
        d_x = num - x_l * x_l
        if d_x < discriminant: 
            return x_l + d_x / discriminant
        else: 
            d_x = x_u * x_u - num
            return x_u - d_x / discriminant
        
    approx_root = get_approx_root(num, x_l, x_u)

    def newton_s_approx(num, approx_root): 
        # use Newton's new_num = (guess_num + sqr/guess_num) / 2 to establish to dig for deeper root
        # return root_of_n
        root = approx_root
        prev_root = root
        for _ in range(10): 
            root = (root + num/root) / 2
            if prev_root != root: 
                prev_root = root
            elif prev_root == root: 
                break
        return root 

    return newton_s_approx(num, approx_root) # , approx_root


if len(sys.argv) == 2: 
    try: 
        input_num = float(sys.argv[1])
        print(f'Root of {input_num}:', '\t', square_root(input_num), end='\n\n')
    except: 
        print('Invalid number!', end='\n\n')


# print('4', '\t', square_root(4))
# print('9', '\t', square_root(9))
print('4.1', '\t', square_root(4.1))
