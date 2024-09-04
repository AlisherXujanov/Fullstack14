# Errors in python

# 1. Compile time
#    ex: Syntax error
# -------------------------------
# 2. Logical
#    ex: 2 + 2 == 5 ?
# print("2 + 2")  # 2 + 2
# x = 2**3/2 # ....
# print(x + 2 == 4) # False
# -------------------------------
# 3. Run time
# num = 10
# answer = int(input("Enter a number please: "))
# print(num / answer)
# =========================================================================
# =========================================================================
# ERROR TYPES
# 1. SyntaxError  =>  '...  => not closed string
#     RU: не закрытая строка
# ex: print('Hello world)
# --------------------------
# 2. TypeError    =>  1 + '...'  =>  unsupported operand type(s) for +: 'int' and 'str'
#     RU: неподдерживаемый тип операнда (ы) для +: 'int' и 'str'
#     ex: print(1 + 'Hello world')

# int + str  ==  Error
# int + int  ==  number
# str + str  ==  text
# 1st-type + different-type  == Error

# print("Hello" * 2)   ->  works fine
# --------------------------
# 3. NameError    =>  x  =>  name 'x' is not defined
#     RU: имя 'x' не определено
#     ex: print(x)
# x = 10
# print(y)
# --------------------------
# 4. IndexError   =>  [1, 2, 3][3]  =>  list index out of range
#     RU: индекс списка вне диапазона
#     ex: print([1, 2, 3][3])

# x = "Hello"
# print(x[1])  # e
# print(x[10]) # Error
# --------------------------
# 5. ValueError   =>  int('...')  =>  invalid literal for int() with base 10: '...'
#     RU: недопустимый литерал для int() с основанием 10: '...'
#     ex: print(int('Hello world'))

# int()
# str()
# float()
# list()
# ...()
# int("Hello")
# float("Hello")

# "", 0, [], {}, False, None   =>  Falsy values
# --------------------------
# 6. KeyError     =>  {'a': 1}['b']  =>  'b' =>  not in dictionary
#     OBJECT in JS     ===     DICTIONARY in Python
#     RU: 'b' => не в словаре
#     ex: print({'a': 1}['b'])
# --------------------------
# 7. AttributeError  =>  'Hello'.append('!')  =>  'str' object has no attribute 'append'
#     RU: объект 'str' не имеет атрибута 'append'
#     ex: print('Hello'.append('!'))

# [].push() ==  "".append()
# "".bool()
# 123.str()
# --------------------------
# 8. ZeroDivisionError  =>  1 / 0  =>  division by zero
#     RU: деление на ноль
#     ex: print(1 / 0)
# --------------------------
# 9. ImportError  =>  import test  =>  No module named 'test'
#     RU: нет модуля с именем 'test'
# import math
# import lorem
# --------------------------
# 10. IndentationError  =>  def func():  =>  expected an indented block
#     RU: ожидался отступный блок
#     - Forgetting to indent the code inside a function, while, for, or if statement.
#     RU: Забывая отступить код внутри функции, while, for или if оператора.
# def test():
# ...
# -----------------
# print("Start ...")
# print("------------------------------------------------")
# try: 
#     # ...
#     client_input = 0 # input(...)
#     print(2 / client_input.append("!"))  # Error
#     # ...
# except ZeroDivisionError as err:
#     print("Please, do not use 0 (zero)")
# except NameError as err:
#     print("You didn't create a var: ", err)
# print("Continue ...")

# =========================================================================
# In JavaScript
# try {}  catch {}  =>  попробуй, если получится, а если нет то перехвати ошибку

# In Python
# try: ...   except: ...  => попробуй, если получится, а если нет то пропускай ошибку

# x = 2
# z = "123"

# print("BEFORE ...")
# try:
#     print(x/z)
# except ZeroDivisionError as error:
#     print("Нельзя делить на ноль! - ", error)
# except Exception as error:
#     print("Вообще не понял - ", error)

# print("AFTER ...")
# -----------------------------------------------
# Block - FINALLY
# Works in any case  ->  сработает в любом случае

# try:
#     print("open file")
#     print(2/0)
# except Exception as e:
#     print(e)
# finally:
#     print("close file")

# -----------------
# IF WE WANT TO USE MULTIPLE EXCEPTIONS

# print("Start ...")
# try:
#     print(x)
# except (NameError, TypeError) as error:
#     print(error)
# print("End ...")
# ============================================================================
# =============================================================================
# usage of KEYWORD  ==>>  raise

# throw new Error(...)   ->  in JS
# raise Error-name(...)  ->  in Python

# def my_fn(x:int) -> int:
#     # if not isinstance(x, int):
#     # if not x.isnumeric():
#     if type(x) != int:
#         raise TypeError('Bemiyya!!!  Nomer yoz!!!')
#     return x*x  # ==  x**2

# print(my_fn("10"))
# -----------------------------------------------
# Ternary operator in Python

# 2==2 ? True : False  => In JavaScript
# True if 'условие' else False
# print("Правда" if 2==3 else "Ложь")

# -------------------------------------
# "Yes" if 2==2 else "No"
# if 2==2:
#     print('Yes')
# else:
#     print('No')
# =========================================================================
# =========================================================================

# Generators
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# ---------------------
# If the loop is too big then it takes all memory and slows down our computers
# 10GB
# ... 1000000 lines
# ---------------------
# The Solution is to use GENERATORS
# ---------------------


# Create a generator for the first 10 Fibonacci numbers
# int(), str(), ...
# fib = fibonacci(10)
# print(int(fib.__next__()))
# print(int(fib.__next__()))
# print(int(fib.__next__()))
# for i in fib:
#     print(i)
    
# up_to_number = 10000
# a = 0
# b = 1
# for i in range(up_to_number):
#     print(f"{i}. ---> ", a)
#     first = a
#     second = b
#     a = second
#     b = first + second
    
# a=0,  b=1
# a=1,  b=1
# a=1,  b=2
# a=2,  b=3
# a=3,  b=5

# Print the Fibonacci numbers
# for num in fib:
#     print(num)

# In this example, the fibonacci function is a generator that yields
# the first n Fibonacci numbers. We create a generator fib for the first
# 10 Fibonacci numbers, and then we use a for loop to print each number.
# This is more memory-efficient than creating a list of the first n
# Fibonacci numbers, especially for large n.
# RU: Это более эффективно с точки зрения использования памяти, 
# чем создание списка первых n чисел Фибоначчи, особенно для больших n.
# =========================================================================

