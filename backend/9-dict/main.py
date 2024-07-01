# DICTIONARIES
# Словари - это структуры данных, которые хранят данные в виде пар ключ-значение.
# ----------------------------
# {"key": value}  &&  {number: value}
# ----------------------------
# 1-a,  2-b,  3-c,  4-d
# z = ['a', 'b', 'c', 'd']
# {"zero": "a", 1: "b", 2: "c", 3: "d"} ...
# ----------------------------
# x = {0: "a", "second": "b", "third": "c", 4: "d"}
# print(x[0])
# print(x.get(1, 'Not found'))
# ----------------------------

# x = {
#     "first": "Один",    "second": "Два",
#     "third": "Три",     "fourth": "Четыре",
#     "fifth": "Пять",    "sixth": "Шесть",
#     "seventh": "Семь",  "eighth": "Восемь",
# }
# print(x.get("fourth", "Не нашлось"))
# print(x["fourth"]) # => Четыре

# print(x["www"]) # => # KeyError if not found
# ['a', 'b', 'c', 'd'][4]  # => IndexError
# ------------------------------------------------
# z = ["Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь"]
# for i in z:
#     if i == "Четыре":
#         print(i)

# NOTE:
# If there are 1000 doors, when using list and seeking some of them,
# the loop we are using, opens every door one by one to check them
# But, if we use dictionary here, it directly opens the needed one.
# RU: Если есть 1000 дверей, когда мы используем <list> и ищем
# некоторые из них, цикл, который мы используем, открывает каждую дверь
# по одной, чтобы проверить их. Но, если мы используем здесь <dict>,
# он сразу же открывает нужную.
# ------------------------------------------------
# IN JAVA-SCRIPT
# function Person(name, ..., ...) {
#     this.name = name
#     this.surname = ...
#     this.age = ...
#     ...
# }
# let person1 = new Person(..., ..., ...)
# {name: ...,  surname: ...,  age: ...}
# ------------------------------------------------
# IN PYTHON
# dict()  =>  dict(key=value, key=value, key=value)
# person = dict(name='Kamron', bemiyya=True)
# print(person)
# list()  => []
# str()   => ''
# int()   => 0
# float() => 0.0
# bool()  => False
# set()   => set()
# dict()  => {}



# # ACCESSING ITEMS ---------------------------------------------------------------------------
# dict[key]         => берёт значение по ключу
# dict.get(key)     => берёт значение по ключу
# dict.get(key, default)  => берёт значение по ключу, если его нет, то возвращает default

# Object.keys(dict) => возвращает список ключей (JS)
# dict.keys()       => возвращает список ключей

# x = {
#     "first": "Один",    "second": "Два",
#     "third": "Три",     "fourth": "Четыре",
#     "fifth": "Пять",    "sixth": "Шесть",
#     "seventh": "Семь",  "eighth": "Восемь",
# }

# Object.values(dict) => возвращает список ключей (JS)
# dict.values()     => возвращает список значений

# Object.entries(dict) => возвращает список ключей (JS)
# dict.items()      => возвращает список кортежей (ключ, значение)

# person1 = dict(name='Javox', bemiyya='True')
# print(person1.items())


# # ADDING ITEMS -----------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# print(person1.items())
# person1['bemiyya'] = True
# person1['...'] = "..."
# person1[1] = 1
# print(person1.items())
# -----------------
# Update => updates the dict (changes the original)
# dict.update({key:value, key:value, key:value})

# person1 = dict(name='Mirsaid', address="Tashkent")
# person1['other'] = "Alex"
# print(person1)

# person1.update({
#     "name": "Alex",
#     "address": "Samarkand",
#     "bemiyya":True
# })
# print(person1)
# -----------------
# If the key is not found, a new key:value pair is added to the dictionary.
# RU: Если ключ не найден, в словарь добавляется новая пара ключ: значение.

# But if it exists, then the value of the key is NOT updated.
# RU: Но если он существует, то значение ключа НЕ обновляется.


# dict.setdefault(key, value)
# person1 = dict(name='Mirsaid', address="Tashkent")
# person1.setdefault("address", "Buxoro")
# print(person1)


# # REMOVING ITEMS ---------------------------------------------------------------------------
person1 = dict(name='Mirsaid', address="Tashkent")

# dict.pop(key)
# del_val = person1.pop('name')
# print("del_val: ", del_val)
# print("original object: ->  person1 = ", person1)

# dict.pop(key, default)
# res = person1.pop('www', "Not found")
# print("Result: ", res)
# print(person1)

# dict.popitem() => removes the last inserted item
# res = person1.popitem()
# print("Result: ", res)
# print("Remaining: ", person1)

# del dict[key]
# del person1['address']
# del person1 # deletes the whole dict
# print("Remaining: ", person1)

# # MERGE ------------------------------------------------------------------------------------
person1 = dict(name='Mirsaid', has_pet=False)
person2 = dict(name="Covid",   contageous=True)
person3 = dict(name="John",    widespread=True)
# -----------------------------------------------
# print("Before: ", person1)
# person1 |= person2 
# print("After: ", person1)
# -----------------------------------------------
# person1 |= person2 | person3
# print("After: ", person1)
# -----------------------------------------------
# print("Original: ", person1)
# # {**{...}, **{...}, **{...}}   ->  удаляются фигурные скобки изза звёздочек 
# result = {**person1, **person2, **person3}
# print("New: ", result)
# -----------------------------------------------
# DEFINITIONS all together

# dict1.update(dict2)               ->  updates original dict1 adding dict2 into it
#                       RU: обновляет оригинальный dict1, добавляя dict2 в него

# dict1 |= dict2        
# dict1 |= dict2 | dict3 | dict4    ->  they are getting merged into first (dict1) dict
#                       RU: они объединяются в первом (dict1) словаре

# {**dict1, **dict2, **dict3, **dict4}  -> they are getting merged into one dict
#                       RU: они объединяются в одном словаре
# a = {**person, **person2, **person3 }
# works like spread operator in JS  -> RU: работает как оператор spread в JS
# -----------------------------------


# # OTHER METHODS ----------------------------------------------------------------------------
# ----------------------------- 
# dict.clear()
# x = {"a": 1, "b": 2, "c": 3}
# x.clear()
# print(x)
# -----------------------------
# dict.copy()  ->  copies the object into different variable with new identity
#              RU: копирует объект в другую переменную с новым идентификатором
# x = {"a": 1, "b": 2, "c": 3}
# z = x.copy()
# z.update({"d": 4})
# print(id(x))
# print(id(z))
# =============================
# for key, val in person.items():
#     person[key] = ""

person = {
    "name": "John",
    "age": 20,
    "surname": "Khan",
    "address": "Samarkand"
}
for key, val in person.items():
    print("KEY: ", key)
    print("VAL: ", val)
