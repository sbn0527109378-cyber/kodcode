# exercise 1
# age = int(input("Please enter your age: "))
# if not 0 < age < 121:
#     print("Invalid")
# elif age > 17:
#     print("Adult")
# elif age > 12:
#     print("Teen")
# else:
#     print("Child")

# exercise 2
# char = input("Please enter a char: ")
# vowel = ["a","e","i","o","u"]
# if not 96 < ord(char.lower()) < 123:
#     print("Invalid")
# else:
#     if char in vowel:
#         print("Vowel")
#     else:
#         print("Consonant")

# exercise 3
# age = int(input("Please enter your age: "))
# vip_card = input("Please enter yes if you have a VIP card and no if you do not: ")
# if age < 16:
#     print("You don't have permission")
# elif age in [19,20,21]:
#     print("You have permission")
# else:
#     if vip_card == "yes":
#         print("You have permission")
#     else:
#         print("You don't have permission")

# exercise 4
# passwd = "98765432"
# user_passwd = input("Please enter your password: ")
# if user_passwd == passwd:
#     print("Access Granted")
# else:
#     if len(user_passwd) < 8:
#         print("Too short")
#     else:
#         print("Wrong password")

# exercise 5
# x = int(input("Please enter a width between 10 and 50: "))
# y = int(input("Please enter a length between 20 and 80: "))
# if not 10 <= x <= 50 or not 20 <= y <= 80:
#     print("Outside the rectangle")
# elif x == 10 or x == 50 or y == 20 or y == 80:
#     print("On the edge")
# else:
#     print("Inside the rectangle")

# exercise 6
# name = input("Please enter your name: ")
# print(f"Hello {name or "Anonymous"}")

# their is no exercise 7

# exercise 8
# num1 = int(input("Please enter your first number: "))
# num2 = int(input("Please enter your second number: "))
# num3 = int(input("Please enter your third number: "))
# len_of_positive = int(0 < num1) + int(0 < num2) + int(0 < num3)
# print(len_of_positive)

# their is no exercise 9

# exercise 10
# score = int(input("Please enter your score between 0 and 100: "))
# grade = "F" if score < 70 else "C" if 70 <= score < 80 else "B" if 80 <= score < 90 else "A"
# print(grade)