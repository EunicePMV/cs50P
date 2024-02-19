from validator_collection import validators, errors

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        valid = validators.email(s)
        return valid
    except ValueError or errors.EmptyValueError:
        return False


if __name__ == "__main__":
    main()
