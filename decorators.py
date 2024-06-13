'''
Decorater chanage the functionaly of the another function by passing 
function as ar argument
'''

# let's take a simple sinario of the function
'''
def add(x, y):
    return x + y

result = add(10, 10)
print(result)
'''


# passing function into the anothe function
'''
def car(brand, price):
    print(price)
    return brand

def brand(name):
    pass

brand_name = brand("Toyota")
details = car(brand_name, 2000000)
print(details)
'''

# decorator without @ symbol
'''
def outer(fun):
    def inner():
        print("I'm inner function inside the outer function")
        new_outer()
    return inner

def new_outer():
    print("I'm new_outer function")

outer_fun_obj = outer(new_outer)
outer_fun_obj()
'''


# decorator with @ symbol
'''
def outer(fun):
    def inner():
        print("I'm inner function inside the outer function")
        fun()
    return inner

@outer  
def new_outer():
    print("I'm new_outer function")

new_outer()
'''     


# Example of decorator
'''     
def smart_division(fun):
    def inner(a, b):
        if b == 0:
            print("Not divisible")
        
        return fun(a, b)
    return inner

@smart_division
def divide(a, b):
    print(a / b)

divide(5, 2)
'''   


# greed to the person
'''
def greed(fun):
    def inner_fun(name):
        return f"Hello, {name}"
    
    return inner_fun

@greed
def say_hello(name):
    return name

result = say_hello("ankit")
print(result)
'''


# Question 1: Basic Level
# Question: Write a Python decorator uppercase_decorator that takes a function say_hello as input
# and modifies it to print its output in uppercase.
'''
def uppercase_decorator(fun):
    def wrapper():
        return fun().upper()
    return wrapper
    # print(temp.upper())

@uppercase_decorator
def say_hello():
    return "hello"

result = say_hello()
print(result)
'''


# Question 2: Intermediate Level
# Question: Create a decorator timing_decorator that measures and prints the time taken for a function to execute.

# def timing_decorator(fun):
#     def wrapper():
#         return fun()
#     return wrapper

# @timing_decorator
# def calculate_sum(n):
#     return sum(range(n + 1))

# result = calculate_sum(1000000)
# print(result())



# Question 3: Basic Level
# Question: Write a decorator even_odd_decorator that takes a function is_even_or_odd as input and
# modifies it to print whether the return value is even or odd.
'''
def even_odd_decorator(fun):
    def inner():
        temp = fun()
        return temp
    return inner

@even_odd_decorator
def is_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

result = is_even_or_odd(5)
print(result())
'''


# Question: Write a decorator print_arguments that prints the arguments passed to the 
# function before calling it.


