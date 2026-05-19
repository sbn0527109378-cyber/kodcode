

# exersice 1

# def remove_duplicates(lst):
#     return list(set(lst))
#
# print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))


# exersice 2

# def count_unique_elements(lst):
#     listi = []
#     for char in lst:
#         if char not in listi:
#             listi.append(char)
#     return len(listi)
#
# print(count_unique_elements([1, 2, 2, 3, 1, 4]))


# exersice 3

# def common_elements(list1,list2):
#     return sorted(set(list1) & set(list2))
#
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))


# exersice 4

# def elements_in_only_one(list1,list2):
#     return sorted(set(list1) ^ set(list2))
#
# print(elements_in_only_one([1, 2, 3, 4], [3, 4, 5, 6]))


# exersice 5

# def is_subset(a, b):
#     return set(a) <= set(b)
#
# print(is_subset([1, 2, 3], [1, 2, 3, 4, 5]))
# print(is_subset([1, 2, 6], [1, 2, 3, 4, 5]))


# exersice 6

# def unique_characters(stri):
#     seti = set(list(stri))
#     return len(stri) == len(seti)
#
# print(unique_characters("abcdef"))
# print(unique_characters("hello"))


# exersice 7

# def first_repeated_element(lst):
#     if not len(set(lst)) == len(lst):
#         stri = ""
#         for char in lst:
#             if str(char) not in stri:
#                 stri += str(char)
#                 continue
#             return char
#     return None
#
# print(first_repeated_element([1, 2, 3, 2, 4, 1]))
# print(first_repeated_element([1, 2, 3, 4]))


# exersice 8

# def distinct_words(string_of_words):
#     return len(set(string_of_words.lower().split(" ")))
#
# print(distinct_words("The cat and the dog and the bird"))


# exersice 9

# def pair_sum_exists(list_of_integers, target):
#     for i in range(target):
#         if i in list_of_integers and target - i in list_of_integers:
#             return True
#     return False
#
# print(pair_sum_exists([3, 1, 4, 7, 2], 6))
# print(pair_sum_exists([3, 1, 4, 7, 2], 100))


# exersice 10

# def symmetric_difference(lst1, lst2):
#     new_list = list(set(lst1 + lst2))
#     for num in lst1:
#         if num in lst2:
#             new_list.remove(num)
#     return sorted(new_list)
#
# print(symmetric_difference([1, 2, 3, 4], [3, 4, 5, 6]))