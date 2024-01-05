import random


def main():
    # should prompt 1,2, or 3; else reprompt
    lvl = get_level()

    # output EEE if not correct or not even a number, prompt the user again until 3 tries, the program should output the correct answer
    # output the scores
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
            if sum == X+Y:
                print('correct')
                continue



def get_level():
    valid_lvls = [1,2,3]
    while True:
        lvl = input('Level: ')
        if int(lvl) in valid_lvls:
            return int(lvl)


def generate_integer(level):
    # generate non-negative int with level digits or raises ValueError if level not 1, 2, or 3
    X = random.randint(1, level)
    Y = random.randint(1, level)
    return X, Y


if __name__ == "__main__":
    main()

# If David were to answer incorrectly, the toy would display EEE
# after three incorrect answers for the same problem, display the correct answer: 4 + 0 = 4
