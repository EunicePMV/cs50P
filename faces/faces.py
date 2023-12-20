def convert(user_input):
    if user_input.find(':)'):
        user_input.replace
        user_input[user_input.find(':)')] = '🙂'
        user_input[user_input.find(':)') + 1] = ''
    elif user_input.find(':('):
        user_input[user_input.find(':(')] = '🙁'
        user_input[user_input.find(':(') + 1] = ''


def main():
    user_input = input('Give me a word/sentence: ')
    convert(user_input)

# main()


user_input = input('Give me a word/sentence: ')
print(user_input.replace(':)', '🙂'))
