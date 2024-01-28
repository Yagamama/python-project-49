import random
import brain_games.scripts.games_logic as gl


def main():
    name = gl.hello()
    gcd(name)


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    for i in range(gl.GAMES_COUNT):
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 20)
        question = str(number1) + " " + str(number2)
        correct_answer = gl.gcd(number1, number2)
        result = gl.is_correct(name, question, correct_answer)
        if result is False:
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
