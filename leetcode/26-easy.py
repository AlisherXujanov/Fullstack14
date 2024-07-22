# DELETE DUPLICATES with algorithm TWO POINTERs from sorted list
sorted_numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

j = 0
for i in range(1, len(sorted_numbers)):
    if sorted_numbers[i] != sorted_numbers[j]:
        j += 1
        sorted_numbers[j] = sorted_numbers[i]

# j=0, i=1 == 0, 0  =>   [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# j=1, i=2 == 0, 1  =>   [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
# j=1, i=3 == 1, 1  =>   [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
# j=1, i=4 == 1, 1  =>   [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
# j=2, i=5 == 1, 2  =>   [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
# j=2, i=6 == 2, 2  =>   [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
# j=3, i=7 == 2, 3  =>   [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
# ...

sorted_numbers[:] = sorted_numbers[:j+1] + ["_"]*len(sorted_numbers[j+1:])
print("J:", j)
print(sorted_numbers)
