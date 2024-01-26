import prompt
import random
import games_logic


def main():
    name = games_logic.hello()
    calculate(name)


def calculate(name):
    print('What is the result of the expression?')
    for i in range(3):
        number1 = random.randint(1,25)
        number2 = random.randint(1,10)
        operation = random.choice('+-*')
        match operation:
            case '+':
                correct_answer = number1 + number2
            case '-':
                correct_answer = number1 - number2
            case '*':
                correct_answer = number1 * number2
        print(f'Question: {number1} {operation} {number2}')
        answer = prompt.integer('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
