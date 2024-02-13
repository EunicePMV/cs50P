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
        command_line_arg = sys.argv[1]

        try:
            second_arg = sys.argv[2]
            if second_arg:
                sys.exit('Too many command-line arguments')
        except IndexError:
            if not command_line_arg.endswith('.py'):
                sys.exit('Not a Python file')

            

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
