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
            return False
        if s.isdigit() and len(s) == 2:
            return False

        for pos, letter in enumerate(s):
            if letter.isdigit():
                if letter == '0':
                    return False
                elif s[pos:].isdigit():
                    if s[:2].isalpha():
                        return True
                    else:
                        return False
            elif letter in special_char:
                return False
    else:
        return False

if __name__ == "__main__":
    main()
