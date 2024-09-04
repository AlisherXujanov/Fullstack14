# # Write a Python program to calculate the sum of a list of numbers using recursion.

def sum_with_recursion(numbers):
    first = numbers[0]
    if len(numbers) == 1:
        return first
    return first + sum_with_recursion(numbers[1:])

list1 = [1, 2, 3, 4, 5]
# print("Task - 1:", sum_with_recursion(list1))

# =======================================================================
#  Write a Python program to get the factorial of a non-negative integer using recursion.

def factorial_with_recursion(num):
    if num == 0:
        return 1
    else:
        return num * factorial_with_recursion(num - 1)


res = factorial_with_recursion(4)
# print("Task - 2:", res)

# ================================================================
# Write a Python program to solve the Fibonacci sequence using recursion.
def recursion_fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return recursion_fibonacci(number - 1) + recursion_fibonacci(number - 2)


res = recursion_fibonacci(7)  # 0, 1, 1, 2, 3, 5, 8, 13
print("Task - 3:", res)

# ====================================================================================
# 6, 7 
# 10, 11 - task i cannot do it

def remove_dublicates(num1, num2):
    ...

num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6, 7, 5, 3]
result = remove_dublicates(num1, num2)
print("Task - 1: Unique elements ->", result)
