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
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    # ^[0-255]+\.[0-255]+\.[0-255]+\.[0-255]$ -> first trial
    # r"^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]\.){3}([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$"
    if re.search(r"^([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]\.){3}([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
