def fizz_buzz(x: int) -> None:
    try:
        x = int(x)
        print(f'{x} is out of range[1, 100]' if (x < 1) or (x > 100) else
              'Fizz' if x % 3 == 0 else '',
              'Buzz' if x % 5 == 0 else '',
              x if (x % 5 != 0) and (x % 3 != 0) else '', sep='')
    except ValueError:
        print('Need an integer')
    return


if __name__ == '__main__':
    while True:
        n = input('Enter the number:')
        fizz_buzz(n)
