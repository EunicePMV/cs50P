import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # get the src link
    matches = re.search(r"^(src)=\"(.)\"$", s)
    matches.group(1)



...


if __name__ == "__main__":
    main()
