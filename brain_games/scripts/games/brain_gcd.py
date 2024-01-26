import prompt
import random
import brain_games.scripts.games_logic as gl


def main():
    name = gl.hello()
    gcd(name)


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    for i in range(gl.GAMES_COUNT):
        number1 = random.randint(1,50)
        number2 = random.randint(1,20)
        print(f'Question: {number1} {number2}')
        answer = prompt.integer('Your answer: ')
        correct_answer = gl.gcd(number1, number2)
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()