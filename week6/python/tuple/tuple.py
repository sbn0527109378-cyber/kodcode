

# exersice 1

# def sum_of_a_tuple(tupi):
#     sumi = 0
#     for num in tupi:
#         sumi += num
#     return sumi
#
# print(sum_of_a_tuple((1, 2, 3, 4, 5)))


# exersice 2

# def maximum_element(tupi):
#     maxi = tupi[0]
#     for num in tupi:
#         if num > maxi:
#             maxi = num
#     return maxi
#
# print(maximum_element((3, 7, 2, 8, 5)))


# exersice 3

# def count_occurrences(tupi,value):
#     counter = 0
#     for num in tupi:
#         if num == value:
#             counter += 1
#     return counter
#
# print(count_occurrences((1, 2, 3, 2, 4, 2),2))


# exersice 4

# def reverse_a_tuple(tupi):
#     new_tupi = ()
#     for i in range(-1,(-len(tupi)-1),-1):
#         new_tupi += tupi[i],
#     return new_tupi
#
# print(reverse_a_tuple((1, 2, 3, 4)))


# exersice 5

# def swap_pairs(tupi):
#     new_tupi = ()
#     for i in range(0,len(tupi),2):
#         new_tupi += (tupi[i + 1], tupi[i])
#     return new_tupi
#
# print(swap_pairs((1, 2, 3, 4, 5, 6)))


# exersice 6

# def min_and_max(tupi):
#     mini = tupi[0]
#     maxi = tupi[0]
#     for num in tupi:
#         if num > maxi:
#             maxi = num
#         elif num < mini:
#             mini = num
#     return mini, maxi
#
# print(min_and_max((4, 1, 7, 3, 5)))


# exersice 7

# def distance_between_points(tupi1,tupi2):
#     return ((tupi1[0] - tupi2[0]) ** 2 + (tupi1[1] - tupi2[1]) ** 2) ** 0.5
#
# print(distance_between_points((0, 0), (3, 4)))


# exersice 8

# def merge_and_sort(tupi1,tupi2):
#     sorted_tupi = tuple(sorted(tupi1 + tupi2))
#     return sorted_tupi
#
# print(merge_and_sort((3, 1, 4), (1, 5, 9)))


# exersice 9

# def frequency_table(tupi):
#     new_tupi = ()
#     for char in tupi:
#         temp_tupi = (char,tupi.count(char))
#         if temp_tupi not in new_tupi:
#             new_tupi += temp_tupi,
#     return tuple(new_tupi)
#
# print(frequency_table(("a", "b", "a", "c", "b", "a")))


# exersice 10

# def rotate_a_tuple(tupi, k):
#     k = k % len(tupi)
#     return tuple(tupi[-k:]) + tuple(tupi[:-k])
#
# print(rotate_a_tuple((1, 2, 3, 4, 5),2))