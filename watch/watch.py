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
    yt_pattern = r"\"https?\:\/\/(www\.)?youtube\.com\/embed\/.*?\""
    matches = re.search(yt_pattern, s)
    if matches:
         shorten_link = convert(matches.group())
         return shorten_link
    else:
        return None

def convert(link):
    replace_pattern = r"(youtube\.com\/embed\/)(\w*)"
    matches_link = re.search(replace_pattern, link)
    if matches_link:
        grp_link = list(matches_link.group(1, 2))
        shorten_link = 'https://youtu.be/' + grp_link[-1]
        return shorten_link


if __name__ == "__main__":
    main()
