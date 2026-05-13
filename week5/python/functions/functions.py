#
#
# exercise 1
#
# def is_even(n):
#     return n % 2 == 0
#
# print(is_even(1))
#
#
# exercise 2
#
# def factorial(n):
#     result = 1
#     for num in range(n):
#         result += result * num
#     return result
#
# print(factorial(5))
#
#
# exercise 3
#
# def count_vowels(s):
#     counter = 0
#     for letter in s:
#         if letter in ["a","e","i","o","u"]:
#             counter += 1
#     return counter
#
# print(count_vowels("uei"))
#
#
# exercise 4
#
# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("abc"))
#
#
# exercise 5
#
# def find_max(lst):
#     max = lst[0]
#     for num in lst:
#         if num > max:
#             max = num
#     return max
#
# print(find_max([2,4,5,6,23]))
#
#
# exercise 6
#
# def celsius_to_fahrenheit(c):
#     return c * (9 / 5) + 32
#
# print(celsius_to_fahrenheit(34))
#
#
# exercise 7
#
# def is_palindrome(s):
#     palindrome = True
#     for i,letter in enumerate(s):
#         if not letter == s[-i-1]:
#             palindrome = False
#     return palindrome
#
# print(is_palindrome("asas"))
#
#
# exercise 8
#
# def even_numbers(lst):
#     for num in lst:
#         if not num % 2 == 0:
#             lst.remove(num)
#     return lst
#
# print(even_numbers([1,2,3,4,5,6,7,8,9,0]))
#
#
# exercise 9
#
# def is_anagram(s1,s2):
#     list_s2 = []
#     for letter in s2:
#         list_s2.append(letter)
#     for letter in s1:
#         if letter in list_s2:
#             list_s2.remove(letter)
#     if not list_s2:
#         return True
#     return False
#
# print(is_anagram("abaa","aaba"))
#
#
# exercise 10
#
# def word_count(s):
#     s_to_list = list(s.split(" "))
#     dicti_count = {}
#     for word in s_to_list:
#         if word.lower() not in dicti_count:
#             dicti_count[word] = 1
#         else:
#             dicti_count[word] += 1
#     return dicti_count
#
# print(word_count("aba ana aba"))
#
#
# exercise 11
#
# def calculate_resource_drain(cost,waste_factor):
#     return cost * waste_factor
#
# def get_net_resources(cost,waste_factor):
#     result = cost - calculate_resource_drain(cost,waste_factor)
#     return result
#
# print(get_net_resources(50,0.2))
#
#
# exercise 12
#
# def intercept_length(packet):
#     return len(packet)
#
# def verify_transmission(packet):
#     return f"Intercepted packet contains {intercept_length(packet)} bytes of data."
#
# print(verify_transmission("adsaecqc"))
#
#
# exercise 13
#
# import math
# def convert_to_decibels(signal_strength):
#     return 20 * math.log10(signal_strength/1)
#
# def is_threat_detected(signal_strength):
#     if convert_to_decibels(signal_strength) > 90:
#         return True
#     return False
#
# print(is_threat_detected(100))
#
#
# exercise 14
#
# The exercise isn't clearly

# def get_fuel_surcharge(distance):
#     return distance / 10 * 8 * 0.17
#
# def get_hazard_pay(distance):
#     return get_fuel_surcharge(distance) / 0.17 * 0.05
#
# def calculate_mission_cost(distance):
#     price = get_fuel_surcharge(distance) / 0.17
#     return f"The price is {price}, the fuel surcharge is {get_fuel_surcharge(distance)}, and the hazard pay is {get_hazard_pay(distance)}"
#
# print(calculate_mission_cost(100))