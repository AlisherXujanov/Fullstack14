# 1. Write a function to count the occurrences of each character in a string.
# RU: Напишите функцию для подсчета вхождений каждого символа в строке.
def count_occurences(string: str) -> dict:  # подсчитать_вхождения
    result = {}
    for letter in string:
        if result.get(letter, None):
            result[letter] += 1
        else:
            result[letter] = 1
    return result


r = count_occurences("abaaa")
# print(r)
# {'a': 4,  "b": 1}


# =================================================================================
# =================================================================================
# 2. Write a Python script to concatenate the following dictionaries to create a new one.
# RU: Напишите скрипт Python для объединения следующих словарей для создания нового.

def concatenate_dictionaries(*args: list[dict]) -> dict:
    result = {}
    for d in args:
        result.update(d)
    return result


x = {'a': 1, 'b': 2}
x2 = {'c': 3, 'd': 4}
x3 = {'e': 5, 'f': 6}
x4 = {'g': 7, 'h': 8}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
r = concatenate_dictionaries(x, x2, x3, x4)
# print(r)

# =================================================================================
# =================================================================================
# 3. Write a Python script to check whether a given key already exists in a dictionary.
# RU: Напишите скрипт Python для проверки, существует ли данный ключ уже в словаре.


def check_key(dict, key):
    return dict.get(key, False)


r = check_key({"a": 1, "b": 2}, "a")  # True
# print(r)

# =================================================================================
# =================================================================================
# 4. Write a Python program to iterate over dictionaries using for loops.
# RU: Напишите программу Python для итерации по словарям с помощью циклов for.


def iterate_over_dict(dict):
    for key, val in dict.items():
        print(f"{key}: {val}")


iterate_over_dict({'name': 'John', 'age': 26, 'address': 'London'})
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
def generate_dict(n: int) -> dict:
    result = {}
    for i in range(1, n+1):
        result[i] = i ** 2  # i*i
    return result

r = generate_dict(5)
# print(r)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
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


def sum_dict(object: dict) -> int:
    vals = object.values()
    result = 0
    words = []
    for val in vals:
        val = str(val)
        if val.isnumeric():
            result += int(val)
        else:
            words.append(val)
    return result, words


r = sum_dict({
    'a': 1,
    'b': "2",
    'c': "3",
    'd': 4,
    'e': "Hello"
})
# print(r)   # 10, ['Hello']

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


def multiply_dict(object: dict) -> int:
    vals = object.values()
    result = 1
    words = []
    for val in vals:
        val = str(val)
        if val.isnumeric():
            result *= int(val)
        else:
            words.append(val)
    return result, words


r = multiply_dict({
    'a': 1,
    'b': "2",
    'c': "3",
    'd': 4,
    'e': "Hello"
})
# print(r)   # 24
# =================================================================================
# =================================================================================
# 8. Write a Python program to remove a key from a dictionary.
# RU: Напишите программу Python для удаления ключа из словаря.


def remove_key(dc: dict, _key: str) -> dict:
    dc_copy = dc.copy()
    del dc_copy[_key]
    return dc_copy


r = remove_key({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}, 'b')
# print(r)
# {'a': 1, 'c': 3, 'd': 4}

# =================================================================================
# =================================================================================

# 9. Write a Python program to sort a given dictionary by key.
# RU: Напишите программу Python для сортировки заданного словаря по ключу.
# ------------
# ex: x = {5:"a",  7:"c",   2:"b"} => {2:"b",   5:"a",   7:"c"}
# ------------


def sort_dict_by_key(object: dict) -> dict:
    keys = sorted(object.keys())
    result = {}
    for key in keys:
        result[key] = object[key]
    return result
    # --------------------------------------
    # return {key: object[key] for key in sorted(object.keys())}


r = sort_dict_by_key({
    5: "a",
    7: "c",
    2: "b",
})
# print(r)
# {2: 'b', 5: 'a', 7: 'c'}
# =================================================================================
# =================================================================================
# 10. Write a Python program to get the maximum and minimum value in a dictionary.
# RU: Напишите программу Python для получения максимального и минимального значения в словаре.
# ------------
# ex: {'x':500, 'y':5874, 'z': 560, 'a': 7, 'b': 35, 'c': 113}
# ------------


def get_max_min(object: dict) -> tuple:
    vals = list(object.values())
    minimal, maximal = vals[0], 0
    for i in vals:
        if i < minimal:
            minimal = i
        elif i > maximal:
            maximal = i
    return maximal, minimal
    # --------------------------------------
    # return max(object.values()), min(object.values())

r = get_max_min({
    'x': 500,
    'y': 5874,
    'z': 560,
    'a': 7,
    'b': 35,
    'c': 113,
})
# print(r)
# 5874, 7
