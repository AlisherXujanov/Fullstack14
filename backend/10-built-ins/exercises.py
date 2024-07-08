list1 = [1, 2, 3]                                         # 1
list2 = [4, 5, 6, 7, 8, 9]                                # 3
list3 = [10, 11, 12, 13, 14, 15, 16, 13, 15, 17, 21, 23]  # 4
list4 = [17, 18]                                          # 1
list5 = [17, 18, 20, 22, 24, 26, 28, 30]                  # 7

all_lists = [list1, list2, list3, list4, list5]

def get_max_evens(numbers: list[int]) -> int:
    return len([num for num in numbers if num % 2 == 0])

# print(max(all_lists, key=get_max_evens))
# ====================================================================
# ====================================================================
words = ['apple', 'bananaaa', 'cherry', 'elderberry', 'date']

def func(word):
    return "".join([letter.upper() for letter in word if letter.lower() in 'aeiou'])

x = list(map(func, words))
# print(x)
# ====================================================================
# # ====================================================================
words = ['apple', 'bananaaa', 'cherry', 'elderberry', 'date', 'bbbb', 'cccc']
def get_more_vowels_then_one(word) -> bool:
    vowels = len([letter for letter in word if letter.lower() in 'aeiou'])
    if vowels > 1:
        return True
    else:
        return False

r = list(filter(get_more_vowels_then_one, words))
# print(r)
# ====================================================================
# ====================================================================
from functools import reduce
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def func(acc, item):  return acc

def sum_up(acc, next):
    return acc + next

# 1==acc, 2==next      =>  3
# 3==acc, 3==next      =>  6
# 6==acc, 4==next      =>  10
# 10==acc, 5==next     =>  15
# ...
# ...==acc, 9==next    =>  45

r = reduce(sum_up, nums)
# print(r)

# ====================================================================
# ====================================================================
# Напишите программу, которая принимает список
# строк в качестве входных данных и возвращает
# новый список со всеми строками длиной 4 или больше.
words = ['apple', 'bananaaa', 'cherry', 'elderberry', 'date', 'bbbb', 'cccc']

def more_than_five(word:str) -> bool:
    return True if len(word) > 5 else False

r = list(filter(more_than_five, words))
# print(r)

