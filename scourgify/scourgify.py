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
                clean_data_lst = csv_cleaner(f)

            with open(second_file, 'w', newline='') as f:
                csv_write(f, clean_data_lst)

        except FileNotFoundError:
            sys.exit('Could not read ' + file)

    except IndexError:
        sys.exit('Too few command-line arguments')

def csv_cleaner(file):
    reader = csv.DictReader(file)
    cleaned_data = []
    for row in reader:
        fullname = row['name']
        house = row['house']
        lastname, firstname = fullname.split(',').strip()
        cleaned_data.append({'first name': firstname, 'last name': lastname, 'house':house})
    return cleaned_data

def csv_write(file, data):
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

if __name__ == "__main__":
    main()
