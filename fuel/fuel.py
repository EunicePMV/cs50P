
class InvalidNumerator(Exception):
    pass

done = False
while not done:
    try:
        fraction = input('Fraction: ')
        num, denom = fraction.split('/')

        if num > denom:
            break

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
        continue



# 1/4 - 25%, 1/2 - 50%, 3/4 - 75%
# if 1% remains - E
# if 99% remains - F
# if X and Y is not integer, X > Y, or Y=0
