# for item in list:
# block code

# -----------------------------
# for i in range(1, 11):
#     print("*" * i)
# -----------------------------
# for i in range(10, 0, -1):
#     print("*" * i)
# -----------------------------
# for i in range(10, 0, -1):
#     needed_spaces_num = 10 - i
#     print((" "*needed_spaces_num) + ("*" * i))
# -----------------------------
# PIRAMID
# lines = 10
#     *
#    ***
#   *****
#  *******
# *********
# -----------------------------
# for i in range(1, lines+1):
#     print(" " * (lines - i) + "* " * i)
# -----------------------------
# def create_piramid(layers:int) -> None:
#     times = layers * 2
#     for i in range(1, times+1, 2):
#         print(("*"*i).center(times))
        
# create_piramid(lines)
# -----------------------------
# for idx, item in enumerate(["apple", "banana", "cherry"]):
#     print(f"Index: {idx}, Item: {item}")
# -----------------------------
# NESTED LOOP
# import time

# start_time = time.time()
# for num in range(100):
#     for num2 in range(100):
#         print(num, num2) 

# total = round((time.time() - start_time), 2)
# print("Total time taken: ", total)
# -----------------------------

# for item in ["apple", "banana", "cherry"]:
#     for letter in item:
#         print(letter)


