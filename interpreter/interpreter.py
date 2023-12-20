user_input = input('Give me a math expression: ')
x, y, z = user_input.split(' ')
x = float(x)
y = float(y)
match y:
    case '+':
        print(x + y)
    case '-':
        print(x - y)
    case '*':
        print(x * y)
    case '/':
        print(x / y)
