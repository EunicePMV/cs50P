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
            if not second_file.endswith('.jpg') or not file.endswith('.jpg'):
                sys.exit('Invalid output')

        try:
            with open(file, newline='') as f:
                clean_data_lst = csv_cleaner(f)

            with open(second_file, 'w', newline='') as f:
                csv_write(f, clean_data_lst)

        except FileNotFoundError:
            sys.exit('Could not read ' + file)

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
