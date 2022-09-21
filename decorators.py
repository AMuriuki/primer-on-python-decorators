def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    # return `wrapper` as a function 
    return wrapper


def say_whee():
    print("Whee!")


# `say_whee` variable assigned to `my_decorator(func)`
say_whee = my_decorator(say_whee)


say_whee()