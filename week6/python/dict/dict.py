

# exersice 1
# def sum_of_values(dicti):
#     sumi = 0
#     for value in dicti.values():
#         sumi += value
#     return sumi
#
# print(sum_of_values({"a": 1, "b": 2, "c": 3}))


# exersice 2

# def key_with_maximum_value(dicti):
#     maxi = None
#     for key in dicti:
#         if maxi is None or dicti[key] > maxi:
#             maxi = dicti[key]
#             key_maxi = key
#     return key_maxi
#
# print(key_with_maximum_value({"a": 3, "b": 7, "c": 5}))


# exersice 3

# def count_characters(stri):
#     dicti = {}
#     for char in stri:
#         if char not in dicti:
#             dicti[char] = stri.count(char)
#     return dicti
#
# print(count_characters("banana"))


# exersice 4

# def invert_a_dictionary(dicti):
#     new_dict = {}
#     for key, value in dicti.items():
#         new_dict[value] = key
#     return new_dict
#
# print(invert_a_dictionary({"a": 1, "b": 2, "c": 3}))


# exersice 5

# def merge_two_dictionaries(dict1, dict2):
#     new_dict = {}
#     for key, value in dict1.items():
#         new_dict[key] = value
#     for key, value in dict2.items():
#         new_dict[key] = value
#     return new_dict
#
# print(merge_two_dictionaries({"a": 1, "b": 2}, {"b": 20, "c": 30}))


# exersice 6

# def filter_by_value(dicti, num):
#     new_dict = {}
#     for key, value in dicti.items():
#         if value > num:
#             new_dict[key] = value
#     return new_dict
#
# print(filter_by_value({"a": 1, "b": 5, "c": 3, "d": 8},3))


# exersice 7

# def group_by_first_letter(list_of_words):
#     new_dict = {}
#     for word in list_of_words:
#         if word[0] not in new_dict:
#             new_dict[word[0]] = []
#         if word not in new_dict[word[0]]:
#             new_dict[word[0]].append(word)
#     return new_dict
#
# print(group_by_first_letter(["apple", "ant", "banana", "berry", "cherry"]))


# exersice 8

# def word_frequency(stri):
#     dicti = {}
#     for word in stri.split(" "):
#         if word not in dicti:
#             dicti[word] = stri.count(word)
#     return dicti
#
# print(word_frequency("the cat sat on the mat"))


# exersice 9

# def common_keys(dict1, dict2):
#     list_of_keys = [key for key in dict1 if key in dict2]
#     return list_of_keys
#
# print(common_keys({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7}))


# exersice 10

# def most_frequent_value(dicti):
#     appears_most_often = 0
#     for value in dicti.values():
#         if list(dicti.values()).count(value) > list(dicti.values()).count(appears_most_often):
#             appears_most_often = value
#     return appears_most_often
#
# print(most_frequent_value({"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}))