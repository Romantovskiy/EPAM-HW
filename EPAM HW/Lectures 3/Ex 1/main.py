def validate_point(x: float, y: float) -> bool:
    if (y == 1) or ((y <= 1) and (y >= 0) and (y >= abs(x))):
        return True
    return False


if __name__ == '__main__':
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))

    print('Is point in shadow area:', validate_point(x, y))