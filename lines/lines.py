# expects one command-line argument:
#   - the name or path of a Python file
#   -> output: num of lines

# if file:
#   - does not end in .py
#   - file does not exist
# exit: sys.exit

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
            print(lines)
            for line in lines:
                line = line.lstrip(' ')
                print(line)
                if line.startswith('#'):
                    print('comment exist')
                    continue
                # elif line.startswith('"""'):
                #     continue

        except FileNotFoundError:
            sys.exit('File does not exist')

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
