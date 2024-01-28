import random
import brain_games.scripts.games_logic as gl


def main():
    name = gl.hello()
    prime(name)


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(gl.GAMES_COUNT):
        number = random.randint(1, 100)
        correct_answer = gl.is_prime(number)
        result = gl.is_correct_string(name, number, correct_answer)
        if result is False:
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
