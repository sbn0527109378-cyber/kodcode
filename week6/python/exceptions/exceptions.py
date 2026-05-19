# exersice 1


# def safe_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None
# print(safe_int("f"))


# exersice 2

# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "undefined"
# print(safe_divide(3,0))


# exersice 3

# def get_value(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return "missing"
# print(get_value({"a":1,"b":2},"c"))


# exersice 4

# def parse_ints(values):
#     ints_list = []
#     for num in values:
#         try:
#             ints = int(num)
#             ints_list.append(ints)
#         except ValueError:
#             pass
#     return ints_list
# print(parse_ints(["2","a","3","d"]))


# exersice 5

# def set_age(age):
#     if 0 <= age <= 150:
#         return age
#     else:
#         raise ValueError
# print(set_age(190))


# exersice 6

# def retry(func, n):
#     for i in range(n):
#         try:
#             return func()
#         except Exception as e:
#             if i == n - 1:
#                 raise e


# exersice 7

# def count_errors(funcs):
#     counter = 0
#     for func in funcs:
#         try:
#             func()
#         except Exception:
#             counter += 1
#     return counter
# print(count_errors([lambda: 1, lambda: 1/0, lambda: int("x"), lambda: 2]))


# exersice 8

# def load_config(path):
#     try:
#         with open(path,"r") as f:
#             conversion = int(f.readline())
#         return conversion
#     except Exception as e:
#         raise RuntimeError("failed to load config") from e
# load_config("fd")