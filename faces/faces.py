def convert(user_input):
    # find the emoticon
    index = user_input.find(':)') if  else user_input.find(':(')
    print(index)

    # if index != 0:
    #     user_input[]

    # # convert the emoticon into emoji

    # # convert the emoticon here
    # user_input.replace(')', '🙂')
    # print(user_input)

    # if there is ':)' replace the emoticon


def main():
    user_input = input('Give me a word/sentence: ')
    convert(user_input)

main()

