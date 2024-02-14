import re
import sys

# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string
# []    set of characters
# [^]   complementing the set
# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    # get the src link
    # http://www.youtube.com/embed/xvFZjo5PgG0
    matches = re.search(r"^(<iframe \w) (src=\"https?://(www\.)?youtube\.com/embed/\w\) \w><iframe>$")", s, re.IGNORECASE)
    matches.group(1)



...


if __name__ == "__main__":
    main()
