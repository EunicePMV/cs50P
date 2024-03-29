import sys
import os
from PIL import Image, ImageOps

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
            elif os.path.splitext(file)[1] != os.path.splitext(second_file)[1]:
                sys.exit('Input and output have different extension')

        try:
            shirt = Image.open("shirt.png")
            shirt_size = shirt.size
            shirt_mask = shirt.convert('RGBA')

            muppet = Image.open(file)
            muppet = ImageOps.fit(muppet, shirt_size)

            muppet.paste(shirt, shirt_mask)
            muppet.save(second_file)

        except FileNotFoundError:
            sys.exit('Input does not exist')

    except IndexError:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
