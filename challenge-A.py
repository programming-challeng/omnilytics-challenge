import random
import string

#function to create random alphabetical strings
def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(random.randint(5, 20)))
    return result_str

# to generate random integers of random length
def get_random_int():
    return random.randint(100000, 90000000)

# to generate random real numbers of varying length
def get_random_real():
    return random.uniform(10.5, 900000000.5)

# to generate random alphanumeric with random leading & trailing whitespaces 
def get_random_alphanumeric():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ' '*random.randint(1,10)
    for x in range(random.randint(5, 20)):
        result_str = result_str+random.choice(letters_and_digits)
    result_str = result_str+' '*random.randint(1,10)
    return result_str
   

# function to create list of functions in random order each time they are called
def run_functions_in_random_order(*funcs):
    functions = list(funcs)
    random.shuffle(functions)
    return functions

def gen_file():
    maxsize = 10485760 # no of bytes in 1 MB
    f=open('data.txt','w', newline='')
    for i in range(1,200000):
        functions = run_functions_in_random_order(get_random_string, get_random_int, get_random_real, get_random_alphanumeric)
        if f.tell() >= maxsize:
            break
        else:
            if i == 1:
                f.write(f'{functions[0]()},{functions[1]()},{functions[2]()},{functions[3]()}')
            else:
                f.write(f',{functions[0]()},{functions[1]()},{functions[2]()},{functions[3]()}')    
    f.close()

gen_file()