import sys
import csv

def main():
    try:
        file = sys.argv[1]

        try:
            second_arg = sys.argv[2]
            if second_arg:
                sys.exit('Too many command-line arguments')
        except IndexError:
            if not file.endswith('.csv'):
                sys.exit('Not a CSV file')

        try:
            with open(file, newline='') as f:
                prettier(f)

        except FileNotFoundError:
            sys.exit('File does not exist')

    except IndexError:
        sys.exit('Too few command-line arguments')

def prettier(file):
    spamreader = csv.reader(file, delimiter=',')
    for row in spamreader:
        print(', '.join(row))

if __name__ == "__main__":
    main()
