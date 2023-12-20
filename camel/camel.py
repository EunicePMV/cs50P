# initialize empty string
# loop over to the current string
# find the uppercase letter
# keep on adding char in the empty string

user_input = input('Give me camel case: ')
snake_case = ''

for letter in user_input:
    if letter.isupper():
        snake_case = snake_case + '_' + letter.lower()
    else:
        snake_case = snake_case + letter

print('snake case conversion: ' + snake_case)
