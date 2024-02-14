import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# in the ip address should be the following:
#   - ranging from 0-255
#   - only has 3 dots (255.255.255.255)
#   - only has numbers
#   - no other special characters other than "dot"
def validate(ip):
    ...


...


if __name__ == "__main__":
    main()
