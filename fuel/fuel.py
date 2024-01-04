
class InvalidNumerator(Exception):
    pass

done = False
while not done:
    try:
        fraction = input('Fraction: ')
        num, denom = fraction.split('/')
        num = int(num)
        denom = int(denom)

        if num > denom:
            raise InvalidNumerator

        percent = round(num/denom*100)

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
        continue
