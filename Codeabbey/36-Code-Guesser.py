from itertools import product

DIGITS = 3


def bulls(secret, guess):
    return sum(s == g for s, g in zip(secret, guess))


def solution():
    guesses = [input().split() for _ in range(int(input()))]

    possibilities = [[True for _ in range(10)] for _ in range(DIGITS)]

    for guess, answer in guesses:
        for place, g in enumerate(guess):
            if answer == '0':
                possibilities[place][int(g)] = False

    possible_digits = [[index for index, is_possible in enumerate(possibility) if is_possible]
                       for possibility in possibilities]

    possible_numbers = [''.join(map(str, element)) for element in product(*possible_digits)]

    result = [
        number
        for number in possible_numbers
        if all(
            bulls(number, guess) == int(answer) for guess, answer in guesses
        )
    ]

    print(result[0])


if __name__ == '__main__':
    solution()