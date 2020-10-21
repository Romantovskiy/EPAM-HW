CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def play(first_card: str, second_card: str) -> str:
    try:
        first_number = (CARDS.index(first_card) + 2) % 13
        second_number = (CARDS.index(second_card) + 2) % 13
        if (first_number < 1) or (first_number > 9):
            first_number = 0
        if (second_number < 1) or (second_number > 9):
            second_number = 0
        return str((first_number + second_number) % 10)
    except ValueError:
        return 'Do not cheat!'


if __name__ == '__main__':
    first_card = str(input('Play first card:'))
    second_card = str(input('Play second card:'))
    print('Your result:', play(first_card, second_card))
