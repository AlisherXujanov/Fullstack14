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
print("J:", j)
print(sorted_numbers)


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

def draw_stars_up(max_lines:int, counter:int=1):
    if counter > max_lines:
        return
    print("*" * counter)
    return draw_stars_up(max_lines, counter+1)

draw_stars_up(10)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# third = "✅3. Linear search"
...

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# fourth = "✅4. Binary search"
...

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# fifth = "✅5. Bubble sort"s
...
