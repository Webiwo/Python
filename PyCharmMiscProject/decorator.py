# Decorator

def my_decorator(func):
    def wrap_func():
        print("*************")
        func()
        print("*************")

    return wrap_func


@my_decorator
def hello():
    print("Heloooooo!")


# to samo co
# my_decorator(hello)()  - Higher Order Function (FOC)
# lub
# a = my_decorator(hello)
# a()

hello()


def my_decorator_params(func):
    def wrap_func(*args, **kwargs):
        print("*************")
        func(*args, **kwargs)
        print("*************")

    return wrap_func


@my_decorator_params
def greet(greeting, emoji=':-)'):
    print(greeting, emoji)


greet("hiii")

###### PERFORMANCE DECORATOR
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time_fn():
    for i in range(10000000):
        j = i * 5


long_time_fn()

###### AUTHENTICATION DECORATOR
user1 = {
    "name": "Olaf",
    "valid": False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def send_message(user):
    print("message has been sent")


send_message(user1)
