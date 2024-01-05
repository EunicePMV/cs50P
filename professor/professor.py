import random


def main():
    # should prompt 1,2, or 3; else reprompt
    lvl = get_level()

    # generate 10 math probs, X and Y random positive int: X + Y =
    # X, Y = generate_integer(lvl)

    # output EEE if not correct or not even a number, prompt the user again until 3 tries, the program should output the correct answer
    # output the scores


def get_level():
    while True:
        lvl = input('Level: ')
        if lvl.isnumeric() and lvl != '0':
            return int(lvl)


def generate_integer(level):
    valid_lvl = [1, 2, 3]
    # generate non-negative int with level digits or raises ValueError if level not 1, 2, or 3
    ...


if __name__ == "__main__":
    main()

# If David were to answer incorrectly, the toy would display EEE
# after three incorrect answers for the same problem, display the correct answer: 4 + 0 = 4
