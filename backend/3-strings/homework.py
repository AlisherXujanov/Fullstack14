# 1. Write a function to swap the first and last characters in a string.
# RU: Напишите функцию, чтобы поменять местами первый и последний символы в строке.
# =================================================================================
# =================================================================================
# 2. Write a function to reverse a string.
# RU: Напишите функцию, чтобы перевернуть строку.
# =================================================================================
# =================================================================================
# 3. Write a function to remove the nth index character from a n onempty string.
# RU: Напишите функцию, чтобы удалить символ с индексом n из непустой строки.
# =================================================================================
# =================================================================================
# 4. Write a function to remove the characters which have odd index values of a given string.
# RU: Напишите функцию, чтобы удалить символы, которые имеют нечетные индексы заданной строки.
# text = "Hello, World!"
# print(text[::2])
# =================================================================================
# =================================================================================
# 5. Write a Python script that takes input from the user and displays
# that input back in upper and lower cases.
# RU: Напишите скрипт Python, который принимает ввод от пользователя и
# отображает этот ввод в верхнем и нижнем регистрах.
# answer = input("Write something: ")
# print(answer.lower())
# print(answer.upper())
# =================================================================================
# =================================================================================
# 6. Write a function to find the second most frequent character in a given string.
# RU: Напишите функцию, чтобы найти второй наиболее часто встречающийся символ в данной строке.
# второй_наиболее_часто_встречающийся
# for loop
# function
# algorithm
# =================================================================================
# =================================================================================
# 7. Write a function to convert a given string into a list of integers.
# RU: Напишите функцию, чтобы преобразовать заданную строку в список целых чисел.
# "123..."  =>  [1, 2, 3 ...]
# number_as_str = "123456"
# result = [int(n) for n in list(number_as_str)]
# print("Result:", result) # =>  [1, 2, 3, 4, 5, 6]
# =================================================================================
# =================================================================================
# 8. Write a function to check if a given string is a palindrome.
# RU: Напишите функцию, чтобы проверить, является ли заданная строка палиндромом.
# =================================================================================
# =================================================================================
# 9. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# RU: Напишите программу на Python, чтобы получить строку, состоящую из первых 2 и последних 2 символов заданной строки.
# Если длина строки меньше 2, вместо этого верните пустую строку.
# text = "Hello, World!"
# if len(text) <= 2:
#     print("...")
# else:
#     print(text[:2] + text[-2:])
# =================================================================================
# =================================================================================
# 10. Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# RU: Напишите программу на Python, чтобы получить строку из заданной строки, где все вхождения ее первого символа
# были заменены на '$', кроме самого первого символа.

# INPUT:   =>  "This is test text"
# OUTPUT:  =>  "This is $es$ $ex$"
# изменить_первый_символ
# =================================================================================
# =================================================================================
# 11. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# RU: Напишите программу на Python, чтобы получить одну строку из двух заданных строк,
# разделенных пробелом и поменять местами первые два символа каждой строки.
# text = "Hello, world!"  # --  "Wello, horld!"
# splitted_text = text.split()
# first = splitted_text[0]
# last = splitted_text[1]

# result = last[0].upper() + first[1:] + " " + first[0].lower() + last[1:]
# print(result)
# =================================================================================
# =================================================================================
# 12. Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with
# 'ing', add 'ly' instead. If the string length of the given string
# is less than 3, leave it unchanged.
# RU: Напишите программу на Python, чтобы добавить 'ing' в конец заданной строки (длина должна быть не менее 3).
# Если заданная строка уже заканчивается на 'ing', вместо этого добавьте 'ly'.
# Если длина строки заданной строки меньше 3, оставьте ее без изменений.
# text = input("Enter a text: ") # ...
# if len(text) >= 3:
#     if text.endswith("ing"):
#         print(text + "ly")
#     else:
#         print(text + "ing")
# else:
#     print(text)
# =================================================================================
# =================================================================================
# 13. Write a Python program to find the first appearance of the
# substrings 'not' and 'poor' in a given string. If 'not' follows 'poor',
# replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# RU: Напишите программу на Python, чтобы найти первое появление подстрок «не» и «плохо» в заданной строке.
# Если «не» перед «плохо» стоит, замените всю подстроку  `«не» ... «плохо»` на «хорошо».
# Вернуть полученную строку.
# text = input("Enter a text: ")
# # "The lyrics is not that poor!"
# # text = "The lyrics is that good!"
# indexOfNot = text.find("not")
# indexOfPoor = text.find("poor")

# if indexOfPoor and indexOfNot:
#     if indexOfPoor > indexOfNot:
#         text = text.replace('not ', '')
#         text = text.replace('poor', 'good')

# print(text)
# =================================================================================
# =================================================================================
# 14. Write a Python function to create an HTML string with tags around the word(s)
# RU: Напишите функцию Python для создания HTML-строки с тегами вокруг слова (слов).
# tag = input("Enter a tag: ")
# print(f"<{tag}>...</{tag}>")
# =================================================================================
# =================================================================================
# 15. Write a Python function to insert a string in the middle of a string.
# RU: Напишите функцию Python для вставки строки посередине строки.
# text = "Hello world!"
# MIDDLE = len(text) // 2

# random_text = "..."
# print(text[:MIDDLE] + random_text + text[MIDDLE:])
# =================================================================================
# =================================================================================
# 16. You have a str and get last two letters and repeat them 4 times
# RU: У вас есть строка и получите последние две буквы и повторите их 4 раза
# text = "Hello, World!"
# print(text[-2:] * 4)
# =================================================================================
# =================================================================================
# 17. Write a Python function to get the first half of a specified string of even length.
# RU: Напишите функцию Python, чтобы получить первую половину заданной строки четной длины.
# text = "Hello world!"
# if len(text)%2 == 0:
#     MIDDLE = len(text)//2
#     print(text[:MIDDLE])
# else:
#     print("NOT EVEN")
# =================================================================================
# =================================================================================
# 19. Write a Python program to concatenate two strings and return the result.
# If the length of the strings are not same then remove the characters from the longer string.
# RU: Напишите программу на Python для объединения двух строк и верните результат.
# Если длины строк не одинаковы, то удалите символы из более длинной строки.
# text1 = "Hello "
# text2 = "World!..."
# if len(text1) > len(text2):
#     print(text1[:len(text2)] + text2)
# elif len(text1) < len(text2):
#     print(text1 + text2[:len(text1)])
# else:
#     print(text1 + text2)
# =================================================================================
# =================================================================================
# 20. Write a Python function to convert a given string to all uppercase if it contains
# at least 2 uppercase characters in the first 4 characters.
# RU: Напишите функцию Python для преобразования заданной строки в верхний регистр,
# если она содержит не менее 2 заглавных символов в первых 4 символах.
# text = "Hello world!"
# # HeLlo world! => HELLO WORLD!
# # Hello world! => Hello world!
# alpha = "abcdefghijklmnopqrstuvwxyz"
# alpha_upper = alpha.upper()

# counter = 0
# if text[0] in alpha_upper: counter += 1
# if text[1] in alpha_upper: counter += 1
# if text[2] in alpha_upper: counter += 1
# if text[3] in alpha_upper: counter += 1

# if counter >= 2:
#     print(text.upper())
# else:
#     print(text)