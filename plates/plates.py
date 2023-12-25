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
        if s.isalpha():
            return True
        elif s.isdigit() and len(s) == 2:
            return False

        for pos, letter in enumerate(s):
            if letter.isdigit():
                if letter == '0':
                    return False
                elif s[pos:].isdigit():
                    return True
            elif letter in special_char:
                return False
    else:
        return False

main()
