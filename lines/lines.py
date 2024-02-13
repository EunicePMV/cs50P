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

    # check if there's an argument
    if sys.argv[2]:
        print 
    # check if there's too many arguments
    # check if the argument is .py file

if __name__ == "__main__":
    main()
