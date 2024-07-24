# ✅1. Nested loops
# ✅2. Recursion
# ✅3. Linear search
# ✅4. Binary search
# ✅5. Bubble sort
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
first = "✅1. Nested loops"

# for n in range(1000):       # 1000 => times         # O(n)
#     for n2 in range(1000):  # 1000*1000 => times    # O(n^2)
#         # MEMORY Inefficient
#         # TIME Inefficient
#         print("Hello world")

# ----------------------------------------------------------
# ----------------------------------------------------------
# j = 0
# for i in range(100):
#     # TWO POINTERs algorithm
#     ...
# ------------------
# EXAMPLE:
# DELETE DUPLICATES with algorithm TWO POINTERs from sorted list
sorted_numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

j = 0
for i in range(1, len(sorted_numbers)):
    if sorted_numbers[i] != sorted_numbers[j]:
        j += 1
        sorted_numbers[j] = sorted_numbers[i]

sorted_numbers[:] = sorted_numbers[:j+1] + ["_"]*len(sorted_numbers[j+1:])
# print("J:", j)
# print(sorted_numbers)


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# second = "✅2. Recursion"
# IMPORTANT RULES:
#       1. CHECK the condition to prevent the infinite loop
#          - Проверка условия для предотвращения бесконечного цикла
#       2. In order to call the function as RECURSION, it should be called within itself
#          - Чтобы называть функцию как "РЕКУРСИЯ", ее нужно вызвать внутри себя самого
#       3. It should always pass different arguments to itself when calling itself again
#          - Всегда нужно передавать разные аргументы самому себе при повторном вызове

# EXAMPLE:
# *
# **
# ***
# ****
# *****

def draw_stars_up(max_lines: int, counter: int = 1):
    if counter > max_lines:
        return
    print("*" * counter)
    return draw_stars_up(max_lines, counter+1)


# draw_stars_up(10)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# third = "✅3. Linear search"
def linear_search(nums:list[int], target:int) -> bool:
    for n in nums:
        if n == target:
            return True
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
r = linear_search(numbers, target)
# print("Result: ", r)


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# fourth = "✅4. Binary search"
def binary_search(nums:list[int], target:int) -> bool:
    start = 0               # 0
    end = len(nums) - 1     # 9
    while start <= end:
        MIDDLE = (start+end)//2
        if nums[MIDDLE] == target:
            return True
        else:
            if nums[MIDDLE] < target:
                start = MIDDLE + 1
            else:
                end = MIDDLE - 1
    return False

# MIDDLE==4,           nums[MIDDLE]==5,   target==9
# (5+9)//2==MIDDLE     nums[MIDDLE]==8,   target==9
# (7+9)//2==MIDDLE     nums[MIDDLE]==9,   target==9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
r = binary_search(numbers, target)
# print("Result: ", r)
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# fifth = "✅5. Bubble sort"s
# Memory Efficient
# Time Inefficient
def bubble_sort(u_nums:list[int]) -> list:
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(u_nums)-1):
            left = u_nums[i]
            right = u_nums[i+1]
            if left > right:
                u_nums[i], u_nums[i+1] = right, left
                sorted = False
    return u_nums

# [5, 3, 8, 6, 7, 2]   =>  original unsorted list
# [3, 5, 8, 6, 7, 2]
# [3, 5, 6, 8, 7, 2]
# [3, 5, 6, 7, 8, 2]
# [3, 5, 6, 7, 2, 8]

unsorted_list = [5, 3, 8, 6, 7, 2]
r = bubble_sort(unsorted_list)
print("Result: ", r)
