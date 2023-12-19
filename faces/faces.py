def convert(user_input):
    # convert the emoticon here
    user_input.replace(':)', '🙂')
    print(user_input)

    # if there is ':)' replace the emoticon
    

def main():
    user_input = input('Give me a word/sentence: ')
    convert(user_input)

main()
