x = 10

def my_function():
    x = 5
    print(x)

my_function()

# error. x is used before initializing

def my_function():
    a = 1

    if True:
        print(a)

my_function()

# prints 1

a = 1

def my_function():
    print(a)

my_function()

# prints 1

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# prints 1 and initializes new local variable a and assigns it to 2
# nevermind it doesn't work. Don't try to mutate or reassign global variables
# error bc tries to access a before initialization