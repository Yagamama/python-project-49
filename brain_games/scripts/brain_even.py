#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    even(name)


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(1,100)
        if number % 2 == 0:
            correct_answer = 'yes' 
            wrong_answer = 'no'
        else:
            correct_answer = 'no' 
            wrong_answer = 'yes'
            
        print(f'Question: {number} ')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
