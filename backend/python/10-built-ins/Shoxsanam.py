# 1. Write a Python program to triple all numbers in a given list of integers.
# Use Python map.
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def triple(num:int):
#     return num * 3

# z = list(map(triple, x))
# print(z)
# ------------------------------------------------------------------------------
# 2. Write a Python program to add three given lists using Python map and lambda.
import math
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [8, 9, 10]

lists = map(lambda x, y, z: x + y + z, list1, list2, list3)
# print("Task - 2:", list(lists))
# ------------------------------------------------------------------------------

# 3. Write a Python program to listify the list of given strings individually
# using Python map.

text = 'Hello World!'


def listed(string: str):
    return list(string)


z = list(map(listed, text))
# print("Task -3:", z)
# ------------------------------------------------------------------------------

# 4. Write a Python program to create a list containing the power of said
# number in bases raised to the corresponding number in the index using Python map.

nums = [10, 20, 30, 40, 50]
index = [1,  2,  3,  4,  5]


def power(num, index):
    return num**index


# powered = list(map(power, nums, index))
# print(powered)
# ------------------------------------------------------------------------------

# 5. Write a Python program to square the elements of a list using the map() function.
x = [2, 4, 6, 8]


def square_num(num: int):
    return num * num


r = list(map(square_num, x))
# print("Task - 5: ", r)
# ------------------------------------------------------------------------------

# 6. Write a Python program to convert all the characters into uppercase and
# lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
words = ["h", "W", "e", "L", "l"]


def changed_version(letter: str):
    return letter.upper(), letter.lower()


changed = set(map(changed_version, words))
# print("Task - 6:", changed)
# ------------------------------------------------------------------------------

# 7. Write a Python program to add two given lists and find the difference
# between them. Use the map() function.
#
list1 = ["hello", 1, 10, False, "WORLD", "!"]
list2 = [2, 20, True, "hello", "World", "?", 10, 0]


r = list(map(lambda item: item if item not in list2 else None, list1))
x = [item for item in r if item is not None]
# print("Task - 7:", x)
# --------------------------------------------------------------------
r2 = list(map(lambda item: item if item not in list1 else None, list2))
x = [item for item in r2 if item is not None]
# print("Task - 7:", x)
# ------------------------------------------------------------------------------

# 8. Write a Python program to convert a given list of integers and a tuple of
# integers into a list of strings.

lists = [1, 2, 3, 4, 5]
tuples = (6, 7, 8, 9, 10)


l_strs = list(map(str, lists))
t_strs = list(map(str, tuples))
total = [*l_strs, *t_strs]
# print("Task - 8:", total)
# ------------------------------------------------------------------------------

# 9. Write a Python program to create a new list taking specific elements
# from a tuple and convert a string value to an integer

tuple_nums_as_str = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
r = list(map(int, tuple_nums_as_str))

# print("Task -9:", r)
# ------------------------------------------------------------------------------
# 10. Write a Python program to compute the square of the first N Fibonacci
# numbers, using the map function and generate a list of the numbers.

# math.sqrt() =>   16  ->  4
# math.pow()  =>   n**2


def create_n_fibbo_nums(n: int) -> list:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
    result = [0, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result


fibbos = create_n_fibbo_nums(10)
r = list(map(math.sqrt, fibbos))
# print("Task - 10:", r)
# ------------------------------------------------------------------------------

# 11. Write a Python program to compute the sum of elements of an array
# of integers.


x = [1, 2, 3, 4, 5]
r = sum(x)

# print("Task - 11:", r)
# ------------------------------------------------------------------------------

# 12. Write a Python program to find the ratio of positive numbers, negative
# numbers and zeroes in an array of integers.




def make_ratio_of_numbers(nums:list[int]) -> str:
    zeros = [zero for zero in nums if zero == 0]
    positives = [num for num in nums if num > 0]
    negatives = [num for num in nums if num < 0]
    result = [str(len(positives)), str(len(negatives)), str(len(zeros))]

    return ":".join(result)

x = [2, 5, 10, -5, 0, -12, 10, 100, 1000]
r = make_ratio_of_numbers(x)
# print(r)
# OUTPUT: 6:2:1
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Write a Python program to interleave two lists into another list randomly.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# ------------------------------------------------------------------------------
# Write a Python program to split a given dictionary of lists into list of
# dictionaries.
# ------------------------------------------------------------------------------

