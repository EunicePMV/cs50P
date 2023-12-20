def main():
    user_input = input('Give me a time: ')
    hours = convert(user_input)

    if hours 


def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    minutes /= 60
    hours += minutes
    return hours


if __name__ == "__main__":
    main()
