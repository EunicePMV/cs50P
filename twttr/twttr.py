user_input = input('Input:')
new_word = ''
vowel = 'aeiouAEIOU'
for letter in user_input:
    if letter in vowel:
        continue
    new_word += letter

print('Output:', new_word)
