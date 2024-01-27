import prompt
import random
import brain_games.scripts.games_logic as gl


def main():
    name = gl.hello()
    progression(name)


def progression(name):
    print('What number is missing in the progression?')
    for i in range(gl.GAMES_COUNT):
        step = random.randint(1,5)
        first_number = random.randint(1,20)
        hiden = random.randint(0,9)
        list_of_numbers = range(first_number, 10*step+first_number, step)
        line_of_numbers = ''
        correct_answer = 0
        for j in range(10):
            if j == hiden:
                line_of_numbers = line_of_numbers + '.. '
                correct_answer = list_of_numbers[j]
            else: 
                line_of_numbers = line_of_numbers + str(list_of_numbers[j]) + " "
        result = gl.is_correct(name,line_of_numbers, correct_answer)
        if result == False:
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()