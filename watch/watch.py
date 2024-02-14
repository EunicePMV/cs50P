import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    # get the src link
    matches = re.search(r"^(src)=\"(.)\"$", s)
    matches.group()



...


if __name__ == "__main__":
    main()
