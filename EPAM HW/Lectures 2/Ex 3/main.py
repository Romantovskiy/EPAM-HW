def replace_un(s: str):
    a = s.find(' reasonable')
    b = s.find('unreasonable')
    str = s[0:b] + s[b + 2:-1]
    if a > b:
        a -= 2
    return str[0:a + 1] + s[b:b + 2] + str[a + 1:-1]


if __name__ == '__main__':
    input_str = 'The reasonable man adapts himself to the world; ' \
                'the unreasonable one persists in typing to adapt the world to himself'
    print(replace_un(input_str))
