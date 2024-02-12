def main():
    word = input('Input:')
    print(shorten(word))

def shorten(word):
    new_word = ''
    vowel = 'aeiouAEIOU'
    for letter in word:
        if letter in vowel:
            continue
        new_word += letter

    return new_word

if __name__ == "__main__":
    main()
