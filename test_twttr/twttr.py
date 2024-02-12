def main():
    user_input = input('Input:')
    print(shorten(user_input))


def value(greeting):
    user_input = input('Input:')
    new_word = ''
    vowel = 'aeiouAEIOU'
    for letter in user_input:
        if letter in vowel:
            continue
        new_word += letter
    return new_word

if __name__ == "__main__":
    main()
