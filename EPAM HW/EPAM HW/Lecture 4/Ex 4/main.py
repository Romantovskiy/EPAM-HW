def binary(n: int) -> str:
    return str(n) if n <= 1 else binary(n // 2) + str(n % 2)


def binary_sum(n: int) -> int:
    return n if n <= 1 else n % 2 + binary_sum(n // 2)


if __name__ == '__main__':
    n = 128
    print(f'Number is {n}, binary representation is {binary(n)}, sum is {binary_sum(n)}')
