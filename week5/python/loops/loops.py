# exercise 1
# for number in range(1,10):
#     if number % 2 == 0:
#         continue
#     elif number == 7:
#         break
#     else:
#         print(number)

# exercise 2
# password = "1234"
# while True:
#     user_password = input("Please enter your password: ")
#     if user_password == password:
#         print("Welcome!")
#         break
#     else:
#         print("Try again")
# because we don't know when the user will enter a correct password

# exercise 3
# listi = []
# while True:
#     item = input("Please enter the name of your item name or exit: ")
#     if item.lower() != "exit":
#         listi.append(item)
#     else:
#         print(listi)
#         break
# because we don't know when the user will enter to exit

# exercise 3 B

# for row in range(1,4):
#     for col in range(1,4):
#         if col == 2:
#             break
#         print(row, col)

# exercise 4
# vowels_counter = 0
# user_str = input("Please enter a string: ")
# for letter in user_str:
#     if letter in ["a", "e", "i", "o", "u"]:
#         vowels_counter += 1
# print(vowels_counter)
# yes! the outer loop keep going

# exercise 5
# for num1 in range(1,6):
#     for num2 in range(1,6):
#         print(f"{num1} * {num2} = {num1 * num2}")

# exercise 6
# user_str = input("Please enter a string: ")
# accumulator = ""
# for letter in user_str:
#     accumulator = letter + accumulator
# print(accumulator)

# exercise 7
# num = int(input("Please enter a int number: "))
# counter = 0
# while num > 0:
#     digit_of_unity = num % 10
#     if digit_of_unity % 2 == 0:
#         counter += 1
#     num = num // 10
# print(counter)

# exercise 8
# stri = input("Please enter a string: ")
# new_str = ""
# for letter in stri:
#     new_str += letter * 2
# print(new_str)

# exercise 9
# highest_number = 0
# while True:
#     num = int(input("Please enter a number: "))
#     if num > highest_number:
#         highest_number = num
#     if num == 0:
#         break
# print(highest_number)

# exercise 10
# stri = input("Please enter a string: ")
# special_characters = ""
# for char in stri:
#     if not 96 < ord(char.lower()) < 123 and not 47 < ord(char) < 58:
#         special_characters += char
# if special_characters:
#     print(False)
#     print(special_characters)
# else:
#     print(True)

# exercise 11
# num = int(input("Please enter a number: "))
# new_num = 0
# while num > 0:
#     digit_of_unity = num % 10
#     new_num = new_num * 10
#     new_num += digit_of_unity * 10
#     num = num // 10
# print(new_num // 10)