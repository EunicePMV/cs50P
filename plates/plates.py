def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    special_char = '. [@_!$%^&*()<>?/\\|}{~:]#'
    substring = ''
    if len(s) >= 2 and len(s) <= 6:
        if special_char in s:
            return False
        for pos, letter in enumerate(s):
            if letter.isdigit():
                if letter == '0':
                    return False
                elif s[pos:].isdigit():
                    print(s[pos:])
                    return True
        # if substring.isdigit():
        #     return True
        # if substring.isalpha():
        #     return True
    else:
        return False

main()
