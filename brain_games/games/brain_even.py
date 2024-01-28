import random
import brain_games.scripts.games_logic as gl


def main():
    name = gl.hello()
    even(name)


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(gl.GAMES_COUNT):
        number = random.randint(1, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        result = gl.is_correct_string(name, number, correct_answer)
        if result is False:
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
