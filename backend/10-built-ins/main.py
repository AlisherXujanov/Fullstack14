# 1. max()
# Return the largest item in an iterable or the largest of two or more arguments.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.

# If one item is given, it should be iterable. The largest item in the iterable is returned.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.
# max(iterable, *[, key, default])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(max(nums)) # 10

words = ['apple', 'bananaaa', 'cherry', 'elderberry', 'date']
# -------------------------------------------
# print(max(words, key=len))  # =>  elderberry
# [5,        6,        6,       10,           4     ]  =>  10
# ['apple', 'banana', 'cherry', 'elderberry', 'date']  =>  'elderberry'
# -------------------------------------------
# [2,        5,          1,        3,           2     ]
# ['apple', 'bananaaa', 'cherry', 'elderberry', 'date']  =>  'bananaaa'
# def get_vowels(word:str) -> int:
#     return len([letter for letter in word if letter.lower() in 'aeiou'])

# print(max(words, key=get_vowels))  # =>  bananaaa
# -------------------------------------------
# print(max([], default=0))
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------



# If two or more positional arguments are provided, the largest of the positional arguments is returned.
# RU: Если предоставлено два или более позиционных аргумента, возвращается наибольший из позиционных аргументов.
# max(arg1, arg2, *args[, key])

# There are two optional keyword-only arguments.
# RU: Есть два необязательных аргумента только ключевых слов.

# key- key function where the iterables are passed and comparison is performed based on its return value
# RU: key- ключевая функция, в которой передаются итерируемые объекты,
# и сравнение выполняется на основе возвращаемого значения
# EX:
#   iterable = ['geeks', 'code', 'python', 'java']
#   max(iterable, key=len)  =>  'python'
# iterable = [30, 15, 20, 25, 30]
# print(max(iterable, key=lambda x: x%15))  # => 25
#   => here the remainder after dividing each element by
#      15 is calculated and the maximum of those values is returned
#      ex:  10%15 = 10,  15%15 = 0,  20%15 = 5,  25%15 = 10,  30%15 = 0

# The default argument specifies an object to return if the provided iterable is empty.
# If the iterable is empty and the default is not provided, a ValueErrors raised.
# EX:
#   iterable = []
#   max(iterable, default=100)  =>  100
#   max(iterable)  =>  ValueError: max() arg is an empty sequence
# ==================================
# 2. min()         Works the same way as max(), but returns the smallest value

# ===========================================================================================
# 3. map()         Returns a map object (which is an iterator) of the results after applying the
#               given function to each item of a given iterable (list, tuple etc.)
#           RU: Возвращает объект отображения (который является итератором) результатов после применения
#               заданной функции к каждому элементу заданного итерируемого объекта (список, кортеж и т. Д.)
#           EX:
#               def wordCount(n):
#                   return len(n)
#               # Or we could use:
# wordCount = lambda n: len(n)
# x = map(wordCount, ('apple', 'banana', 'cherry'))
# print(x)        # => [5, 6, 6]
# print(list(x))  # => [5, 6, 6]
# ------------------------------------------------------------------------------
# 4. filter()      Use a filter function to exclude items in an iterable object
#           RU: Используйте функцию фильтра, чтобы исключить элементы в итерируемом объекте
#           EX:
#               def myFunc(n):
#                   # if n > 18:
#                   #     return True
#                   # else:
#                   #     return False
#                   -------------------
#                   # return True if n > 18 else False
#                   -------------------
#                   return n > 18

#               x = filter(myFunc, (5, 7, 18, 25, 32))
#               print(list(x))  =>  [25, 32]
# NOTE: The callback function should return True/False
# depending on the value in the iterable
# RU: Функция обратного вызова должна возвращать True / False
# в зависимости от значения в итерируемом объекте
# ------------------------------------------------------------------------------
# 5. reduce()      Use a function to reduce an iterable to a single value
#           RU: Используйте функцию для сокращения итерируемого объекта до одного значения
#           EX:
from functools import reduce
# def myFunc(acc, next):
#     """
#         acc  - accumulator
#         next - next value
#         NOTE: the initial value of the accumulator is the first value of the iterable
#               if not given as last argument
#     """
#     return acc + next
#     # return acc if acc > next else next

# x = reduce(myFunc, (1, 2, 3, 4))
# print(x)  # =>  10

# x = map(lambda x: x*2, arr)
# print(list(x))


# def myFunc(current, next):
#     if current > next:
#         print("current > next", current)
#         return current
#     else:
#         print("current > next", next)
#         return next
# arr = [11, 22, 3, 4515, 56]
# res = reduce(myFunc, arr)
# print(res)
