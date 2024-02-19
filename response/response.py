from validator_collection import validators, errors

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        valid = validators.email(s)
        if valid:
            return True
        else:
            return False
    except (ValueError, errors.EmptyValueError, errors.):
        return False


if __name__ == "__main__":
    main()
