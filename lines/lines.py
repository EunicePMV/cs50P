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

        # check if there's an argument
        if sys.argv[2]:
            sys.exit('Too many command-line arguments')
        elif command_line_arg.endswith('.py'):
            print(command_line_arg.endswith('.py'))
    except IndexError:
        sys.exit('Too few command-line arguments')


    # check if there's too many arguments
    # check if the argument is .py file

if __name__ == "__main__":
    main()
