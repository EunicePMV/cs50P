import sys
import os
import Pillow

def main():
    try:
        file = sys.argv[1]
        second_file = sys.argv[2]

        try:
            second_arg = sys.argv[3]
            if second_arg:
                sys.exit('Too many command-line arguments')
        except IndexError:
            if not second_file.endswith(('.jpg', '.jpeg', '.png')) or not file.endswith(('.jpg', '.jpeg', '.png')):
                sys.exit('Invalid output')
            elif os.path.splitext(file) != os.path.splitext(second_file):
                sys.exit('Input and output have different extension')

        try:
            shirt = Image.open("shirt.png")
            size = shirt.size

            muppet = Image.open(file)
            new_img = 

        except FileNotFoundError:
            sys.exit('Input does not exist')

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
