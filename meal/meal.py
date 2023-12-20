def main():
    user_input = input('Give me a time: ')
    convert(user_input)


def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    minutes /= 60
    hours += minutes
    print(hours)


if __name__ == "__main__":
    main()
