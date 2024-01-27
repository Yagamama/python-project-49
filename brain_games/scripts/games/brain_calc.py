import random
import brain_games.scripts.games_logic as gl


def main():
    name = gl.hello()
    calculate(name)


def calculate(name):
    print('What is the result of the expression?')
    for i in range(gl.GAMES_COUNT):
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
        question = str(number1) + " " + operation + " " + str(number2)
        result = gl.is_correct(name,question, correct_answer)
        if result == False:
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()