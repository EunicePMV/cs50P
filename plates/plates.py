# must start with atleast 2 letters
# n >= 2 and n <= 6
# numbers should be in the end
# no periods, space or punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()
