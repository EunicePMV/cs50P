
class InvalidNumerator(Exception):
    pass

done = False
while not done:
    try:
        fraction = input('Fraction: ')
        num, denom = fraction.split('/')

        if num > denom:
            raise InvalidNumerator

        percent = round(int(num)/int(denom)*100)
        print(percent)

        if percent >= 99:
            print('F')
        elif percent <= 1:
            print('E')
        else:
            print(f'{percent}%')
        done = True
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    except InvalidNumerator:
        break



# 1/4 - 25%, 1/2 - 50%, 3/4 - 75%
# if 1% remains - E
# if 99% remains - F
# if X and Y is not integer, X > Y, or Y=0

# :( input of 1/3 yields output of 33%
#     expected "33%", not "34%\n"

# :( input of 99/100 yields output of F
#     Did not find "F" in "Fraction: "


# :( input of 10/3 results in reprompt
#     expected program to reject input, but it did not
