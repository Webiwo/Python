from time import time


# how do generators work?
def generator_function(num):
    for n in range(num):
        yield n


for i in generator_function(10):
    print(i)

gf = generator_function(100)
print(next(gf))
print(next(gf))
print(next(gf))


# generators efficiency
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time1():
    print("long_time1")
    for i in range(10000000):
        j = i * 5


@performance
def long_time2():
    for i in list(range(10000000)):
        j = i * 5


long_time1()
long_time2()


# UNDER THE HOOD OF GENERATORS
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3, 4])


# MY OWN RANGE GEN
class MyRange:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


my_range = MyRange(5, 9)
for i in my_range:
    print(i)


# FIBONACCI NUMBERS
class Fibonacci:
    def __init__(self, f_num):
        self.first_num = 0
        self.second_num = 1
        self.f_num = f_num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.f_num:
            temp = self.first_num
            self.first_num = self.second_num
            self.second_num = temp + self.second_num
            self.counter += 1
            return temp
        raise StopIteration


print("Fibonacci 1")
fib = Fibonacci(10)
for i in fib:
    print(i)


def fib_func(f_num):
    first_num = 0
    second_num = 1
    for i in range(f_num):
        yield first_num
        temp = first_num
        first_num = second_num
        second_num = temp + second_num


print("Fibonacci 2")
for x in fib_func(10):
    print(x)
