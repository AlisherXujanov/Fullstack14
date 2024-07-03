# 1. Write a function to count the occurrences of each character in a string.
# RU: Напишите функцию для подсчета вхождений каждого символа в строке.
# def count_occurences(string) -> dict: # подсчитать_вхождения
#     text = [string]
#     for x in text:
#         r = sum(x)

# word = ["shalala"]
# print(count_occurences(word))
# count_occurences("abaaa")
# {'a': 4,  "b": 1}
print("Task - 1: I cannot do it")

# =================================================================================
# =================================================================================
# 2. Write a Python script to concatenate the following dictionaries to create a new one.
# RU: Напишите скрипт Python для объединения следующих словарей для создания нового.

# def concatenate_dictionaries(*args) -> dict:
# x = {'a': 1, 'b': 2}
# x2 = {'c': 3, 'd': 4}
# x3 = {'e': 5, 'f': 6}
# x4 = {'g': 7, 'h': 8}
# concatenate_dictionaries(x, x2, x3, x4)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x = {'a': 1, 'b': 2}
x.update({
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
})
print(x)

# =================================================================================
# =================================================================================
# 3. Write a Python script to check whether a given key already exists in a dictionary.
# RU: Напишите скрипт Python для проверки, существует ли данный ключ уже в словаре.

# def check_key(dict, key):
#     ...
# check_key({"a": 1, "b": 2}, "a")  # True

dict = {"a": 1, "b": 2}
print(dict.get("c", False))

# =================================================================================
# =================================================================================
# 4. Write a Python program to iterate over dictionaries using for loops.
# RU: Напишите программу Python для итерации по словарям с помощью циклов for.


def iterate_over_dict(dict):
    ...


iterate_over_dict({'name': 'John',  'age': 26,  'address': 'London'})

# name: John
# age: 26
# address: London

# =================================================================================
# =================================================================================
# 5. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys.
# RU: Напишите скрипт Python для печати словаря, где ключи - числа
# от 1 до n (оба включены), а значения - квадрат ключей.
# ex: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# def generate_dict(n):
#     x = dict(n = n**n)
#     print(x)

# z = 5
# generate_dict(z)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Task - 5: I cannot do it")
# =================================================================================
# =================================================================================
# 6. Write a Python program to sum all the items in a dictionary.
# !!! NOTE: values could be int or str, if str, convert to int
# But, if the value is not convertible to int, skip it.
# ----------------
# RU: Напишите программу Python для суммирования всех элементов в словаре.
# !!! ПРИМЕЧАНИЕ: значения могут быть int или str, если str, преобразуйте в int
# Но, если значение нельзя преобразовать в int, пропустите его.
# ----------------
# ex:  x =  {...: "10", ...: 'qwe', ...: 5}  => 15
# ----------------


def sum_dict(dict):
    dict = ({
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    })
    # total = sum(value for value in dict if int(value))
    total = sum(dict.values())
    return total


print(sum_dict({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': "hello"
}))
# =================================================================================
# =================================================================================
# 7. Write a Python program to multiply all the items in a dictionary.
# !!! NOTE: values could be int or str, if str, convert to int
# But, if the value is not convertible to int, skip it.
# ----------------
# RU: Напишите программу Python для умножения всех элементов в словаре.
# !!! ПРИМЕЧАНИЕ: значения могут быть int или str, если str, преобразуйте в int
# Но, если значение нельзя преобразовать в int, пропустите его.
# ----------------
# {...: "10", ...: 'qwe', ...: 5}  => 50


def multiply_dict(dict):
    ...


multiply_dict({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
})
# 24
# =================================================================================
# =================================================================================
# 8. Write a Python program to remove a key from a dictionary.
# RU: Напишите программу Python для удаления ключа из словаря.


def remove_key(dc, _key):
    ...


remove_key({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}, 'b')
# {'a': 1, 'c': 3, 'd': 4}

# =================================================================================
# =================================================================================

# 9. Write a Python program to sort a given dictionary by key.
# RU: Напишите программу Python для сортировки заданного словаря по ключу.
# ------------
# ex: {5:"a",  7:"c",   2:"b"} => {2:"b",   5:"a",   7:"c"}
# ------------


def sort_dict_by_key(dict):
    ...


sort_dict_by_key({
    5: "a",
    7: "c",
    2: "b",
})
# {2: 'b', 5: 'a', 7: 'c'}
# =================================================================================
# =================================================================================
# 10. Write a Python program to get the maximum and minimum value in a dictionary.
# RU: Напишите программу Python для получения максимального и минимального значения в словаре.
# ------------
# ex: {'x':500, 'y':5874, 'z': 560, 'a': 7, 'b': 35, 'c': 113}
# ------------


def get_max_min(dict):
    ...


get_max_min({
    'x': 500,
    'y': 5874,
    'z': 560,
    'a': 7,
    'b': 35,
    'c': 113,
})
# 5874, 7
# =================================================================================
# =================================================================================
