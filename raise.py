def raise_both(value1, value2):
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)

    return new_tuple

result = raise_both(5, 7)

print(result)