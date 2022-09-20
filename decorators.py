'''
using functions as return values.  
'''


def parent(num):

    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        # `first_child` returns a reference to the function
        # in contrast `first_child()` refers to the result 
        return first_child
    else:
        return second_child

# define & assign `first` and `second` variables 
# as references of respective `first_child` and `second_child` functions
first = parent(1)
second = parent(2)

# use the variables as if they are regular functions
first()
second()
