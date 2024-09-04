# HOMEWORK
# NOTE: use functions

# 1 - use simple loop (simple logic)
# 2 - use list comprehension

# =====================================================
# =====================================================

# 1. Write a Python program to multiplies all the items in a list.
# RU: Напишите программу Python, чтобы умножить все элементы в списке.

# def multiply_list_items(l:list) ->  int:
# [1] * 2  =>   [1, 1]
# 'a' * 2  =>   'aa'
# --------------------
# result = 1
# for n in l:
#     result *= n
# return result
# --------------------
# result = 1
# result = [result := result * num for num in l][-1]
# return result

# r = multiply_list_items([1, 2, 3, 4, 5])  # 120
# print("Result:", r)
# =====================================================
# x = lambda a, b: a + b
# z = x(1, 2)
# if z > 0:
# if (z := x(-10, 2)) > 0:
#     print("Positive", z)
# else:
#     print("Negative")
# =====================================================
# =====================================================
# 2.  Write a Python program to count the number of strings from a given
# list of strings. The string length is 2 or more and
# it should have first 2 and last two same in reversed order
# RU: Напишите программу Python, чтобы подсчитать количество строк из данного
# списка строк. Длина строки 2 или более и
# она должна иметь первые 2 и последние две одинаковые в обратном порядке

# ['abc', 'xyz', 'aba', '1212381923128321']
#              ab == ba      12  == 21
# Expected Result : 2

# def find_same_characters(l: list) -> int:
#     result = 0
#     items = []
#     # -------------------------------------
#     # LOGIC WITH SIMPLE LOOP
#     for item in l:
#         if len(item) >= 2:
#             if item[:2] == item[-2:][::-1]:
#                 result += 1
#                 items.append(item)
#     # =====================================
#     # LOGIC WITH LIST COMPREHENSION
#     # result = [(result := result + 1, items.append(i))
#     #          for i in l if len(i) >= 2 and i[:2] == i[-2:][::-1]
#     #          ][-1][0]
#     # -------------------------------------
#     return result, items

# r, i = find_same_characters(
#     ['abc', 'xyz', 'aba', '1212381923128321', 'waaw', 'wab'])
# print("Result:", r)
# print("Items:", i)
# =====================================================
# =====================================================
