# Use map() and filter() together to convert a list of
# strings and numbers to a list of only integers and then remove all odd numbers.
# NOTE: If the item is str then get the length of the string
# if the item is int in quotes "..." then convert it to int
# RU: Используйте map() и filter() вместе, чтобы преобразовать список
# строк и чисел в список только целых чисел, а затем удалите все нечетные числа.
# ПРИМЕЧАНИЕ. Если элемент - это строка, то получите длину строки
# если элемент - это int в кавычках "...", то преобразуйте его в int
import random
from functools import reduce
data = ['123', 'hello', 456, '789', 'world', '42']


def process_item(item):
    if isinstance(item, str):
        if item.isdigit():
            return int(item)
        else:
            return len(item)
    return item


# processed_data = list(map(process_item, data))
# result = list(filter(lambda x: x % 2 == 0, processed_data))
# print(result)


# ===========================================================================
# ===========================================================================
# Write a function that takes an input from user and deletes all duplicate
# letters using filter or map somehow. Then, count each letter within the original str
# RU: Напишите функцию, которая принимает ввод от пользователя и удаляет все дублирующиеся
# буквы с помощью filter() или map() каким-то образом. Затем подсчитайте каждую букву в исходной строке

def remove_duplicates_and_count(input_str):

    seen = set()
    filtered_str = ''.join(
        filter(lambda x: not (x in seen or seen.add(x)), input_str))

    letter_counts = {}
    for char in input_str:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    return filtered_str, letter_counts


# user_input = input("Enter a string: ")
# filtered_str, letter_counts = remove_duplicates_and_count(user_input)

# print(f"String with duplicates removed: {filtered_str}")
# print("Letter counts in the original string:")
# for letter, count in letter_counts.items():
#     print(f"{letter}: {count}")


# ===========================================================================
# ===========================================================================
# Create a function that can take a list of positive or negative numbers
# and get the difference between smallest positive and largest negative numbers
# Do this with the help of filter or map or reduce.
# Then find nearest number to this difference
# EX:
#   l = [1, -2, 10, 4, 5, -6, 7, 8, 9]
#   distance = 3
#   result = 3nd index that is 4


def find_difference_and_nearest(nums:list[int]) -> int:
    negatives = sorted([num for num in nums if num < 0])
    positives = sorted([num for num in nums if num >= 0])

    min_positive = positives[0]
    max_negative = negatives[-1]
    difference = min_positive - max_negative

    counter = 0
    while True:
        if difference + counter in nums:
            return difference, difference + counter
        elif difference - counter in nums:
            return difference, difference - counter
        else:
            counter += 1

# Example usage
nums = [1, -2, 10, 4, 5, -6, 7, 8, 9]
difference, nearest_value = find_difference_and_nearest(nums)

# print(f"Difference: {difference}")
# print(f"Value {nearest_value}")

# ===========================================================================
# ===========================================================================
# Write a Python program to interleave two lists into another list randomly.


def interleave_randomly(list1, list2):
    combined_list = list1 + list2
    random.shuffle(combined_list)
    return combined_list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = interleave_randomly(list1, list2)
# print(result)

# ===========================================================================
# ===========================================================================
# Write a Python program to split a given dictionary of lists into list of
# dictionaries.


def split_dict_of_lists(dict_of_lists):
    keys = dict_of_lists.keys()
    values = zip(*dict_of_lists.values())
    list_of_dicts = [dict(zip(keys, value)) for value in values]
    return list_of_dicts


dict_of_lists = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
}

result = split_dict_of_lists(dict_of_lists)
# print("Original dictionary:", dict_of_lists)
# print("List of dictionaries:", result)


# l1 = [ 1,   2,   3 ]
# l2 = ['a', 'b', 'c']
# z = zip(l1, l2)
# print([list(i) for i in list(z)])










