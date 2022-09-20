'''
functions in python are first class objects. 
They can be passed around and used as arguments 
'''


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are awesome"


def greet_bob(greeter_func):
    return greeter_func("Bob")


greet_bob(say_hello)

greet_bob(be_awesome)
