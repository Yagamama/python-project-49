import prompt


GAMES_COUNT = 3


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def gcd(number1, number2):
    while number1 != number2:
        result = abs(number1 - number2)
        if number1 > number2:
            number1 = result
        else:
            number2 = result
    return result