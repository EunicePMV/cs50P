import random


def main():
    # should prompt 1,2, or 3; else reprompt
    lvl = get_level()

    scores = 0
    trials = 3
    for _ in range(10):
        # generate 10 math probs, X and Y random positive int: X + Y =
        X, Y = generate_integer(lvl)
        total = X+Y

        # given 3 trials for each problem
        trials = 3
        while trials != 0:
            sum = input(f'{X} + {Y} = ')
            if int(sum) == total:
                trials = 0
                scores += 1
            else:
                # output EEE if incorrect, and subtract num of trials
                print('EEE')
                trials -= 1

            if trials == 0:
                print(f'{X} + {Y} = {total}')
    print(f'Score: {scores}')



def get_level():
    valid_lvls = [1,2,3]
    while True:
        try:
            lvl = int(input('Level: '))
            if lvl in valid_lvls:
                return lvl
        except ValueError:
            continue


def generate_integer(level):
    # generate non-negative int with level digits or raises ValueError if level not 1, 2, or 3
    if level == 1:
        X = random.randint(1, 10)
        Y = random.randint(1, 10)
    elif level == 2:
        X = random.randint(1, 20)
        Y = random.randint(1, 20)
    elif level == 3:
        X = random.randint(1, 30)
        Y = random.randint(1, 30)
    else:
        raise ValueError
    return X, Y


if __name__ == "__main__":
    main()
