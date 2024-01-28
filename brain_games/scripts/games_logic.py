import prompt
import math


GAMES_COUNT = 3


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_correct(name, question, correct_answer):
    print(f'Question: {question}')
    answer = prompt.integer('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '",
              f"{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def is_correct_string(name, question, correct_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was'",
              f"{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def gcd(number1, number2):
    while number1 != number2:
        result = abs(number1 - number2)
        if number1 > number2:
            number1 = result
        else:
            number2 = result
    return result


def is_prime(number):
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'
