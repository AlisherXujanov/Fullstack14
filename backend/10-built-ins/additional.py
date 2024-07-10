# Use map() and filter() together to convert a list of
# strings and numbers to a list of only integers and then remove all odd numbers.
# NOTE: If the item is str then get the length of the string
# if the item is int in quotes "..." then convert it to int
# RU: Используйте map() и filter() вместе, чтобы преобразовать список
# строк и чисел в список только целых чисел, а затем удалите все нечетные числа.
# ПРИМЕЧАНИЕ. Если элемент - это строка, то получите длину строки
# если элемент - это int в кавычках "...", то преобразуйте его в int


def map_and_filter(arr: list) -> list:
    ...


test_arr = [22, "wwww", "12345", "qwe", 124, '54321', 'aaaaa']
print(map_and_filter(test_arr))
# ===========================================================================
# ===========================================================================
# Write a function that takes an input from user and deletes all duplicate
# letters using filter or map somehow. Then, count each letter within the original str
# RU: Напишите функцию, которая принимает ввод от пользователя и удаляет все дублирующиеся
# буквы с помощью filter() или map() каким-то образом. Затем подсчитайте каждую букву в исходной строке


def remove_duplicates_and_count_letters():
    ...


remove_duplicates_and_count_letters()

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

# ===========================================================================
# ===========================================================================
# Write a Python program to interleave two lists into another list randomly.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# ===========================================================================
# ===========================================================================
# Write a Python program to split a given dictionary of lists into list of
# dictionaries.
