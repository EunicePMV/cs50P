import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    # invalid: yummy, yum, album
    # valid: ' um ', 'um', 'um.,?!'
    # 1st pattern: \s?um[\s\.\,\?\!]*?[^\w]
    # match the string if walang katabing character
    sub_pattern = r"\bum\b"
    found = re.findall(sub_pattern, s)
    return len(found)


if __name__ == "__main__":
    main()
