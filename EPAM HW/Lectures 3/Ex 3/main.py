a = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def b(f_c: str, s_c: str) -> str:
    try:
        f_n = (a.index(f_c) + 2) % 13
        s_n = (a.index(s_c) + 2) % 13
        if (f_n < 1) or (f_n > 9):
            f_n = 0
        if (s_n < 1) or (s_n > 9):
            s_n = 0
        return str((f_n + s_n) % 10)
    except ValueError:
        return 'Do note cheat'


if __name__ == '__main__':
    f_c = input('F c:')
    s_c = input('S c:')
    print('...', b(f_c, s_c))
