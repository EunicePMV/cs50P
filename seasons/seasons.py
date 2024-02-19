from datetime import date
import sys, inflect


def main():
    get_mins(input('Date of Birth: '))

def get_mins(birthdate):
    try:
        # check if input is valid
        birthdate = date.fromisoformat(birthdate)
        print(birthdate)
    except ValueError:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()
