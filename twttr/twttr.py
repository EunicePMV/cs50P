user_input = input('Input:')
new_word = ''
vowel = 'a e i o u A E I O U'
for letter in user_input:
    if letter in vowel:
        continue
    new_word += letter

print('Output:', new_word)
