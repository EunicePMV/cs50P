user_input = input('Input:')
new_word = ''
for letter in user_input:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        continue
    new_word += letter

print('Output:', new_word)
