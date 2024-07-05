# =============== BEGINNER LEVEL ===============
# 1. Создайте объект под названием car с следующими
#   свойствами: brand, model, color, year.
#   Выведите каждое свойство в консоль.

import random


def car(dict) -> dict:
    for key, value in dict.items():
        print(f"{key} : {value}")


obj = {"brand": "Mercedes", "model": "Mercedes-Benz G-класс",
       "color": "Black", "year": "1979"}
# print("Task - 1:", car(obj))

# --------------------------------------------------------------------------------------------------
# 2. У вас есть объект, получите длину ключей и значений объекта.


def lengths(object: dict) -> dict:
    return len(object.keys())


obj = {"name": "shamana", "age": "18"}
# print(lengths(obj))
# --------------------------------------------------------------------------------------------------
# 3. Создайте функцию, которая принимает объект и ключ в качестве
#   параметров. Затем удалите ключ из объекта и верните
#   оставшийся объект.


def removed(obj: dict, key: str) -> dict:
    del obj[key]
    return obj


# obj = {"a": 1, "b": 2, "c": 3}
# print("Task - 3:", removed(obj, "c"))

print("=============== INTERMEDIATE LEVEL ===============")

# 1. Создайте функцию, которая принимает объект в качестве параметра
#   и возвращает сумму всех значений, которые являются числами.


def sum_dict(object: dict) -> dict:
    return sum([int(item) for item in object.values() if str(item).isnumeric()])
    # vals = object.values()
    # result = 0
    # for val in vals:
    #     val = str(val)
    #     if val.isnumeric():
    #         result += int(val)
    # return result


r = sum_dict({"a": 5, "b": "10", "c": "abc", "d": 15})
# print("Task - 1:", r)
# ------------------------------------------------------------------------------
# 2. Создайте функцию, которая принимает объект в качестве параметра
#   и преобразует каждый ключ в обратный регистр (назад-вперёд)
#   и возвращает новый объект.


def new_obj(object: dict) -> dict:
    # result = {}
    # for key, value in object.items():
    #     key = key[::-1]
    #     result[key] = value
    # return result
    # ----------------------------------
    return {key[::-1]: val for key, val in object.items()}


result = {"school": 23, "floor": 3, "room": "biology"}
# print("Task -2:", new_obj(result))
# ------------------------------------------------------------------------------
# 3. Создайте функцию, которая принимает столько объектов, сколько
#   захотите, и возвращает объект, который содержит все ключи
#   и значения переданных объектов.


def unite_objects(*args: list[dict]) -> dict:
    # result = {}
    # for obj in args:
    #     result.update(obj)
    # return result
    # -----------------------------------
    return {key: val for nested_obj in args for key, val in nested_obj.items()}


obj1 = {"a": 1, "b": 2}
obj2 = {"c": 3, "d": 4}
obj3 = {"e": 5, "f": 6}

r = unite_objects(obj1, obj2, obj3)
# print("Task - 3:", r)
# ------------------------------------------------------------------------------
# 4. Создайте функцию, которая принимает объект в качестве параметра
#   и возвращает объект, отсортированный по его ключам


def sort_dict_by_key(object: dict) -> dict:
    keys = sorted(object.keys())
    result = {}
    for key in keys:
        result[key] = object[key]
    return result


r = {
    5: "a",
    7: "c",
    2: "b",
}
# print("Task - 4:", sort_dict_by_key(r))
# ------------------------------------------------------------------------------
# 5. Создайте функцию, которая принимает объект в качестве параметра
#   и возвращает объект, отсортированный по его значениям (а не ключам).


def sort_dict_by_value(object: dict) -> dict:
    result = {}

    for val in sorted(object.values()):
        for key2, val2 in object.items():
            if val2 == val:
                result[key2] = val
    return result


r = {
    2: "c",
    1: "a",
    3: "b",
}
# print("Task - 5:", sort_dict_by_value(r))

print("=============== ADVANCED LEVEL ===============")
# 1. Напишите функцию, чтобы подсчитать, сколько раз каждое значение
#   встречается в объекте.


