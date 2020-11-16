# Assigning Functions to Variables
def plus_one(number):
    return number + 1

add_one = plus_one

print(add_one(5))

# Defininf Functions inside other Functions

def plus_one2(number):
    def add_one(number):
        return number + 1
    result = add_one(number)
    return result

print(plus_one2(4))

# Passing Functions as arguments for other Functions

def plus_one3(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one3))


# Functions Returning other Functions

def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi

hello = hello_function()
print(hello())

# Nested Functions have acess to the Enclosing Function's Variable Scope

def print_message(message):
    'Enclosong function'
    def messsage_sender():
        'Nested Function'
        print(message)
    
    messsage_sender()

print_message('Some random message')

# Creating Decorators
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def say_hello():
    return 'hello there'

decorate = uppercase_decorator(say_hello)

print(decorate())

#However, Python provides a much easier way for us to apply decorates. We simply use the @ symbol before the function we'd like to decorate.

@uppercase_decorator
def say_hello2():
    return 'hello there'

print(say_hello2())



# Um decorador ele vai, basicamente, mudar as funcionalidades de uma função sem mexer no seu escopo. Vamos a um exemplo simples a seguir:

