

# exersice 1

# count = 0
# def bump():
#     global count
#     count += 1
#
# def value():
#     return count


# exersice 2

# def make_counter():
#     counter = 0
#     def step():
#         nonlocal counter
#         counter += 1
#         print(counter)
#     return step
#
# c = make_counter()
#
# c()
# c()
# c()


# exersice 3

# local
# enclosing
# global


# exersice 4

# This raises a TypeError because the list above is inside a variable named list and it overwrites the list function.

# listi = [1, 2, 3]
# print(list(range(5)))


# exersice 5

# done


# exersice 6

# done


# exersice 7

# from datetime import datetime as dt ;print(dt.now())



# exersice 8
# import math
#
# def public_names(m):
#     attribute_name = [name for name in dir(m) if not name.startswith("_")]
#     return attribute_name
#
# print(public_names(math))


# exersice 9

# Since bug == list then only before the first time it will be empty,
# and it will remember everything we entered since it is just a pointer to memory and not a value.
# The fix is to make a new list.

# def add_item(item, bag=[]):
#     bag = bag[:]
#     bag.append(item)
#     return bag
#
# print(add_item(1))
# print(add_item(2))


# exersice 10

from geometry import circle, rectangle

print(circle.area(5))
print(rectangle.area(4, 6))