def count_val(dict) -> dict:
    # vals = list(dict.values()) # ['abc', 'bdc', 'abc']
    # result = {} # {}
    # for val in vals: # each value in vals
    #     # result['abc'] = 2
    #     result[val] = vals.count(val)
    # return result
    # --------------------------------------------------
    return {value: list(dict.values()).count(value) for key, value in list(dict.items())}


r = {"a": "abc", "b": "bdc", "c": "abc"}
# print(count_val(r))
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 2. Напишите функцию, чтобы получить копию объекта, где ключи стали
#   значениями, а значения ключами.


def new_obj(object: dict) -> dict:
    # result = {}
    # for key, val in object.items():
    #     result[val] = key
    # return result
    # -----------------------------------
    return {val: key for key, val in object.items()}


r = {"a": 2, "b": 4, "c": "hello"}
# print("Task - 2:", new_obj(r))
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 3. Напишите программу на JS, чтобы получить максимальное и минимальное
#   значения (если это число) в словаре.


def max_min(dict) -> dict:
    return max(dict.values()), min(dict.values())


r = max_min({
    'x': 500,
    'y': 5874,
    'z': 560,
    'a': 7,
    'b': 35,
    'c': 113,
})
# print("Task - 3:", r)
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 4. Вам надо найти количество людей одного типа из массива и сохранить
#   их в массив категории. В массиве категорий специально допущены ошибки
#   (исходный массив менять нельзя)

users = [
    {
        "id": random.random(),
        "name": 'Timur',
        "info": {
            "school": '235',
            "faculity": 'SMM'
        },
    },
    {
        "id": random.random(),
        "name": 'Imran',
        "info": {
            "school": 'ne izvestno',
            "faculity": 'programming'
        },
    },
    {
        "id": random.random(),
        "name": 'Aminjon',
        "info": {
            "school": '444',
            "faculity": 'Dizayn'
        },
    },
    {
        "id": random.random(),
        "name": 'Maxmud',
        "info": {
            "school": '777',
            "faculity": '3dsmax'
        },
    },
    {
        "id": random.random(),
        "name": 'Muxammad',
        "info": {
            "school": '5555',
            "faculity": 'Backend'
        },
    },
    {
        "id": random.random(),
        "name": 'Timur',
        "info": {
            "school": '235',
            "faculity": 'SMM'
        },
    },
    {
        "id": random.random(),
        "name": 'Imran',
        "info": {
            "school": 'ne izvestno',
            "faculity": 'programming'
        },
    },
    {
        "id": random.random(),
        "name": 'Aminjon',
        "info": {
            "school": '444',
            "faculity": 'Dizayn'
        },
    },
    {
        "id": random.random(),
        "name": 'Maxmud',
        "info": {
            "school": '777',
            "faculity": '3dsmax'
        },
    },    {
        "id": random.random(),
        "name": 'Maxmud',
        "info": {
            "school": '777',
            "faculity": '3dsmax'
        },
    },
    {
        "id": random.random(),
        "name": 'Muxammad',
        "info": {
            "school": '5555',
            "faculity": 'Backend'
        },
    },
]

categories = [
    {
        "course": ' SMM',
        "count": 0
    },
    {
        "course": 'PROGRAMMING',
        "count": 0
    },
    {
        "course": '     3DSMAX',
        "count": 0
    },
    {
        "course": ' DIZAYN',
        "count": 0
    },
    {
        "course": '   BACKEND',
        "count": 0
    },
]


for user in users:
    user_course = user['info']['faculity'].lower().strip()

    for category in categories:
        category_course = category['course'].lower().strip()
        if user_course == category_course:
            category['count'] += 1
        category['course'] = category_course.title()


# print("Task - 4:")
# for item in categories:
#     print(item)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# 5. Получите всех пользователей по этой ссылке https://jsonplaceholder.typicode.com/users ...
#   и разделите их по окончаниям электронной почты (например: com, net, org и т. д.).
#   Для этого создайте функцию и передайте массив объектов (пользователей)
#   в качестве параметра.Таким образом, функция вернет объект, где каждый ключ -
#   это окончание электронной почты, а значение - количество пользователей
#   с таким окончанием электронной почты.
print("Task - 5: I cannot do it")
