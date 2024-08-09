# 1. Write a Python function to find the maximum of three numbers.
# RU: Напишите функцию Python, чтобы найти максимум из трех чисел.

ONE_SECOND = 1
import time

def calculate_time_dec(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(ONE_SECOND)
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {round(end - start, 4)}")
        return result
    return wrapper

def print_message(fn):
    def wrapper(*args, **kwargs):
        print("This is MESSAGE")
        result = fn(*args, **kwargs)
        return result
    return wrapper


@print_message
@calculate_time_dec
def get_max(n1:int, n2:int, n3:int) -> int:
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    # return max(n1, n2, n3)

r = get_max(1, 2, 3) # 3
print(r)
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== 
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== 
# 2. Write a Python function to sum all the numbers in a list.
# RU: Напишите функцию Python, чтобы сложить все числа в списке.


@calculate_time_dec
def sum_nums(arr:list[int]) -> int:
    result = 0
    for n in arr:
        result += n
    return result


# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== 
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# 3. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String: 'The quick Brow Fox'
# Expected Output:
# Number of Upper case characters: 3
# Number of Lower case Characters : 12

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = alpha_lower.upper()


@calculate_time_dec
def count_upper_lower(sentence: str) -> str:
    uppers = 0    
    lowers = 0    
    for letter in sentence:
        if letter in alpha_lower:
            lowers += 1
        elif letter in alpha_upper:
            uppers += 1

    return f"Number of Upper case characters: {uppers}\nNumber of Lower case characters : {lowers}"


r = count_upper_lower('The quick Brow Fox')
# print(r)
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# 4. Write a Python function that takes a list and returns a new list with 
# distinct elements from the first list.
# Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]


@calculate_time_dec
def get_unique_items(arr: list[int]) -> list[int]:
    return list(set(arr))

r = get_unique_items([1, 2, 3, 3, 3, 3, 4, 5])
# print(r)
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# 5. Write a Python function to check whether a string is a pangram or not .
# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
# RU: Напишите функцию Python, чтобы проверить, является ли строка панграммой или нет.
# Примечание. Панграммы - это слова или предложения, содержащие хотя бы один раз каждую букву алфавита.

# For example: "The quick brown fox jumps over the lazy dog"


@calculate_time_dec
def pangram(text: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    
    for letter in text:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')
    
    return True if len(alphabet) == 0 else False

r = pangram("The quick brown fox jumps over the lazy dog")
# print(r)

r = pangram("Hello world")
# print(r)
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# 6. Write a  Python program that accepts a hyphen-separated sequence of 
# words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items: green-red-yellow-black-white
# Expected Result: black-green-red-white-yellow


@calculate_time_dec
def sort_alphabetically(text: str) -> str:
    splitted_text = text.split("-")
    splitted_text.sort()
    return "-".join(splitted_text)

# def sort_alphabetically(text: str) -> str: return "-".join(sorted(text.split("-")))

r = sort_alphabetically("green-red-yellow-black-white")
# print(r) # black-green-red-white-yellow
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# 7. Write a Python function to create and print a list where the values are the 
# squares of numbers between 1 and 30 (both included).


@calculate_time_dec
def get_squares_of_nums(nums: list[int]) -> list[int]:
    return [num*num for num in nums]

r = get_squares_of_nums(list(range(1, 31)))
# print(r)
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# 8. Create a range function that is almost similar to 'range' in python
# but, it will include starting and ending points as well.


@calculate_time_dec
def manual_range(start: int, stop: int, step=1) -> list[int]:
    x = 1
    print(locals())
    return [n for n in range(start, stop+1, step)]

r = manual_range(1, 100)
# print(r)
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======