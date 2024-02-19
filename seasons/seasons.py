from datetime import date, timedelta
import sys, inflect


def main():
    get_mins(input('Date of Birth: '))

def get_mins(birthdate):
    try:
        # check if input is valid
        birthdate = date.fromisoformat(birthdate)
        current_date = date.today()
        # current_date = date.fromisoformat('2000-01-01')
        age = current_date - birthdate
        total_mins = round(age.days * 24 * 60)

        p = inflect.engine()
        word_mins = p.number_to_words(total_mins).capitalize()
        print(f'{word_mins} minutes')
    except ValueError:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()
