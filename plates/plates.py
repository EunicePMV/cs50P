
# numbers should be in the end

def main():
    plate = input("Plate: ")
    is_valid(plate)
    # if is_valid(plate):
    #     print("Valid")
    # else:
    #     print("Invalid")


def is_valid(s):
    special_char = '. [@_!$%^&*()<>?/\\|}{~:]#'
    if len(s) >= 2 and len(s) <= 6:
        if special_char in s:
            return False

        for pos, letter in enumerate(s):
            if letter.isdigit():
                sub_string = s[pos:]
                print(sub_string.isdigit())




main()
