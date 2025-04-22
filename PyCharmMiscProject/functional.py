# map, filter, zip, reduce
####################################### MAP
my_list = [1, 2, 3]


def multiply_by_2(item):
    return item * 2


new_list_1 = list(map(multiply_by_2, my_list))
print(new_list_1)

print(list(map(lambda item: item * 2, my_list)))


####################################### FILTER
def check_odd(item):
    return item % 2 != 0


new_list_2 = list(filter(check_odd, my_list))
print(new_list_2)

print(list(filter(lambda item: item % 2 != 0, my_list)))

####################################### ZIP
your_list = [5, 6, 7, 8]
his_list = [11, 12, 13, 14]

new_list_3 = list(zip(my_list, your_list, his_list))
print(new_list_3)

####################################### REDUCE
from functools import reduce


def accumulate(acc, item):
    return acc + item


new_val = reduce(accumulate, my_list, 0)
print(new_val)
print(reduce(lambda acc, item: acc + item, my_list))

# exercise
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))

# lambda expressions
num_list = [5, 4, 3]
print("square", list(map(lambda item: item ** 2, num_list)))

my_tuples = [(0, 2), (4, 3), (9, 9), (10, -1)]
my_tuples.sort(key=lambda item: item[1])
print("Sort", my_tuples)

# COMPREHENSIONS
even_squared_numbers = [num ** 2 for num in range(20) if (num ** 2) % 2 == 0]
print(even_squared_numbers)

my_square_dict = {num: num ** 2 for num in [1, 2, 3, 4]}
print(my_square_dict)

letter_list = ["a", "b", "a", "c", "d", "b", "n", "n"]
duplicates = set([l for l in letter_list if letter_list.count(l) > 1])
print(duplicates)
