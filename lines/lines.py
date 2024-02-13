# expects one command-line argument:
#   - the name or path of a Python file
#   -> output: num of lines

# if file:
#   - does not end in .py
#   - file does not exist
# exit: sys.exit

import sys

def main():
    # get the user input in the command-line
    print(sys.argv[1])

if __name__ == "__main__":
    main()
