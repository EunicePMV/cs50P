def convert(user_input):
    if ':)' in user_input and ':(' in user_input:
        user_input.replace(':)', '🙂')
        user_input.replace(':(', '🙁')
        print(user_input)
    elif ':)' in user_input:
        print(user_input.replace(':)', '🙂'))
    elif ':(' in user_input:
        print(user_input.replace(':(', '🙁'))

def main():
    user_input = input('Give me a word/sentence: ')
    convert(user_input)

main()
