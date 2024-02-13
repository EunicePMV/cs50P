import sys

def main():
    try:
        file = sys.argv[1]

        try:
            second_arg = sys.argv[2]
            if second_arg:
                sys.exit('Too many command-line arguments')
        except IndexError:
            if not file.endswith('.py'):
                sys.exit('Not a Python file')

        try:
            with open(file, 'r') as f:
                lines = f.readlines()

            num_lines = 0
            for line in lines:
                line = line.lstrip(' ')
                if line.startswith('#'):
                    continue
                elif line.startswith('"""'):
                    continue
                elif line == '\n':
                    continue
                num_lines += 1
            print(num_lines)

        except FileNotFoundError:
            sys.exit('File does not exist')

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
