# ========================================
# ========================================
# type()  =>  shows the datatype of the variable
# x = 123
# z = "..."
# print(type(x))
# print(type(z))
# ========================================
# ========================================
# int()     -> 1, 2, 3
# float()   -> 1.0,  2.012,  3.14
# ========================================
# ========================================
# x = 123
# print(x)
# del x
# print(x)
# ========================================
# ========================================
# sequence =>  [..., ...], (..., ...), "...", range
# len(...)  -> shows the length of the sequence
# x = [1, 2, 3, 4, 5]
# print(len(x))
# z = 'Hello world'
# print(len(z))
# ========================================
# ========================================
# function test() {}   ->  in JS
# ----------
# def test():
#     print('...')
#     print('...')
#     print('...')
# ----------
# def sum_up(a, b, c):
#     print(a + b + c)

# # sum_up(10)
# sum_up(2, 2, 10)
# ----------
# ========================================
# ========================================
# input()  =>  prompt()
# --------
# IF ELSE 

# In JS
# if (условие==true) { прочитать код }
# else {}
# --------
# In Python
# if условие == true:  ....
# else: ...
def get_input():
    answer = input('Enter a number: ')
    if answer.isnumeric(): # '123'
        print(int(answer) + 10)
    else:
        print('Please enter a number')


# NOTE: 2 types can never be added together
#      RU: 2 типа нельзя сложить вместе
# ========================================
# ========================================
# e  -> in calculations
# print(2e2)   # 200
# print(2e5)   # 200000
# print(2e10)  # 20000000000
# ========================================
# Python has several built-in data types. 
# Here are the most commonly used ones:

# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Text Sequence Type: str
# Binary Sequence Types: bytes, bytearray, memoryview
# Set Types: set, frozenset
# Mapping Type: dict
# Boolean Type: bool
# None Type: None

# Bool   =>   bool()

# 1 ==  True
# 0 ==  False

# "", [], {}, (), False, 0, None  => Negatives
# Everything else is              => True

# x = 123
# result = bool(x)
# print("Result is: ", result)

# ------------------------------------------------------------------
# `${variable}`  -> in JS
# f"{variable}"  -> in Python

# If / elif / else 

# if 1!=2:
#     print(f'1 != 2 is => {1==2}')
# elif 1==1:
#     print(f'1 == 1 is => {1==1}')
# else:
#     print(1==2)
# ------------------------------------------------------------------
# match / case
HTTPS_status = 200
# if HTTPS_status == 200 or HTTPS_status == 201:
#     print('OK')
# elif HTTPS_status == 404:
#     print('Not found')
# elif HTTPS_status == 301 or HTTPS_status == 302:
#     print('Redirect')
# else:
#     print('Unknown')

# match HTTPS_status:
#     case 200 | 201:
#         print('OK')
#     case 404:
#         print('Not found')
#     case 301 | 302:
#         print('Redirect')
#     case _:
#         print('Unknown')
# ------------------------------------------------------------------

# EXERCISES
# 1. Reverse and input from a user    &&    Reverse a number
# RU: 
#     Берите текст от клиента и выведите на терминале. 
#     Найти зеркальное число.
# inp = input("What is your name: ")
# print("Polindrome: ", inp[::-1] == inp)
# print(str(num)[::-1])
# ----------------------------------------------------------
# Напишите логику, которая проверяет, является ли число положительным, отрицательным или нулем. 
# number = 0
# # Positive  ||  Negative  ||  Zero
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")
# ----------------------------------------------------------
# Напишите логику, которая проверяет, четное число или нет.
# number = ...
# # Even || Odd
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# ----------------------------------------------------------
# Напишите логику, которая проверяет, кратно ли число на 3 и 5 одновременно.
# (делится ли число и на 3 и на 5 одновременно без остатка)
# number = 6
# if number % 3 == 0 and number % 5 == 0:
#     print("Yes")
# else:
#     print("No")
# ----------------------------------------------------------
# Напишите логику, которая проверяет, пустая строка или нет
# text = "..."
# if len(text) == 0:
# # if text == "":
#     print("Empty")
# else:
#     print("Not empty")
# ----------------------------------------------------------
# print("O" in "Hello")
# Напишите логику, которая проверяет, содержит ли строка определенный символ.
# text = "..."
# symbol = "$"
# # print(symbol in text)
# if symbol in text:
#     print("Yes")
# else:
#     print("No")
