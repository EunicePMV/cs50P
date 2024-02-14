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


# in the ip address should be the following:
#   - ranging from 0-255
#   - only has 3 dots (255.255.255.255)
#   - only has numbers
#   - no other special characters other than "dot"
def validate(ip):
    if re.search(r"^[0-255]+\.[0-255]+\.[0-255]+\.[0-255]$", ip):
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
