def convert(user_input):
    if ':)' in user_input:
        print(user_input.replace(':)', '🙂'))
    elif ':(' in user_input:
        print(user_input.replace(':(', '🙁'))
    elif ':)' in user_input and ':(' in user_input:

def main():
    user_input = input('Give me a word/sentence: ')
    convert(user_input)

main()
