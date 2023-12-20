user_input = input('Give me a math expression: ')
x, y, z = user_input.split(' ')
x = float(x)
z = float(z)
match y:
    case '+':
        print(x + z)
    case '-':
        print(x - z)
    case '*':
        print(x * z)
    case '/':
        print(x / z)
