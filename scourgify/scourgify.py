import sys

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
            with open(file, 'r') as f:
                lines = f.readlines()

        except FileNotFoundError:
            sys.exit('Could not read ' + file)

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
