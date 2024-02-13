import sys
import csv

def main():
    try:
        file = sys.argv[1]
        second_file = sys.argv[2]

        try:
            second_arg = sys.argv[3]
            if second_arg:
                sys.exit('Too many command-line arguments')
        except IndexError:
            if not file.endswith('.csv'):
                sys.exit('Not a CSV file')

        try:
            with open(file, newline='') as f:
                csv_cleaner(f)

        except FileNotFoundError:
            sys.exit('Could not read ' + file)

    except IndexError:
        sys.exit('Too few command-line arguments')

def csv_cleaner(file):
    reader = csv.DictReader(file)
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        fullname = row['name']
        house = row['house']
        lastname, firstname = fullname.split(',')
        print({'first': firstname, 'last': lastname, 'house':house})

if __name__ == "__main__":
    main()
