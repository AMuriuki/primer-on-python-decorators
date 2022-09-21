from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        # run decorated during the day only
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

# if you call between 10PM - 6AM nothing happens
say_whee()
