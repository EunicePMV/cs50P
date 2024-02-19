import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    sub_pattern = r"\bum\b"
    found = re.findall(sub_pattern, s)
    return len(found)


if __name__ == "__main__":
    main()
