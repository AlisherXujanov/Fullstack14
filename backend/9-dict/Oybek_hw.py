def sum_numeric_values(d):
    total_sum = 0
    for value in d.values():
        # if isinstance(value, (int, float)):
        if str(value).isnumeric():
            total_sum += value
    return total_sum


sample_dict = {
    'a': 10,
    'b': 20,
    'c': 'string',
    'd': 15.5,
    'e': -5
}

total_sum = sum_numeric_values(sample_dict)
# Вывод: Сумма всех числовых значений: 40.5
print(f"Сумма всех числовых значений: {total_sum}")
# ----------------------------------------------------------------------------------------------


def reverse_case_keys(d):
    new_dict = {}
    for key, value in d.items():
        if isinstance(key, str):
            new_key = key.swapcase()
        else:
            new_key = key
        new_dict[new_key] = value
    return new_dict


sample_dict = {
    'a': 10,
    'B': 20,
    'c': 'string',
    4: 'number',
    'e': -5
}

new_dict = reverse_case_keys(sample_dict)
print(new_dict)
# Вывод: {'A': 10, 'b': 20, 'C': 'string', 4: 'number', 'E': -5}
# -------------------------------------------------------------------


def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5, 'e': 6}

merged = merge_dicts(dict1, dict2, dict3)
print(merged)
# Вывод: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
# ----------------------------------------------------------------


def count_occurrences(obj):
    occurrences = {}
    for item in obj:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences


values = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_occurrences(values)
print(result)  # Вывод: {1: 1, 2: 2, 3: 3, 4: 4}
# -----------------------------------------------------------


def invert_dict(d):
    # inverted = {}
    # for key, value in d.items():
    #     inverted[value] = key
    # return inverted
    return {value: key for key, value in d.items()}


original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)  # Вывод: {1: 'a', 2: 'b', 3: 'c'}
# -----------------------------------------------------------


def find_max_min_values(d):
    numerical_values = [
        value for value in d.values() if isinstance(value, (int, float))]

    if not numerical_values:
        return None, None

    max_value = max(numerical_values)
    min_value = min(numerical_values)

    return max_value, min_value


sample_dict = {
    'a': 10,
    'b': 20,
    'c': 'string',
    'd': 15.5,
    'e': -5
}

max_value, min_value = find_max_min_values(sample_dict)
# Вывод: Максимальное значение: 20
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")  # Вывод: Минимальное значение: -5
