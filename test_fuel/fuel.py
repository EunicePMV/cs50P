class InvalidNumerator(Exception):
    pass

def main():
    fraction = input('Fraction: ')
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    try:
        num, denom = fraction.split('/')
        num = int(num)
        denom = int(denom)

        if num > denom:
            raise InvalidNumerator

        percent = round(num/denom*100)
        return percent
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    except InvalidNumerator:
        continue

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()

# done = False
# while not done:
#     try:
#         fraction = input('Fraction: ')
#         num, denom = fraction.split('/')
#         num = int(num)
#         denom = int(denom)

#         if num > denom:
#             raise InvalidNumerator

#         percent = round(num/denom*100)

#         if percent >= 99:
#             print('F')
#         elif percent <= 1:
#             print('E')
#         else:
#             print(f'{percent}%')
#         done = True
#     except ValueError:
#         continue
#     except ZeroDivisionError:
#         continue
#     except InvalidNumerator:
#         continue
