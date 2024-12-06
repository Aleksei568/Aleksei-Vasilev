def sum_numbers_and_count_strings(data):
    total_sum = 0
    total_length = 0

    for item in data:
        if isinstance(item, (int, float)):  
            total_sum += item
        elif isinstance(item, str):
            total_length += len(item)
        elif isinstance(item, (list, tuple, set)): 
            sub_sum, sub_length = sum_numbers_and_count_strings(item)
            total_sum += sub_sum
            total_length += sub_length
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, (int, float, str)): 
                    if isinstance(key, str):
                        total_length += len(key)
                    else:
                        total_sum += key
                if isinstance(value, (int, float, str)): 
                    if isinstance(value, str):
                        total_length += len(value)
                    else:
                        total_sum += value
                elif isinstance(value, (list, tuple, set, dict)): 
                    sub_sum, sub_length = sum_numbers_and_count_strings(value)
                    total_sum += sub_sum
                    total_length += sub_length

    return total_sum, total_length

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum, total_length = sum_numbers_and_count_strings(data_structure)
print(f"Сумма всех чисел: {total_sum}, Длина всех строк: {total_length}")
