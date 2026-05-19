

# exersice 1
# def sum_of_list(lst):
#     sumi = 0
#     for num in lst:
#         sumi += num
#     return sumi
#
# print(sum_of_list([1, 2, 3, 4, 5]))


# exersice 2

# def largest_num(lst):
#     maxi = lst[0]
#     for num in lst:
#         if num > maxi:
#             maxi = num
#     return maxi
#
# print(largest_num([3, 7, 2, 8, 5]))


# exersice 3

# def counter_value_in_list(lst,value):
#     counter = 0
#     for num in lst:
#         if num == value:
#             counter += 1
#     return counter
#
# print(counter_value_in_list([1, 2, 3, 2, 4, 2],2))


# exersice 4

# def reverse_list(lst):
#     new_list = []
#     for i in range(len(lst)):
#         numm = lst.pop()
#         new_list.append(numm)
#     return new_list
#
# print(reverse_list([4, 3, 2, 1]))


# exersice 5

# def remove_duplicates(lst):
#     new_list = []
#     for num in lst:
#         if not num in new_list:
#             new_list.append(num)
#     return new_list
#
# print(remove_duplicates( [1, 2, 2, 3, 1, 4, 3]))


# exersice 6

# def second_largest_distinct_value(lst):
#     second_value = None
#     maxi = max(lst)
#     for num in lst:
#         if num != maxi and (second_value == None or num > second_value):
#             second_value = num
#     return second_value
#
# print(second_largest_distinct_value([4, 1, 7, 7, 3, 5]))
# print(second_largest_distinct_value([10,10,10]))


# exersice 7

# def merge_two_sorted_lists(lst1,lst2):
#     new_list = []
#     new_list.extend(lst1)
#     new_list.extend(lst2)
#     new_list.sort()
#     return new_list
#
# print(merge_two_sorted_lists([1, 3, 5], [2, 4, 6]))

# exersice 8

# def rotate_a_list(lst,k):
#     k = k % len(lst)
#     new_list = []
#     for num in lst[-k::1]:
#         indexi = lst.index(num)
#         popi = lst.pop(indexi)
#         new_list.append(popi)
#     new_list.extend(lst)
#     return new_list
#
# print(rotate_a_list([1, 2, 2, 2, 3],9))