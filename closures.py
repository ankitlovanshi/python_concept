# closures

def outer_fun(fname):
    def inner_fun(lname):
        print(fname + " " + lname)
    
    return inner_fun

result = outer_fun("ankit")
result("lovanshi")



# questions
# Create a function make_multiplier that takes a single argument n and returns a 
# new function. This new function should take another argument x and return the product of x and n.
def make_multiplier(n):
    def inner_fun(x):
        return n * x
    
    return inner_fun

result = make_multiplier(5)
print(result(2))



# Create a function make_counter that returns a new function. This new function 
# should return the count of how many times it has been called.

def make_counter():
    count = 0
    def inner_fun():
        nonlocal count
        count += 1
        return count
    
    return inner_fun

result = make_counter()
print(result())
print(result())
print(result())



# Create a function make_accumulator that takes a single argument start and 
# returns a new function.This new function should take another argument x and 
# add x to an internal total starting from start.It should return the new total
#  each time it's called.

def make_accumulator(start):
    total = start
    def inner_fun(x):
        nonlocal total 
        total += x
        return total
    return inner_fun

result = make_accumulator(10)
print(result(10))
print(result(10))



# Create a function make_power that takes a single argument exp (exponent) and 
# returns a new function. This new function should take another argument base 
# and return base raised to the power of exp.

def make_power(exp):
    def inner_fun(base):
        power = base ** exp
        return power
    return inner_fun

result = make_power(2)
print(result(3))
print(result(5))

result = make_power(3)
print(result(2))   
print(result(4)) 


# Create a function make_suffix_adder that takes a single argument suffix and 
# returns a new function. This new function should take another argument word
#  and return the word concatenated with the suffix.

def make_suffix_adder(suffix):
    
    def inner_fun(word):
        return word + suffix
    
    return inner_fun

result = make_suffix_adder("ing")
print(result("play"))
print(result("read"))



# Create a function make_greeting that takes a single argument greeting (a string) 
# and returns a new function. This new function should take another argument name
#  and return a greeting message that combines both the greeting and the name.


def make_greeting(greeting):
    def inner_fun(name):
        greet = greeting + " " + name
        return greet
    
    return inner_fun

result = make_greeting("Hello")
print(result("ankit"))



# Create a function make_cache that returns a new function. This new function should
#  take a single argument x, and return the square of x. Additionally, it should cache
#  the result so that if the function is called again with the same x, it returns the 
# cached result instead of recalculating it.

'''
I have to solve some cocept is not clear
'''


# Create a function make_fibonacci that returns a new function. This new function 
# should return  the next number in the Fibonacci sequence each time it is called.

# check

def make_fibonacci():
    a, b = 0, 1
    def inner_fun():
        nonlocal a, b
        next_value = a
        a = b
        b = a + b
        return next_value
    
    return inner_fun

result = make_fibonacci()
print(result())

# Create a function make_avg_calculator that returns a new function. This new function 
# should take a single argument x and return the running average of all the numbers 
# it has been called with.

def make_avg_calculator():
    total = 0
    count = 1
    def inner_fun(x):
        nonlocal total, count 
        total = total + x
        avg = total / count
        count += 1
        return avg
    
    return inner_fun

result = make_avg_calculator()
print(result(10))
print(result(20))


# Create a function make_divisible_by that takes a single argument n and returns a 
# new function.This new function should take another argument x and return the smallest
#  number divisible by n that is greater than or equal to x.


