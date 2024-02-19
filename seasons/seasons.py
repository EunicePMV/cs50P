from datetime import date
import sys, inflect


def main():
    print(get_mins(input('Date of Birth: ')))

def get_mins(birthdate, test_date=None):
    try:
        # check if input is valid
        birthdate = date.fromisoformat(birthdate)
        current_date = date.fromisoformat(test_date) if test_date else date.today()
        age = current_date - birthdate
        total_mins = round(age.days * 24 * 60)

        p = inflect.engine()
        word_mins = p.number_to_words(total_mins, andword='').capitalize()
        return f'{word_mins} minutes'
    except ValueError:
        # raise ValueError("Invalid date")
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()
