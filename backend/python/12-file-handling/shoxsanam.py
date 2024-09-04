# 1. Create and write to a file with names and read the file and print
# the names and the number of times they appear in the file.
# RU: Создайте и запишите в файл имена, прочитайте файл и напечатайте
# имена и количество раз, которое они встречаются в файле.

def write_names(filename, names):
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')


def read_and_count_names(filename):
    name_count = {}
    with open(filename, 'r') as file:
        for line in file:
            name = line.strip()
            if name_count.get(name):
                name_count[name] += 1
            else:
                name_count[name] = 1
    return name_count

filename = "names.txt"
names = [
    "Oliver", "George", "Harry", "Jack", "Jacob", "Noah",
    "Charlie", "Muhammad", "Thomas", "Oscar", "William",
    "James", "Leo", "Alfie", "Henry", "Archie", "Ethan",
    "Charlie", "Muhammad", "Thomas", "Oscar", "William",
    "Joseph", "Freddie", "Samuel", "Alexander", "Logan"
]

w = write_names(filename, names)
c = read_and_count_names(filename)
print(w,c)
# ======================================================================================================================
# ======================================================================================================================
# 2. Create a file with numbers and read the file and print the sum of all numbers.
# RU: Создайте файл с числами, прочитайте файл и напечатайте сумму всех чисел.


# def read_numbers_and_sum(filename, numbers):
#     with open(filename, 'w') as file:
#         for number in numbers:
#             file.write(str(number))


import os
def create_numbers(filename):
    total_sum = 0

    if not os.path.exists(filename):
        open(filename, 'x')

    # with open(filename, 'r') as file:
    #     for line in file:
    #         number = int(line)
    #         total_sum += number
    
    return total_sum


# RE-DO this task:
# 1. Create file
# 2. Write numbers into file
# 3. Read numbers from file and sum them
# 4. Re-write the file with sum of numbers (write)


numbers = [23, "45", 12, 67, "89", 34, "56", 78, 90, 10]
filename = "numbers.txt"

sum_num = create_numbers(filename)
write_num = read_numbers_and_sum(filename, numbers)
print(sum_num, write_num)


# ======================================================================================================================
# ======================================================================================================================
