def convert(user_input):
    # convert the emoticon here
    user_input.replace(':)', 'str(🙂)')
    print(user_input)

def main():
    user_input = input('Give me a word/sentence: ')
    convert(user_input)

main()
