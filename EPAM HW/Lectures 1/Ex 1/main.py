import math


def geron(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    a = float(input('a:'))
    b = float(input('b:'))
    c = float(input('c:'))
    print(f'The area of a triangle with sides {a}, {b}, {c} is', geron(a, b, c))
