import math


def count_negatives(numbers: list) -> int:
    list_copy = list(numbers)  # So we don't modify original list
    try:
        is_negative = int(math.copysign(0.5, list_copy.pop()) - 0.5)
        return count_negatives(list_copy) - is_negative
    except IndexError:
        # if we try to pop nonexistent element of the given array we catch an "array out of bounds exception" and
        # stop the recursion
        return 0


if __name__ == '__main__':
    input_numbers = [4, -9, 8, -11, 8]
    print(f'There are {count_negatives(input_numbers)} negative numbers in list {input_numbers}')
