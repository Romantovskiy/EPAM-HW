def factorial(a: int) -> int:
    return 1 if a == 1 else a*factorial(a-1)


if __name__ == '__main__':
    a = int(input('Please, enter the number:'))
    print(f'Factorial of {a} is {factorial(a)}')
