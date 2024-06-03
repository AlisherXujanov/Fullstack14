# ''
# ""
# ==================================
# ==================================
# """
# This is 
# long 
# string
# """
# ==================================
# ==================================
# x = 'Hello'
# # z = f'{x} world'
# z = "{} world".format(x)
# print(z)
# ==================================
# ==================================
# x.slice(start, end)  -> in JS
# x[start:end:step]    -> in Python
# ----------------------------------
# x = "Hello World"
# z = x[2]   # Only one letter
# z = x[2:7] # From 2 to 7
# z = x[2:10:2]  # From 2 to 10 with step 2 (nth-child(2n))
# z = x[-8:-2]     # From -8 to -2
# z = x[::-1]     # Reverse
# print("Result: ", z)
# ==================================
# ==================================
# ''.replace('o', '...')  -> in JS (only one letter)
# ''.replace(/o/gi, '...')  -> in JS (all letters)

# ''.replace('...', '...')  -> 
# in python it changes all occurences
# -----------------------------------
import re  # regular expressions
# x = "Hello World OO oo OO"
# print(x.replace('o', '...'))

# <input pattern="^[a-zA-Z0-9]{3,}$" characters at least">

# re.sub(what, to-what, where, count=all, flags=rules)
# string = """I love an apple but sometimes 
#             I eat an ORANGE and Banana"""
# # only change vowels
# print("------------------------------")
# res1 = re.sub(r'[aieou]', "*", string)
# print("Result 1: ", res1)
# print("------------------------------")
# fruits = ['apple', 'orange', 'banana']  # after join => 'apple|orange|banana'
# res2 = re.sub('|'.join(fruits), "***", string, flags=re.IGNORECASE)
# print("Result 2: ", res2)
# print("------------------------------")
# res3 = re.sub('|'.join(fruits), "***", string, flags=re.IGNORECASE, count=2)
# print("Result 3: ", res3)
# print("------------------------------")
# ==================================
# ==================================
# "  ...   ".trim()  -> in JS
# "  ...   ".strip()  -> in Python
# text = "    hello world    "
# print(text)
# print(text.strip())
# ==================================
# ==================================
# in JS
# "hello".padStart(10, '.')   =>  ".....hello"
# "hello".padEnd(10, '.')     =>  "hello....."

# in Python
# "hello".rjust(10, '.')   =>  ".....hello"
# "hello".ljust(10, '.')   =>  "hello....."
# "hello".center(10, '.')  =>  "..hello..."
# ==================================
# ==================================
# in JS
# indexOf()      ->  'hello'.indexOf('l')      => 2
# lastIndexOf()  ->  'hello'.lastIndexOf('l')  => 3

# in Python
# find()      ->  'hello'.find('l')      => 2
# index()     ->  'hello'.index('l')     => 2

# rfind()     ->  'hello'.rfind('l')     => 3
# rindex()    ->  'hello'.rindex('l')    => 3

# The difference between both methods is that one gives -1 and the
# other one gives an ERROR if the letter is not found
# RU: Разница между обоими методами в том, что один дает -1, 
# а другой вызывает ОШИБКУ, если буква не найдена

# print('hello'.find('l'))  # 2
# print('hello'.find('z'))  # -1

# print('hello'.index('l')) # 2
# print('hello'.index('w')) # ValueError: substring not found
# ==================================
# ==================================
# CASES

# in JS
# "...".toLowerCase()    =>  abc
# "...".toUpperCase()    =>  ABC

# in Python
# "...".lower()     =>  abc
# "...".upper()     =>  ABC
# "ABC".swapcase()  =>  abc
# "abc".swapcase()  =>  ABC
# "AbCd".swapcase() => aBcD
# ----------------------------------
# "hello world".title()       =>  Hello World
# "hello world".capitalize()  =>  Hello world
# "...".casefold()  =>  abc  (a little more aggressive || stronger)
# ==================================
# ==================================
# SPLIT 

# in JS
# "hello world".split(' ')  =>  ["hello", "world"]
# "hello world".split('')   =>  ["h", "e", "l", "l", ...]
# "hello world".split()     =>  Error


# in Python
# "hello world".split(' ')  =>  ["hello", "world"]
# "hello world".split()     =>  ["hello", "world"]
# "hello world".split('')   =>  Error   =>  replace it with:
# list("hello world")       =>  ["h", "e", "l", "l", ...]
# --------------------
# r = "This is test text".rsplit(" ")  # => ["This", "is", "test", "text"]
# r2 = "This is test text".rsplit(" ", 1)  # => ["This is test", "text"]
# print("Result: ", r)
# print("Result 2: ", r2)
# --------------------
# \n   =>  new line   ==   <br>
# text = "Hello \nworld"
# print(text.splitlines())
# ==================================
# ==================================
# text = "Hello"
# print(text.zfill(10))   =>  only 0

# print("6:00:00".zfill(8))  # 06:00:00
# print("12:00:00".zfill(8))  # 12:00:00




