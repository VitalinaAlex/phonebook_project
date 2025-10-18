from functools import partial

def multiply_two_numbers(a, b):
    print(a, b)
    return (a * b)

print(multiply_two_numbers(7,10))

multiply_numbers_by_two = partial(multiply_two_numbers,2)

print(multiply_numbers_by_two(9))




